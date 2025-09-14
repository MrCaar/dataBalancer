import pandas as pd
import os
import glob
from collections import defaultdict
import numpy as np
from typing import Dict, List
import argparse

class SmartMixSplit:
    def __init__(self, input_dir: str = "input", output_dir: str = "output"):
        """
        CSV dosyalarını birleştiren ve belirtilen yıldız dağılımına göre 
        homojen dil dağılımı ile örnekleme yapan sınıf.
        
        Args:
            input_dir: CSV dosyalarının bulunduğu klasör
            output_dir: Çıktı dosyalarının kaydedileceği klasör
        """
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.combined_data = None
        
    def read_csv_files(self) -> pd.DataFrame:
        """
        Input klasöründeki tüm CSV dosyalarını okur ve birleştirir.
        
        Returns:
            Birleştirilmiş DataFrame
        """
        csv_files = glob.glob(os.path.join(self.input_dir, "*.csv"))
        
        if not csv_files:
            raise FileNotFoundError(f"'{self.input_dir}' klasöründe CSV dosyası bulunamadı!")
        
        print(f"{len(csv_files)} CSV dosyası bulundu:")
        for file in csv_files:
            print(f"  - {os.path.basename(file)}")
        
        dataframes = []
        file_stats = {}  # Her dosya için istatistik tutalım
        
        for file in csv_files:
            try:
                df = pd.read_csv(file)
                filename = os.path.basename(file)
                print(f"'{filename}' dosyası okundu: {len(df)} satır")
                
                # Bu dosya için boş comment istatistikleri
                if 'comment' in df.columns:
                    initial_count = len(df)
                    # Boş comment'ları tespit et
                    empty_mask = (
                        df['comment'].isna() | 
                        (df['comment'].astype(str).str.strip() == '') |
                        (df['comment'].astype(str).str.strip() == 'nan')
                    )
                    empty_count = empty_mask.sum()
                    
                    if empty_count > 0:
                        # Yıldız bazında boş comment analizi
                        empty_data = df[empty_mask]
                        if 'score' in empty_data.columns:
                            score_breakdown = empty_data['score'].value_counts().sort_index().to_dict()
                        else:
                            score_breakdown = {}
                        
                        file_stats[filename] = {
                            'total': initial_count,
                            'empty': empty_count,
                            'valid': initial_count - empty_count,
                            'score_breakdown': score_breakdown
                        }
                
                dataframes.append(df)
            except Exception as e:
                print(f"HATA: '{file}' dosyası okunamadı: {e}")
        
        if not dataframes:
            raise ValueError("Hiçbir CSV dosyası başarıyla okunamadı!")
        
        # Tüm dataframe'leri birleştir
        combined_df = pd.concat(dataframes, ignore_index=True)
        print(f"\nToplam {len(combined_df)} satır birleştirildi.")
        
        # Gerekli sütunları kontrol et
        required_columns = ['profile_name', 'score', 'comment', 'language', 'contribution', 'date', 'url']
        missing_columns = [col for col in required_columns if col not in combined_df.columns]
        
        if missing_columns:
            print(f"UYARI: Eksik sütunlar: {missing_columns}")
            print(f"Mevcut sütunlar: {list(combined_df.columns)}")
        
        # Boş comment'ları filtrele ve detaylı rapor ver
        if 'comment' in combined_df.columns:
            initial_count = len(combined_df)
            
            # Filtrelenmeden önce yıldız dağılımını kaydet
            if 'score' in combined_df.columns:
                original_score_dist = combined_df['score'].value_counts().sort_index().to_dict()
            
            # Boş comment'ları tespit et
            empty_mask = (
                combined_df['comment'].isna() | 
                (combined_df['comment'].astype(str).str.strip() == '') |
                (combined_df['comment'].astype(str).str.strip() == 'nan')
            )
            
            if empty_mask.sum() > 0:
                # Boş comment'ların yıldız dağılımı
                empty_data = combined_df[empty_mask]
                if 'score' in empty_data.columns:
                    empty_score_breakdown = empty_data['score'].value_counts().sort_index().to_dict()
                else:
                    empty_score_breakdown = {}
                
                # Boş olmayan veriyi filtrele
                combined_df = combined_df[~empty_mask]
                filtered_count = len(combined_df)
                removed_count = initial_count - filtered_count
                
                print(f"\n{'='*60}")
                print("BOŞ COMMENT FİLTRELEME RAPORU")
                print(f"{'='*60}")
                
                # Dosya bazında rapor
                total_empty_files = 0
                for filename, stats in file_stats.items():
                    if stats['empty'] > 0:
                        total_empty_files += 1
                        percentage = (stats['empty'] / stats['total']) * 100
                        print(f"\n📁 {filename}:")
                        print(f"  • Toplam satır: {stats['total']}")
                        print(f"  • Boş comment: {stats['empty']} ({percentage:.1f}%)")
                        print(f"  • Geçerli satır: {stats['valid']}")
                        
                        if stats['score_breakdown']:
                            print(f"  • Yıldız bazında boş comment dağılımı:")
                            for score, count in sorted(stats['score_breakdown'].items()):
                                print(f"    - {score} yıldız: {count} boş comment")
                
                if total_empty_files == 0:
                    print("\n✅ Hiçbir dosyada boş comment bulunamadı!")
                else:
                    print(f"\n📊 GENEL ÖZET:")
                    print(f"  • Boş comment içeren dosya sayısı: {total_empty_files}")
                    print(f"  • Toplam filtrelenen boş comment: {removed_count}")
                    print(f"  • Kalan geçerli yorum: {filtered_count}")
                    
                    if empty_score_breakdown:
                        print(f"\n⭐ TOPLAM YILDIZ BAZINDA BOŞ COMMENT DAĞILIMI:")
                        for score in sorted(empty_score_breakdown.keys()):
                            count = empty_score_breakdown[score]
                            total_for_score = original_score_dist.get(score, 0)
                            if total_for_score > 0:
                                percentage = (count / total_for_score) * 100
                                print(f"  • {score} yıldız: {count} boş comment (toplam {score} yıldızlının %{percentage:.1f}'i)")
                            else:
                                print(f"  • {score} yıldız: {count} boş comment")
                
                print(f"{'='*60}")
            else:
                print(f"\n✅ Hiçbir boş comment bulunamadı! Tüm {initial_count} satır geçerli.")
        
        self.combined_data = combined_df
        return combined_df
    
    def analyze_data(self) -> Dict:
        """
        Veriyi analiz eder ve istatistikleri döndürür.
        
        Returns:
            Analiz sonuçları
        """
        if self.combined_data is None:
            raise ValueError("Önce CSV dosyalarını okuyun!")
        
        df = self.combined_data
        
        analysis = {
            'total_rows': len(df),
            'unique_airports': df['profile_name'].nunique() if 'profile_name' in df.columns else 0,
            'score_distribution': df['score'].value_counts().sort_index().to_dict() if 'score' in df.columns else {},
            'language_distribution': df['language'].value_counts().to_dict() if 'language' in df.columns else {},
            'airports': df['profile_name'].value_counts().to_dict() if 'profile_name' in df.columns else {}
        }
        
        return analysis
    
    def print_analysis(self, analysis: Dict):
        """
        Analiz sonuçlarını yazdırır.
        """
        print("\n" + "="*50)
        print("VERİ ANALİZİ")
        print("="*50)
        print(f"Toplam satır sayısı: {analysis['total_rows']}")
        print(f"Benzersiz havalimanı sayısı: {analysis['unique_airports']}")
        
        print(f"\nYıldız dağılımı:")
        for score, count in sorted(analysis['score_distribution'].items()):
            percentage = (count / analysis['total_rows']) * 100
            print(f"  {score} yıldız: {count} ({percentage:.1f}%)")
        
        print(f"\nDil dağılımı:")
        for lang, count in sorted(analysis['language_distribution'].items(), key=lambda x: x[1], reverse=True):
            percentage = (count / analysis['total_rows']) * 100
            print(f"  {lang}: {count} ({percentage:.1f}%)")
        
        print(f"\nHavalimanı dağılımı:")
        for airport, count in sorted(analysis['airports'].items(), key=lambda x: x[1], reverse=True)[:10]:
            percentage = (count / analysis['total_rows']) * 100
            print(f"  {airport}: {count} ({percentage:.1f}%)")
        if len(analysis['airports']) > 10:
            print(f"  ... ve {len(analysis['airports']) - 10} havalimanı daha")
    
    def create_balanced_sample(self, star_distribution: Dict[int, int]) -> pd.DataFrame:
        """
        Belirtilen yıldız dağılımına göre homojen dil dağılımı ile örnekleme yapar.
        
        Args:
            star_distribution: {yıldız_sayısı: kaç_tane_alınacak} formatında dict
            
        Returns:
            Örneklenmiş DataFrame
        """
        if self.combined_data is None:
            raise ValueError("Önce CSV dosyalarını okuyun!")
        
        df = self.combined_data.copy()
        
        # Boş değerleri ve boş comment'ları temizle
        df = df.dropna(subset=['score', 'language', 'profile_name'])
        
        # Comment kontrolü - boş comment'ları filtrele
        if 'comment' in df.columns:
            initial_count = len(df)
            df = df[
                df['comment'].notna() & 
                (df['comment'].astype(str).str.strip() != '') &
                (df['comment'].astype(str).str.strip() != 'nan')
            ]
            filtered_count = len(df)
            removed_count = initial_count - filtered_count
            if removed_count > 0:
                print(f"Örnekleme sırasında {removed_count} boş comment içeren satır daha filtrelendi.")
        
        # Score'u integer'a çevir
        df['score'] = df['score'].astype(int)
        
        sampled_data = []
        
        print("\n" + "="*50)
        print("ÖRNEKLEME İŞLEMİ")
        print("="*50)
        
        for star_rating, target_count in star_distribution.items():
            print(f"\n{star_rating} yıldızlı yorumlar için {target_count} adet seçiliyor...")
            
            # Bu yıldız puanına sahip tüm yorumları filtrele
            star_data = df[df['score'] == star_rating].copy()
            
            if len(star_data) == 0:
                print(f"  UYARI: {star_rating} yıldızlı hiç yorum bulunamadı!")
                continue
            
            if len(star_data) < target_count:
                print(f"  UYARI: {star_rating} yıldızlı sadece {len(star_data)} yorum var, {target_count} istendi!")
                sampled_data.append(star_data)
                continue
            
            # Dil ve havalimanı dağılımını hesapla
            language_counts = star_data['language'].value_counts()
            airport_counts = star_data['profile_name'].value_counts()
            
            print(f"  Mevcut {star_rating} yıldızlı yorum sayısı: {len(star_data)}")
            print(f"  Dil sayısı: {len(language_counts)}")
            print(f"  Havalimanı sayısı: {len(airport_counts)}")
            
            # Homojen dağılım için her dilden ve havalimanından proportional olarak al
            selected_indices = []
            
            # Her dil için orantılı örnekleme
            for language in language_counts.index:
                lang_data = star_data[star_data['language'] == language]
                lang_proportion = len(lang_data) / len(star_data)
                lang_target = max(1, int(target_count * lang_proportion))
                
                # Her havalimanından da orantılı al
                lang_selected = []
                airport_counts_in_lang = lang_data['profile_name'].value_counts()
                
                for airport in airport_counts_in_lang.index:
                    airport_data = lang_data[lang_data['profile_name'] == airport]
                    airport_proportion = len(airport_data) / len(lang_data)
                    airport_target = max(1, int(lang_target * airport_proportion))
                    airport_target = min(airport_target, len(airport_data))
                    
                    if airport_target > 0:
                        selected = airport_data.sample(n=airport_target, random_state=42)
                        lang_selected.extend(selected.index.tolist())
                
                # Eğer yeterli seçilmediyse, kalan kısmı rastgele ekle
                remaining_needed = lang_target - len(lang_selected)
                if remaining_needed > 0:
                    available_indices = set(lang_data.index) - set(lang_selected)
                    if available_indices:
                        additional = min(remaining_needed, len(available_indices))
                        additional_indices = np.random.choice(
                            list(available_indices), 
                            size=additional, 
                            replace=False
                        )
                        lang_selected.extend(additional_indices.tolist())
                
                selected_indices.extend(lang_selected)
            
            # Hedef sayıya ulaşmak için eksik olanları rastgele ekle
            if len(selected_indices) < target_count:
                remaining_needed = target_count - len(selected_indices)
                available_indices = set(star_data.index) - set(selected_indices)
                if available_indices:
                    additional = min(remaining_needed, len(available_indices))
                    additional_indices = np.random.choice(
                        list(available_indices), 
                        size=additional, 
                        replace=False
                    )
                    selected_indices.extend(additional_indices.tolist())
            
            # Hedef sayıyı aştıysak rastgele azalt
            if len(selected_indices) > target_count:
                selected_indices = np.random.choice(
                    selected_indices, 
                    size=target_count, 
                    replace=False
                ).tolist()
            
            selected_sample = star_data.loc[selected_indices]
            sampled_data.append(selected_sample)
            
            print(f"  Seçilen yorum sayısı: {len(selected_sample)}")
            
            # Seçilen örnekteki dil dağılımını göster
            sample_lang_dist = selected_sample['language'].value_counts()
            print(f"  Seçilen örnekteki dil dağılımı:")
            for lang, count in sample_lang_dist.items():
                percentage = (count / len(selected_sample)) * 100
                print(f"    {lang}: {count} ({percentage:.1f}%)")
        
        # Tüm örnekleri birleştir
        if sampled_data:
            final_sample = pd.concat(sampled_data, ignore_index=True)
            
            # Karıştır
            final_sample = final_sample.sample(frac=1, random_state=42).reset_index(drop=True)
            
            print(f"\nToplam örneklenen yorum sayısı: {len(final_sample)}")
            return final_sample
        else:
            print("HATA: Hiçbir örnekleme yapılamadı!")
            return pd.DataFrame()
    
    def save_results(self, sampled_data: pd.DataFrame, filename: str = "sampled_data.csv"):
        """
        Örneklenen veriyi CSV dosyası olarak kaydeder.
        
        Args:
            sampled_data: Örneklenen DataFrame
            filename: Çıktı dosyası adı
        """
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        output_path = os.path.join(self.output_dir, filename)
        sampled_data.to_csv(output_path, index=False)
        print(f"\nSonuçlar '{output_path}' dosyasına kaydedildi.")
        
        # Özet istatistikleri de kaydet
        summary_path = os.path.join(self.output_dir, "summary.txt")
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write("ÖRNEKLEME ÖZETİ\n")
            f.write("="*50 + "\n")
            f.write(f"Toplam örneklenen satır: {len(sampled_data)}\n\n")
            
            f.write("Yıldız dağılımı:\n")
            score_dist = sampled_data['score'].value_counts().sort_index()
            for score, count in score_dist.items():
                percentage = (count / len(sampled_data)) * 100
                f.write(f"  {score} yıldız: {count} ({percentage:.1f}%)\n")
            
            f.write("\nDil dağılımı:\n")
            lang_dist = sampled_data['language'].value_counts()
            for lang, count in lang_dist.items():
                percentage = (count / len(sampled_data)) * 100
                f.write(f"  {lang}: {count} ({percentage:.1f}%)\n")
            
            f.write("\nHavalimanı dağılımı:\n")
            airport_dist = sampled_data['profile_name'].value_counts()
            for airport, count in airport_dist.items():
                percentage = (count / len(sampled_data)) * 100
                f.write(f"  {airport}: {count} ({percentage:.1f}%)\n")
        
        print(f"Özet istatistikler '{summary_path}' dosyasına kaydedildi.")


