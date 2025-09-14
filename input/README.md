# Input Klasörü

CSV dosyalarınızı bu klasöre koyun.

## CSV Formatı

Dosyalarınız şu sütunları içermelidir:

| Sütun | Açıklama | Örnek |
|-------|----------|-------|
| `profile_name` | Havalimanı adı | "Istanbul Airport" |
| `score` | Yıldız puanı (1-5) | 4 |
| `comment` | Yorum metni | "Great service" |
| `language` | Dil kodu | "en", "tr", "de" |
| `contribution` | Katkı bilgisi | "100 contributions" |
| `date` | Tarih | "2024-01-15" |
| `url` | Kaynak URL | "https://..." |

## Kullanım

```bash
# CSV dosyalarınızı buraya kopyalayın
cp /path/to/your/*.csv input/

# Programı çalıştırın
python smart_mix_split.py
```

**Not:** Bu klasördeki CSV dosyaları `.gitignore` ile Git'den hariç tutulmuştur (güvenlik için).
