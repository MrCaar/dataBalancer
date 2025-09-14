# Smart Mix Split 🛫

[![CI/CD Pipeline](https://github.com/mrcaar/smartMixSplit/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/mrcaar/smartMixSplit/actions)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Issues](https://img.shields.io/github/issues/mrcaar/smartMixSplit)](https://github.com/mrcaar/smartMixSplit/issues)
[![Stars](https://img.shields.io/github/stars/mrcaar/smartMixSplit)](https://github.com/mrcaar/smartMixSplit/stargazers)

**Havalimanı yorumlarını akıllı örnekleme ve veri analizi aracı**

Bu profesyonel Python aracı, havalimanı yorumlarını içeren CSV dosyalarını birleştirerek, belirtilen yıldız dağılımına göre **homojen dil ve havalimanı dağılımı** ile stratified sampling yapar. Araştırma projeleri, veri analizi ve makine öğrenmesi çalışmaları için idealdir.

## ✨ Ana Özellikler

### 🔄 Veri İşleme
- **Çoklu CSV Birleştirme**: Input klasöründeki tüm CSV dosyalarını otomatik olarak birleştirir
- **Akıllı Veri Temizleme**: Boş yorumları tespit eder ve detaylı raporlama yapar
- **Veri Doğrulama**: Eksik sütunları kontrol eder ve uyarı verir

### 📊 Gelişmiş Analiz
- **Kapsamlı İstatistikler**: Yıldız, dil ve havalimanı dağılımlarını analiz eder
- **Detaylı Raporlama**: Dosya bazında boş yorum analizi
- **Görsel İstatistikler**: Yüzdelik dilimlerle birlikte dağılım gösterimi

### 🎯 Stratified Sampling
- **Homojen Dil Dağılımı**: Her yıldız puanında dillerin oransal dağılımı korunur
- **Havalimanı Dengesi**: Her havalimanından adil örnekleme yapılır
- **Kullanıcı Kontrollü**: İstediğiniz yıldız dağılımını belirleyebilirsiniz
- **Akıllı Algoritma**: Eksik kısımları rastgele tamamlar

### 💾 Çıktı ve Raporlama
- **CSV Export**: Örneklenen veriler CSV formatında kaydedilir
- **Özet Raporu**: Detaylı istatistiklerle birlikte summary.txt dosyası
- **Süreç Takibi**: Anlık progress ve debug bilgileri

## 🚀 Hızlı Başlangıç

### Gereksinimler

```bash
pip install -r requirements.txt
```

**Gerekli paketler:**
- pandas >= 1.3.0
- numpy >= 1.20.0

### Temel Kullanım

```bash
# 1. CSV dosyalarınızı input/ klasörüne koyun
# 2. Programı çalıştırın
python smart_mix_split.py

# Özel klasörlerle kullanım
python smart_mix_split.py --input-dir /path/to/csv/files --output-dir /path/to/output
```

## 📁 Proje Yapısı

```
smartMixSplit/
├── 📄 smart_mix_split.py      # Ana SmartMixSplit sınıfı
├── 📄 example_usage.py        # Örnek kullanım scripti
├── 📄 requirements.txt        # Python bağımlılıkları
├── 📂 input/                  # CSV dosyalarını buraya koyun
│   └── turkceData.csv         # Örnek veri dosyası
├── 📂 output/                 # Sonuçlar burada oluşturulur
│   ├── sampled_data.csv       # Örneklenen veriler
│   └── summary.txt            # Detaylı istatistikler
└── 📄 README.md              # Bu dosya
```

## 📋 CSV Veri Formatı

CSV dosyalarınız aşağıdaki sütunları içermelidir:

| Sütun | Açıklama | Örnek |
|-------|----------|-------|
| `profile_name` | Havalimanı adı | "Istanbul Airport" |
| `score` | Yıldız puanı (1-5) | 4 |
| `comment` | Yorum metni | "Great airport experience" |
| `language` | Yorum dili kodu | "en", "tr", "de" |
| `contribution` | Katkı bilgisi | "100 contributions" |
| `date` | Yorum tarihi | "2024-01-15" |
| `url` | Kaynak URL | "https://..." |

## 💻 Kullanım Örnekleri

### 🎮 İnteraktif Kullanım

```bash
python smart_mix_split.py
```

Program size veri analizi gösterecek ve yıldız dağılımını soracak:

```
==================================================
VERİ ANALİZİ
==================================================
Toplam satır sayısı: 125,430
Benzersiz havalimanı sayısı: 87

Yıldız dağılımı:
  5 yıldız: 45,233 (36.1%)
  4 yıldız: 32,887 (26.2%)
  3 yıldız: 21,156 (16.9%)
  2 yıldız: 15,432 (12.3%)
  1 yıldız: 10,722 (8.5%)

==================================================
YILDIZ DAĞILIMI BELİRLEME
==================================================
5 yıldızlı yorumlar (mevcut: 45233): 100
4 yıldızlı yorumlar (mevcut: 32887): 150
3 yıldızlı yorumlar (mevcut: 21156): 100
2 yıldızlı yorumlar (mevcut: 15432): 75
1 yıldızlı yorumlar (mevcut: 10722): 25
```

### 🔧 Programlı Kullanım

```python
from smart_mix_split import SmartMixSplit

# SmartMixSplit nesnesini oluştur
mixer = SmartMixSplit("input", "output")

# CSV dosyalarını oku ve birleştir
data = mixer.read_csv_files()

# Veriyi analiz et
analysis = mixer.analyze_data()
mixer.print_analysis(analysis)

# Özel yıldız dağılımı ile örnekleme yap
star_distribution = {5: 100, 4: 150, 3: 100, 2: 75, 1: 25}
sample = mixer.create_balanced_sample(star_distribution)

# Sonuçları kaydet
mixer.save_results(sample, "my_custom_sample.csv")
```

### 📊 Örnek Kullanım Scripti

```bash
python example_usage.py
```

Bu script 3 farklı örnekleme stratejisi ile otomatik olarak örnekleme yapar:

1. **Dengeli Dağılım**: Tüm yıldız puanlarından eşit sayıda
2. **Pozitif Odaklı**: Yüksek puanlı yorumlara odaklanır  
3. **Eşit Ağırlık**: Her yıldız puanından eşit miktarda

## ⚙️ Algoritma Detayları

### 🧠 Stratified Sampling Süreci

1. **📥 Veri Girişi**
   - CSV dosyalarını otomatik tespit ve birleştirme
   - Boş yorumları filtreleme ve raporlama
   - Veri doğrulama ve eksik sütun kontrolü

2. **📈 Analiz Aşaması**
   - Toplam veri miktarı hesaplama
   - Yıldız, dil ve havalimanı dağılımı analizi
   - Dosya bazında boş yorum istatistikleri

3. **🎯 Akıllı Örnekleme**
   - Her yıldız puanı için ayrı işlem
   - Dil bazında orantılı dağılım (proportional sampling)
   - Her dil içinde havalimanı bazında orantılı dağılım
   - Eksik kısımlar için rastgele tamamlama
   - Final karıştırma (shuffle) işlemi

4. **💾 Sonuç Üretimi**
   - CSV formatında örneklenen veri
   - Detaylı istatistiklerle summary.txt

### 🔍 Boş Yorum Filtreleme

Program şu durumları boş yorum olarak algılar:
- `NaN` değerler
- Boş string (`""`)
- Sadece whitespace içeren metinler
- `"nan"` string değeri

## 📈 Çıktı Dosyaları

### 1. `sampled_data.csv`
Örneklenen yorumların tam veri seti:
```csv
profile_name,score,comment,language,contribution,date,url
Istanbul Airport,5,"Great experience",en,"150 contributions",2024-01-15,https://...
Ankara Airport,3,"Average service",tr,"45 contributions",2024-01-10,https://...
```

### 2. `summary.txt`
Detaylı istatistiksel özet:
```
ÖRNEKLEME ÖZETİ
==================================================
Toplam örneklenen satır: 450

Yıldız dağılımı:
  5 yıldız: 100 (22.2%)
  4 yıldız: 150 (33.3%)
  3 yıldız: 100 (22.2%)
  2 yıldız: 75 (16.7%)
  1 yıldız: 25 (5.6%)

Dil dağılımı:
  en: 234 (52.0%)
  tr: 126 (28.0%)
  de: 45 (10.0%)
  fr: 27 (6.0%)
  es: 18 (4.0%)

Havalimanı dağılımı:
  Istanbul Airport: 89 (19.8%)
  Frankfurt Airport: 76 (16.9%)
  ...
```

## 🛠️ Gelişmiş Özellikler

### Komut Satırı Argümanları

```bash
# Özel input ve output klasörleri
python smart_mix_split.py --input-dir /data/airports --output-dir /results

# Yardım için
python smart_mix_split.py --help
```

### Programlı API Kullanımı

```python
from smart_mix_split import SmartMixSplit

# Konfigürasyon
mixer = SmartMixSplit(
    input_dir="custom_input",
    output_dir="custom_output"
)

# Veri işleme pipeline
try:
    # 1. Veri okuma
    data = mixer.read_csv_files()
    
    # 2. Analiz
    analysis = mixer.analyze_data()
    
    # 3. Örnekleme
    sample = mixer.create_balanced_sample({
        5: 200,  # 5 yıldızdan 200 adet
        4: 150,  # 4 yıldızdan 150 adet
        3: 100,  # 3 yıldızdan 100 adet
        2: 50,   # 2 yıldızdan 50 adet
        1: 25    # 1 yıldızdan 25 adet
    })
    
    # 4. Kaydetme
    mixer.save_results(sample, "balanced_sample.csv")
    
except Exception as e:
    print(f"Hata: {e}")
```

## 🔧 Hata Yönetimi ve Uyarılar

Program şu durumlarda bilgilendirici mesajlar verir:

### ⚠️ Uyarı Durumları
- **CSV bulunamadı**: Input klasöründe CSV dosyası yok
- **Eksik sütunlar**: Gerekli sütunlardan bazıları eksik
- **Yetersiz veri**: İstenenden az veri mevcut
- **Boş yorumlar**: Filtrelenen boş yorum sayısı

### ❌ Hata Durumları
- **Dosya okuma hatası**: CSV dosyası bozuk veya erişilemez
- **Veri yokluğu**: Hiçbir geçerli veri bulunamadı
- **Parametre hatası**: Geçersiz yıldız dağılımı

## 🎯 Kullanım Senaryoları

### 🔬 Araştırma Projeleri
- Havalimanı hizmeti kalitesi analizi
- Dil bazında memnuniyet karşılaştırması
- Çok dilli sentiment analizi veri seti hazırlama

### 🤖 Makine Öğrenmesi
- Balanced dataset oluşturma
- Cross-lingual model training
- Stratified sampling for ML

### 📊 Veri Analizi
- Büyük veri setlerinden representative sample
- A/B testing için kontrol grubu oluşturma
- Dil ve coğrafya bazında segmentasyon

## 🚨 Önemli Notlar

### ⚡ Performans
- Büyük CSV dosyaları için memory efficient
- Pandas vectorized operations kullanımı
- Progress tracking ile süreç takibi

### 🔒 Veri Güvenliği
- Orijinal veri dosyalarına dokunulmaz
- Sadece output klasöründe yeni dosyalar oluşturulur
- Veri tiplerinin korunması

### 🌍 Çok Dil Desteği
- UTF-8 encoding ile tüm dilleri destekler
- Unicode karakter uyumluluğu
- Dil kodu standardizasyonu

## 📝 Lisans

Bu proje MIT lisansı altında yayınlanmıştır. Ticari ve akademik kullanım için serbesttir.

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📞 İletişim ve Destek

- 🐛 **Bug Report**: Issues sekmesinden bildirin
- 💡 **Feature Request**: Yeni özellik önerileri için issue açın
- 📖 **Dokümantasyon**: README'yi güncel tutmaya yardım edin

## 📚 Teknoloji Stack'i

- **Python 3.7+**: Ana programlama dili
- **Pandas**: Veri manipülasyonu ve analizi
- **NumPy**: Sayısal hesaplamalar ve random sampling
- **CSV**: Veri input/output formatı

---

**Made with ❤️ for data scientists and researchers**

> 💡 **İpucu**: Büyük veri setleri ile çalışırken önce küçük bir sample ile test edin!

