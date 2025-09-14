#!/usr/bin/env python3
"""
Smart Mix Split - Örnek Kullanım Scripti

Bu script programın nasıl kullanılacağını gösterir.
Programlı olarak belirli yıldız dağılımları ile örnekleme yapar.
"""

from smart_mix_split import SmartMixSplit

def example_usage():
    """
    Örnek kullanım fonksiyonu
    """
    print("Smart Mix Split - Örnek Kullanım")
    print("="*50)
    
    # SmartMixSplit nesnesini oluştur
    mixer = SmartMixSplit("input", "output")
    
    try:
        # CSV dosyalarını oku
        print("1. CSV dosyaları okunuyor...")
        combined_data = mixer.read_csv_files()
        
        # Veriyi analiz et
        print("\n2. Veri analizi yapılıyor...")
        analysis = mixer.analyze_data()
        mixer.print_analysis(analysis)
        
        # Örnek yıldız dağılımları
        example_distributions = [
            {
                "name": "Dengeli Dağılım",
                "distribution": {5: 5, 4: 5, 3: 5, 2: 3, 1: 2}
            },
            {
                "name": "Pozitif Odaklı",
                "distribution": {5: 8, 4: 6, 3: 4, 2: 1, 1: 1}
            },
            {
                "name": "Tüm Puanlar Eşit",
                "distribution": {5: 3, 4: 3, 3: 3, 2: 3, 1: 3}
            }
        ]
        
        for i, example in enumerate(example_distributions, 1):
            print(f"\n{'='*50}")
            print(f"ÖRNEK {i}: {example['name']}")
            print(f"{'='*50}")
            print(f"Dağılım: {example['distribution']}")
            
            # Örnekleme yap
            sampled_data = mixer.create_balanced_sample(example['distribution'])
            
            if len(sampled_data) > 0:
                # Sonuçları kaydet
                filename = f"example_{i}_{example['name'].lower().replace(' ', '_')}.csv"
                mixer.save_results(sampled_data, filename)
                print(f"✅ Örnek {i} başarıyla tamamlandı!")
            else:
                print(f"❌ Örnek {i} başarısız oldu!")
        
        print(f"\n{'='*50}")
        print("TÜM ÖRNEKLER TAMAMLANDI!")
        print(f"{'='*50}")
        print("output/ klasörünü kontrol edin.")
        
    except Exception as e:
        print(f"HATA: {e}")

if __name__ == "__main__":
    example_usage()