def main():
    """
    Ana fonksiyon - programı çalıştırır.
    """
    # Komut satırı argümanları
    parser = argparse.ArgumentParser(description='Havalimanı yorumlarını karıştırıp örnekleyen program')
    parser.add_argument('--input-dir', default='input', help='CSV dosyalarının bulunduğu klasör')
    parser.add_argument('--output-dir', default='output', help='Çıktı dosyalarının kaydedileceği klasör')
    
    args = parser.parse_args()
    
    # SmartMixSplit nesnesini oluştur
    mixer = SmartMixSplit(args.input_dir, args.output_dir)
    
    try:
        # CSV dosyalarını oku ve birleştir
        print("CSV dosyaları okunuyor...")
        combined_data = mixer.read_csv_files()
        
        # Veriyi analiz et
        analysis = mixer.analyze_data()
        mixer.print_analysis(analysis)
        
        # Kullanıcıdan yıldız dağılımını al
        print("\n" + "="*50)
        print("YILDIZ DAĞILIMI BELİRLEME")
        print("="*50)
        print("Her yıldız puanından kaç adet yorum alınacağını belirtin:")
        print("(0 girmeyin eğer o yıldızdan hiç almak istemiyorsanız)")
        
        star_distribution = {}
        for star in [5, 4, 3, 2, 1]:
            while True:
                try:
                    available = analysis['score_distribution'].get(star, 0)
                    count = input(f"{star} yıldızlı yorumlar (mevcut: {available}): ").strip()
                    if count == "":
                        continue
                    count = int(count)
                    if count < 0:
                        print("Negatif sayı giremezsiniz!")
                        continue
                    if count > available:
                        print(f"Mevcut {star} yıldızlı yorum sayısı ({available}) aştınız!")
                        continue
                    if count > 0:
                        star_distribution[star] = count
                    break
                except ValueError:
                    print("Lütfen geçerli bir sayı girin!")
        
        if not star_distribution:
            print("Hiçbir yıldız puanı seçilmedi! Program sonlandırılıyor.")
            return
        
        print(f"\nSeçilen dağılım: {star_distribution}")
        total_target = sum(star_distribution.values())
        print(f"Toplam hedef: {total_target} yorum")
        
        # Örnekleme yap
        sampled_data = mixer.create_balanced_sample(star_distribution)
        
        if len(sampled_data) == 0:
            print("HATA: Örnekleme işlemi başarısız!")
            return
        
        # Sonuçları kaydet
        mixer.save_results(sampled_data)
        
        print("\n" + "="*50)
        print("İŞLEM TAMAMLANDI!")
        print("="*50)
        print(f"Toplam {len(sampled_data)} yorum başarıyla örneklendi ve kaydedildi.")
        
    except Exception as e:
        print(f"\nHATA: {e}")
        return


if __name__ == "__main__":
    main()
