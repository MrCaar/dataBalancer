# Contributing to Smart Mix Split

Katkılarınızı memnuniyetle karşılıyoruz! Bu proje açık kaynak topluluğu için geliştirilmektedir.

## Katkıda Bulunma Sürecі

### 1. Repository'yi Fork Edin

GitHub'da projeyi fork edin ve local makinenize clone yapın:

```bash
git clone https://github.com/YOUR_USERNAME/smartMixSplit.git
cd smartMixSplit
```

### 2. Development Environment Kurun

```bash
# Sanal ortam oluşturun
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Bağımlılıkları yükleyin
pip install -r requirements.txt
```

### 3. Branch Oluşturun

```bash
git checkout -b feature/amazing-feature
# veya
git checkout -b bugfix/fix-issue-123
```

### 4. Kod Yazın

- **Code Style**: PEP 8 standartlarına uyun
- **Docstrings**: Fonksiyonlarınızı dokümante edin
- **Comments**: Karmaşık algoritmaları açıklayın
- **Type Hints**: Mümkün olduğunca type hint kullanın

### 5. Test Edin

```bash
# Örnek veri ile test edin
python example_usage.py

# Kendi testlerinizi yazın
python -m pytest tests/  # (eğer test suite eklerseniz)
```

### 6. Commit Yapın

```bash
git add .
git commit -m "feat: add amazing new feature"

# Commit message formatı:
# feat: yeni özellik
# fix: bug düzeltmesi
# docs: dokümantasyon güncellemesi
# style: kod formatı değişiklikleri
# refactor: kod refactor
# test: test ekleme/düzeltme
```

### 7. Pull Request Açın

1. GitHub'da fork'unuza gidin
2. "New Pull Request" butonuna tıklayın
3. Değişikliklerinizi detaylı açıklayın
4. İlgili issue'ları mention edin (#123)

## Katkı Alanları

### 🐛 Bug Reports

Issue açarken şunları belirtin:
- **OS ve Python versiyonu**
- **Hata mesajı** (tam stack trace)
- **Tekrar üretme adımları**
- **Beklenen davranış**
- **Gerçek davranış**

### 💡 Feature Requests

Yeni özellik önerirken:
- **Use case** açıklayın
- **Mevcut alternatifler** varsa belirtin
- **Mockup/örnek** verin
- **Breaking change** olup olmadığını belirtin

### 📖 Documentation

- README güncellemeleri
- Code comment'ları
- API dokümantasyonu
- Tutorial/example'lar

### 🔧 Code Contributions

#### Öncelikli Alanlar

1. **Performance optimizations**
   - Large CSV handling
   - Memory usage improvements
   - Faster sampling algorithms

2. **New features**
   - Additional file formats (Excel, JSON)
   - More sampling strategies
   - Data visualization
   - GUI interface

3. **Testing**
   - Unit tests
   - Integration tests
   - Performance benchmarks

4. **Code quality**
   - Error handling improvements
   - Code refactoring
   - Type annotations

## Coding Standards

### Python Style Guide

```python
# ✅ Good
def create_balanced_sample(self, star_distribution: Dict[int, int]) -> pd.DataFrame:
    """
    Belirtilen yıldız dağılımına göre örnekleme yapar.
    
    Args:
        star_distribution: Yıldız dağılımı {yıldız: sayı}
    
    Returns:
        Örneklenmiş DataFrame
    """
    if not star_distribution:
        raise ValueError("Star distribution cannot be empty")
    
    # Implementation...

# ❌ Avoid
def create_sample(self, dist):
    # No docstring, no type hints
    if not dist:
        return None  # Should raise exception
```

### Error Handling

```python
# ✅ Good - Specific exceptions with clear messages
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    raise FileNotFoundError(f"CSV file not found: {file_path}")
except pd.errors.EmptyDataError:
    raise ValueError(f"CSV file is empty: {file_path}")

# ❌ Avoid - Generic exceptions
try:
    df = pd.read_csv(file_path)
except:
    print("Error occurred")
```

### Logging

```python
import logging

# ✅ Good
logger = logging.getLogger(__name__)
logger.info(f"Processing {len(files)} CSV files")
logger.warning(f"Found {empty_count} empty comments")

# ❌ Avoid
print("Processing files...")  # Use for user interaction only
```

## Testing Guidelines

### Test Structure

```python
import pytest
import pandas as pd
from smart_mix_split import SmartMixSplit

class TestSmartMixSplit:
    def setup_method(self):
        self.mixer = SmartMixSplit("test_input", "test_output")
    
    def test_read_csv_files_success(self):
        # Test successful CSV reading
        pass
    
    def test_read_csv_files_empty_directory(self):
        # Test empty directory handling
        with pytest.raises(FileNotFoundError):
            self.mixer.read_csv_files()
    
    def test_create_balanced_sample_valid_input(self):
        # Test valid sampling
        pass
```

### Test Data

- Küçük, representative test datasets kullanın
- Edge case'leri test edin (empty files, single row, etc.)
- Different languages ve airports içeren data

## Documentation Guidelines

### Code Comments

```python
# ✅ Good - Explains WHY, not WHAT
# Use stratified sampling to maintain language proportions
# across different star ratings to avoid bias
selected_indices = self._stratified_sample(data, target_count)

# ❌ Avoid - Explains obvious
# Loop through star ratings
for star in star_ratings:
```

### README Updates

- Yeni feature'lar için usage examples ekleyin
- Breaking changes için migration guide yazın
- Performance improvements için benchmarks ekleyin

## Release Process

### Version Numbering

- **Major (X.0.0)**: Breaking changes
- **Minor (0.X.0)**: New features, backwards compatible
- **Patch (0.0.X)**: Bug fixes

### Changelog

Her release için CHANGELOG.md güncelleyin:

```markdown
## [1.2.0] - 2024-01-15

### Added
- Excel file support
- Progress bar for large datasets
- Configuration file support

### Changed  
- Improved memory usage for large CSV files
- Better error messages

### Fixed
- Empty comment filtering bug
- Unicode handling in file names
```

## Community Guidelines

### 🤝 Code of Conduct

- Saygılı ve yapıcı iletişim
- Farklı görüşlere açıklık
- Yeni başlayanları destekleme
- Teknik tartışmalarda odaklanma

### 💬 Communication

- **Issues**: Bug reports ve feature requests
- **Discussions**: Genel sorular ve tartışmalar
- **Pull Requests**: Code review ve feedback

### 🏆 Recognition

Katkıda bulunanlar README'de contributors listesinde belirtilir ve release notes'ta teşekkür edilir.

---

**Teşekkürler!** 🎉

Her türlü katkınız projeyi daha da geliştirir. Küçük düzeltmelerden büyük feature'lara kadar her katkı değerlidir!
