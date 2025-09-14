# dataBalancer ⚖️

[![CI/CD Pipeline](https://github.com/mrcaar/dataBalancer/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/mrcaar/dataBalancer/actions)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Issues](https://img.shields.io/github/issues/mrcaar/dataBalancer)](https://github.com/mrcaar/dataBalancer/issues)
[![Stars](https://img.shields.io/github/stars/mrcaar/dataBalancer)](https://github.com/mrcaar/dataBalancer/stargazers)

**Intelligent data sampling and analysis tool for balanced datasets**

Bu profesyonel Python aracı, CSV veri setlerini birleştirerek **stratified sampling** ile dengeli ve homojen veri örnekleri oluşturur. Havalimanı yorumları, müşteri geri bildirimleri ve çok kategorili veri setleri için ideal. Araştırma projeleri, veri analizi ve makine öğrenmesi çalışmaları için optimize edilmiştir.

## ✨ Ana Özellikler

### 🔄 Veri İşleme
- **Çoklu CSV Birleştirme**: Input klasöründeki tüm CSV dosyalarını otomatik olarak birleştirir
- **Akıllı Veri Temizleme**: Boş ve geçersiz kayıtları tespit eder ve detaylı raporlama yapar
- **Veri Doğrulama**: Eksik sütunları kontrol eder ve uyarı verir
- **Format Esnekliği**: Farklı CSV formatlarını destekler

### 📊 Gelişmiş Analiz
- **Kapsamlı İstatistikler**: Kategori, dil ve kaynak dağılımlarını analiz eder
- **Detaylı Raporlama**: Dosya bazında veri kalitesi analizi
- **Görsel İstatistikler**: Yüzdelik dilimlerle birlikte dağılım gösterimi
- **Trend Analizi**: Zaman bazlı veri dağılımı

### 🎯 Stratified Sampling
- **Homojen Dağılım**: Her kategori içinde alt grupların oransal dağılımı korunur
- **Çok Boyutlu Dengeleme**: Dil, kaynak ve zaman bazında dengeli örnekleme
- **Kullanıcı Kontrollü**: İstediğiniz kategori dağılımını belirleyebilirsiniz
- **Akıllı Algoritma**: Eksik kısımları istatistiksel olarak doğru şekilde tamamlar

### 💾 Çıktı ve Raporlama
- **CSV Export**: Örneklenen veriler CSV formatında kaydedilir
- **Özet Raporu**: Detaylı istatistiklerle birlikte summary.txt dosyası
- **Süreç Takibi**: Anlık progress ve debug bilgileri
- **Audit Trail**: Örnekleme sürecinin tam logları

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
python data_balancer.py

# Özel klasörlerle kullanım
python data_balancer.py --input-dir /path/to/csv/files --output-dir /path/to/output
```

## 📁 Proje Yapısı

```
dataBalancer/
├── 📄 data_balancer.py        # Ana dataBalancer sınıfı
├── 📄 example_usage.py        # Örnek kullanım scripti
├── 📄 requirements.txt        # Python bağımlılıkları
├── 📂 input/                  # CSV dosyalarını buraya koyun
│   └── sample_data.csv        # Örnek veri dosyası
├── 📂 output/                 # Sonuçlar burada oluşturulur
│   ├── balanced_data.csv      # Dengelenmiş veriler
│   └── summary.txt            # Detaylı istatistikler
└── 📄 README.md              # Bu dosya
```

## 📋 CSV Veri Formatı

dataBalancer esnek CSV formatını destekler. Temel gereksinimler:

| Sütun | Açıklama | Örnek | Gerekli |
|-------|----------|-------|---------|
| `category_field` | Ana kategori (score, rating, etc.) | 1-5, A-F, positive/negative | ✅ |
| `content_field` | Ana içerik (comment, review, text) | "Great experience" | ✅ |
| `language` | Dil kodu | "en", "tr", "de" | ⚠️ |
| `source` | Kaynak bilgisi | "airport_name", "store_id" | ⚠️ |
| `date` | Tarih | "2024-01-15" | ❌ |
| `metadata` | Ek bilgiler | JSON, string | ❌ |

**Not:** ⚠️ işaretli alanlar dengeleme için önerilir, ❌ işaretli alanlar opsiyoneldir.

### Desteklenen Veri Türleri

1. **Havalimanı Yorumları**: profile_name, score, comment, language
2. **E-ticaret Reviews**: product_id, rating, review, customer_segment  
3. **Sosyal Medya**: platform, sentiment, content, language
4. **Anket Verileri**: question_id, response, demographic, region
5. **Customer Feedback**: department, satisfaction, feedback, channel

## 💻 Kullanım Örnekleri

### 🎮 İnteraktif Kullanım

```bash
python data_balancer.py
```

Program size veri analizi gösterecek ve kategori dağılımını soracak:

```
==================================================
VERİ ANALİZİ
==================================================
Toplam satır sayısı: 125,430
Benzersiz kaynak sayısı: 87
Ana kategori: score (1-5 arası değerler)

Kategori dağılımı:
  5 puan: 45,233 (36.1%)
  4 puan: 32,887 (26.2%)
  3 puan: 21,156 (16.9%)
  2 puan: 15,432 (12.3%)
  1 puan: 10,722 (8.5%)

Dil dağılımı:
  en: 67,234 (53.6%)
  tr: 31,358 (25.0%)
  de: 15,072 (12.0%)
  fr: 8,766 (7.0%)

==================================================
KATEGORİ DAĞILIMI BELİRLEME
==================================================
5 puanlı kayıtlar (mevcut: 45233): 100
4 puanlı kayıtlar (mevcut: 32887): 150
3 puanlı kayıtlar (mevcut: 21156): 100
2 puanlı kayıtlar (mevcut: 15432): 75
1 puanlı kayıtlar (mevcut: 10722): 25
```

### 🔧 Programlı Kullanım

```python
from data_balancer import dataBalancer

# dataBalancer nesnesini oluştur
balancer = dataBalancer("input", "output")

# CSV dosyalarını oku ve birleştir
data = balancer.read_csv_files()

# Veriyi analiz et
analysis = balancer.analyze_data()
balancer.print_analysis(analysis)

# Özel kategori dağılımı ile örnekleme yap
category_distribution = {5: 100, 4: 150, 3: 100, 2: 75, 1: 25}
sample = balancer.create_balanced_sample(category_distribution)

# Sonuçları kaydet
balancer.save_results(sample, "my_balanced_dataset.csv")
```

### 📊 Örnek Kullanım Scripti

```bash
python example_usage.py
```

Bu script 3 farklı dengeleme stratejisi ile otomatik olarak örnekleme yapar:

1. **Eşit Dağılım**: Tüm kategorilerden eşit sayıda
2. **Ağırlıklı Dağılım**: Yüksek kategorilere odaklanır  
3. **Proportional**: Mevcut oranları koruyarak küçültür

### 🎯 Özel Kullanım Senaryoları

#### Havalimanı Yorumları
```python
# Havalimanı verisi için optimize edilmiş kullanım
balancer = dataBalancer("input", "output")
balancer.set_category_column("score")
balancer.set_content_column("comment")
balancer.set_grouping_columns(["language", "profile_name"])
```

#### E-ticaret Reviews
```python
# E-ticaret verisi için
balancer = dataBalancer("input", "output")
balancer.set_category_column("rating")
balancer.set_content_column("review")
balancer.set_grouping_columns(["product_category", "customer_segment"])
```

#### Anket Verileri
```python
# Anket verisi için
balancer = dataBalancer("input", "output")
balancer.set_category_column("satisfaction_level")
balancer.set_content_column("feedback")
balancer.set_grouping_columns(["department", "employee_type"])
```

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

### 🔍 Veri Temizleme

Program şu durumları geçersiz veri olarak algılar:
- `NaN` değerler
- Boş string (`""`)
- Sadece whitespace içeren metinler  
- `"nan"`, `"null"`, `"undefined"` string değerleri
- Kategori sütununda beklenmeyen değerler

## 📈 Çıktı Dosyaları

### 1. `balanced_data.csv`
Dengelenmiş veri setinin tam içeriği:
```csv
category,content,language,source,date,metadata
5,"Great experience",en,"Istanbul Airport",2024-01-15,"{""sentiment"": ""positive""}"
3,"Average service",tr,"Ankara Airport",2024-01-10,"{""sentiment"": ""neutral""}"
1,"Poor experience",de,"Frankfurt Airport",2024-01-08,"{""sentiment"": ""negative""}"
```

### 2. `summary.txt`
Detaylı istatistiksel özet:
```
dataBalancer ÖZETİ
==================================================
Toplam örneklenen satır: 450
Dengeleme başarı oranı: %96.8

Kategori dağılımı:
  5 puan: 100 (22.2%) - Hedef: 100
  4 puan: 150 (33.3%) - Hedef: 150  
  3 puan: 100 (22.2%) - Hedef: 100
  2 puan: 75 (16.7%) - Hedef: 75
  1 puan: 25 (5.6%) - Hedef: 25

Dil dağılımı (dengeli):
  en: 234 (52.0%) - Orijinal: %53.6
  tr: 126 (28.0%) - Orijinal: %25.0
  de: 45 (10.0%) - Orijinal: %12.0
  fr: 27 (6.0%) - Orijinal: %7.0

Kaynak dağılımı (korundu):
  Istanbul Airport: 89 (19.8%)
  Frankfurt Airport: 76 (16.9%)
  ...

İşlem süresi: 2.34 saniye
Bellek kullanımı: 45.2 MB
```

### 3. `process_log.txt` (Opsiyonel)
Detaylı işlem logları:
```
[2024-09-14 10:30:15] dataBalancer v1.0.0 başlatıldı
[2024-09-14 10:30:15] Input klasörü taranıyor: input/
[2024-09-14 10:30:16] 3 CSV dosyası bulundu
[2024-09-14 10:30:16] turkceData.csv: 125,430 satır okundu
[2024-09-14 10:30:17] Veri temizleme: 1,245 geçersiz satır filtrelendi
[2024-09-14 10:30:18] Kategori analizi tamamlandı
[2024-09-14 10:30:19] Stratified sampling başlatıldı
[2024-09-14 10:30:20] Dengeleme tamamlandı: 450 satır
[2024-09-14 10:30:20] Sonuçlar kaydedildi
```

## 🛠️ Gelişmiş Özellikler

### Komut Satırı Argümanları

```bash
# Özel input ve output klasörleri
python data_balancer.py --input-dir /data/reviews --output-dir /results

# Kategori sütunu belirtme
python data_balancer.py --category-column rating --content-column review

# Hızlı dengeleme modu
python data_balancer.py --quick-mode --sample-size 1000

# Verbose logging
python data_balancer.py --verbose --log-file process.log

# Yardım için
python data_balancer.py --help
```

### Programlı API Kullanımı

```python
from data_balancer import dataBalancer

# Gelişmiş konfigürasyon
balancer = dataBalancer(
    input_dir="custom_input",
    output_dir="custom_output",
    category_column="score",
    content_column="comment",
    grouping_columns=["language", "source"]
)

# Veri işleme pipeline
try:
    # 1. Veri okuma
    data = balancer.read_csv_files()
    
    # 2. Analiz
    analysis = balancer.analyze_data()
    
    # 3. Otomatik dengeleme (equal distribution)
    auto_sample = balancer.auto_balance(total_samples=500)
    
    # 4. Özel dengeleme
    custom_sample = balancer.create_balanced_sample({
        5: 200,  # 5 puandan 200 adet
        4: 150,  # 4 puandan 150 adet
        3: 100,  # 3 puandan 100 adet
        2: 50,   # 2 puandan 50 adet
        1: 25    # 1 puandan 25 adet
    })
    
    # 5. Kalite kontrolü
    quality_report = balancer.quality_check(custom_sample)
    
    # 6. Kaydetme
    balancer.save_results(custom_sample, "balanced_dataset.csv")
    
except Exception as e:
    print(f"Hata: {e}")
```

### Batch İşleme

```python
# Çoklu dosya işleme
from data_balancer import BatchBalancer

batch = BatchBalancer()

# Birden fazla klasörü işle
results = batch.process_folders([
    "data/2023/",
    "data/2024/",
    "data/current/"
])

# Sonuçları birleştir
combined_dataset = batch.merge_results(results)
```

## 🔧 Hata Yönetimi ve Uyarılar

Program şu durumlarda bilgilendirici mesajlar verir:

### ⚠️ Uyarı Durumları
- **CSV bulunamadı**: Input klasöründe CSV dosyası yok
- **Eksik sütunlar**: Gerekli sütunlardan bazıları eksik
- **Yetersiz veri**: İstenenden az veri mevcut
- **Dengesiz dağılım**: Bazı kategorilerde çok az veri
- **Kalite sorunları**: Geçersiz veya bozuk kayıtlar

### ❌ Hata Durumları
- **Dosya okuma hatası**: CSV dosyası bozuk veya erişilemez
- **Veri yokluğu**: Hiçbir geçerli veri bulunamadı
- **Parametre hatası**: Geçersiz kategori dağılımı
- **Bellek hatası**: Çok büyük veri seti
- **Format hatası**: Desteklenmeyen CSV formatı

## 🎯 Kullanım Senaryoları

### 🔬 Araştırma Projeleri
- **Akademik Çalışmalar**: Dengeli veri setleri ile bias-free araştırma
- **Sosyal Bilimler**: Anket verilerinin demografik dengelenmesi
- **Dil Araştırmaları**: Çok dilli korpus oluşturma
- **Pazar Araştırması**: Müşteri segmentasyonu ve analizi

### 🤖 Makine Öğrenmesi
- **Balanced Dataset**: Class imbalance problemini çözme
- **Cross-validation**: Stratified split için veri hazırlama
- **Model Training**: Bias'ı önlemek için dengeli eğitim seti
- **A/B Testing**: Kontrol ve test grupları oluşturma
- **Feature Engineering**: Kategori bazlı özellik çıkarma

### 📊 İş Analizi
- **Müşteri Geri Bildirimi**: Review verilerinin dengelenmesi
- **Kalite Kontrol**: Ürün değerlendirmelerinin stratified analizi
- **Risk Analizi**: Finansal verilerin segment bazlı örneklenmesi
- **HR Analytics**: Çalışan anketlerinin departman bazlı dengelenmesi

### 🌐 Veri Bilimi
- **ETL Süreçleri**: Büyük veri setlerinden temsilci örnekler
- **Data Pipeline**: Otomatik veri dengeleme süreçleri
- **Reporting**: Executive dashboard'lar için özetlenmiş veriler
- **Data Quality**: Veri kalitesi metrikleri ve raporlama

## 🚨 Önemli Notlar

### ⚡ Performans
- **Büyük CSV dosyaları**: Memory-efficient chunk processing
- **Pandas optimizasyonu**: Vectorized operations ile hızlı işleme
- **Progress tracking**: Real-time süreç takibi
- **Parallel processing**: Çoklu dosya için paralel okuma
- **Memory management**: Otomatik garbage collection

### 🔒 Veri Güvenliği
- **Non-destructive**: Orijinal veri dosyalarına dokunulmaz
- **Isolated output**: Sadece output klasöründe yeni dosyalar
- **Data integrity**: Veri tiplerinin ve encoding'in korunması
- **Backup support**: Otomatik backup opsiyonu
- **Privacy**: Hassas veri için anonymization desteği

### 🌍 Çok Dil ve Format Desteği
- **UTF-8 encoding**: Tüm dilleri destekler (Türkçe, Arapça, Çince, vb.)
- **Unicode compatibility**: Emoji ve özel karakterler
- **CSV variants**: Farklı delimiter ve quote karakterleri
- **Locale support**: Tarih ve sayı formatları
- **BOM handling**: Excel uyumluluğu

### 🔧 Esneklik ve Genişletilebilirlik
- **Plugin architecture**: Özel sampling algoritmaları
- **Custom validators**: Kendi veri doğrulama kurallarınız
- **Export formats**: CSV, JSON, Excel desteği (gelecek sürümde)
- **API integration**: REST API ve webhook desteği planlanıyor
- **Configuration files**: YAML/JSON config dosyaları

## 📝 Lisans

Bu proje MIT lisansı altında yayınlanmıştır. Ticari ve akademik kullanım için serbesttir.

## 🤝 Katkıda Bulunma

dataBalancer açık kaynak bir projedir ve katkılarınızı memnuniyetle karşılarız!

### 🚀 Nasıl Katkıda Bulunabilirsiniz?

1. **Fork** yapın
2. **Feature branch** oluşturun (`git checkout -b feature/amazing-feature`)
3. **Değişikliklerinizi commit** edin (`git commit -m 'Add amazing feature'`)
4. **Branch'inizi push** edin (`git push origin feature/amazing-feature`)
5. **Pull Request** açın

### 🎯 Katkı Alanları

- **Yeni sampling algoritmaları**
- **Performans optimizasyonları**
- **Yeni veri formatları** (Excel, JSON, Parquet)
- **Visualization** özellikleri
- **Unit tests** ve documentation
- **Bug fixes** ve code improvements

### 🏆 Contributors

Katkıda bulunanlar CHANGELOG.md'de recognition alırlar!

## 📞 İletişim ve Destek

- 🐛 **Bug Report**: [Issues](https://github.com/mrcaar/dataBalancer/issues) sekmesinden bildirin
- 💡 **Feature Request**: Yeni özellik önerileri için [issue açın](https://github.com/mrcaar/dataBalancer/issues/new)
- 📖 **Dokümantasyon**: README'yi güncel tutmaya yardım edin
- 💬 **Discussions**: [GitHub Discussions](https://github.com/mrcaar/dataBalancer/discussions) alanını kullanın
- 📧 **Email**: Gizli konular için direct iletişim

## 📚 Teknoloji Stack'i

- **Python 3.7+**: Ana programlama dili, modern features
- **Pandas**: Veri manipülasyonu ve analizi, high-performance
- **NumPy**: Sayısal hesaplamalar ve random sampling
- **CSV**: Veri input/output formatı, universal support

### 🔮 Gelecek Planları

- **GUI Interface**: PyQt tabanlı desktop uygulaması
- **Web Interface**: Flask/FastAPI ile web arayüzü
- **Cloud Integration**: AWS S3, Google Cloud Storage desteği
- **Database Support**: PostgreSQL, MySQL, MongoDB
- **Real-time Processing**: Streaming data support
- **Advanced Visualizations**: Plotly, Seaborn entegrasyonu

---

**Made with ❤️ for data scientists, researchers, and developers worldwide**

> 💡 **Pro Tip**: Büyük veri setleri ile çalışırken önce küçük bir sample ile test edin ve sonuçları validate edin!

---

### 📈 Project Stats

![Lines of Code](https://img.shields.io/tokei/lines/github/mrcaar/dataBalancer)
![Code Quality](https://img.shields.io/codacy/grade/abcd1234)
![Test Coverage](https://img.shields.io/codecov/c/github/mrcaar/dataBalancer)
![Downloads](https://img.shields.io/pypi/dm/data-balancer)

