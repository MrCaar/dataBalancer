# Changelog

Bu dosya Smart Mix Split projesindeki tüm önemli değişiklikleri takip eder.

Format [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standardına dayanır ve [Semantic Versioning](https://semver.org/spec/v2.0.0.html) kullanır.

## [Unreleased]

### Planned Features
- GUI interface with PyQt/Tkinter
- Excel file format support
- Advanced visualization with matplotlib
- Configuration file support (YAML/JSON)
- Multi-threaded processing for large datasets
- Docker container support

## [1.0.0] - 2024-09-14

### Added
- ✨ **İlk stable release**
- 📊 **SmartMixSplit ana sınıfı** - CSV dosyalarını birleştirme ve örnekleme
- 🔍 **Gelişmiş veri analizi** - Yıldız, dil ve havalimanı dağılımı
- 🎯 **Stratified sampling algoritması** - Homojen dil ve havalimanı dağılımı
- 🧹 **Akıllı veri temizleme** - Boş yorumları tespit etme ve filtreleme
- 📈 **Detaylı raporlama** - Dosya bazında ve genel istatistikler
- 💾 **CSV export** - Örneklenen veri ve özet dosyası
- 🖥️ **İnteraktif CLI** - Kullanıcı dostu komut satırı arayüzü
- 🔧 **Programlı API** - Python kodundan direkt kullanım
- 📚 **Kapsamlı dokümantasyon** - README, examples ve code comments
- 🎮 **Örnek kullanım scripti** - 3 farklı örnekleme stratejisi

### Technical Features
- **Command line arguments** - `--input-dir` ve `--output-dir` parametreleri
- **Error handling** - Kapsamlı hata yönetimi ve kullanıcı bilgilendirmesi
- **Memory efficient** - Büyük CSV dosyaları için optimize edilmiş
- **Unicode support** - Tüm diller için tam UTF-8 desteği
- **Pandas integration** - Güçlü veri manipülasyonu
- **NumPy random sampling** - İstatistiksel olarak doğru örnekleme

### File Structure
```
smartMixSplit/
├── smart_mix_split.py      # Ana program
├── example_usage.py        # Örnek kullanım
├── requirements.txt        # Python bağımlılıkları
├── README.md              # Kapsamlı dokümantasyon
├── input/                 # CSV input klasörü
├── output/                # Sonuç dosyaları
└── __pycache__/          # Python cache
```

### Dependencies
- **pandas >= 1.3.0** - Veri manipülasyonu ve CSV I/O
- **numpy >= 1.20.0** - Sayısal hesaplamalar ve random sampling

### Performance
- ⚡ **Fast CSV reading** - Parallel file processing
- 🧠 **Memory efficient** - Chunk-based processing for large files
- 📊 **Optimized sampling** - Vectorized operations with pandas/numpy

### Supported Platforms
- 🐧 **Linux** - Fully tested
- 🍎 **macOS** - Compatible
- 🪟 **Windows** - Compatible

### Documentation
- 📖 **Comprehensive README** - Installation, usage, examples
- 💻 **Code examples** - Both CLI and programmatic usage
- 🔧 **API documentation** - Detailed class and method docs
- 📊 **Algorithm explanation** - How stratified sampling works

---

## Semantic Versioning Schema

Bu projede [Semantic Versioning](https://semver.org/) kullanılır:

- **MAJOR version** (X.0.0): Breaking changes (API değişiklikleri)
- **MINOR version** (0.X.0): Yeni özellikler, geriye uyumlu
- **PATCH version** (0.0.X): Bug fixes, geriye uyumlu

### Version Planning

#### 🎯 v1.1.0 - Enhancement Release (Planned)
- **Excel file support** (.xlsx, .xls)
- **Progress bars** for large datasets
- **Configuration files** (YAML/JSON)
- **Performance optimizations**
- **Extended CSV format support**

#### 🚀 v1.2.0 - Visualization Release (Planned)
- **Data visualization** with matplotlib/plotly
- **Interactive charts** for analysis results
- **Export to different formats** (JSON, XML)
- **Advanced filtering options**

#### 🎨 v2.0.0 - Major Release (Future)
- **GUI interface** (PyQt/Tkinter)
- **Web interface** (Flask/FastAPI)
- **Database support** (SQLite, PostgreSQL)
- **API breaking changes** for better architecture

---

## Contributors

Bu projeye katkıda bulunanlar:

- **@mrcaar** - İlk geliştirici ve maintainer

### Contribution Stats
- 📝 **Total commits**: 1
- 🔧 **Lines of code**: ~500
- 📊 **Test coverage**: TBD
- 🐛 **Issues resolved**: 0

---

## Release Notes Format

Her release için şu kategoriler kullanılır:

### Added ✨
Yeni özellikler ve functionality

### Changed 🔄  
Mevcut functionality'de değişiklikler

### Deprecated ⚠️
Yakında kaldırılacak özellikler

### Removed 🗑️
Kaldırılan özellikler

### Fixed 🐛
Bug düzeltmeleri

### Security 🔒
Güvenlik ile ilgili düzeltmeler

---

*Bu changelog [Keep a Changelog](https://keepachangelog.com/) formatını takip eder.*
