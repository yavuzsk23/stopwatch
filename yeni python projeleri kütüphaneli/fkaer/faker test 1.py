from faker import Faker
from loguru import logger
import json

class SiberVeriUretici:
    def __init__(self):
        # Türkçe veri üretmek için 'tr_TR' kullanıyoruz kanka.
        self.sahte_yonetici = Faker('tr_TR')
        logger.info("Türkçe Veri Üretici Aktif Edildi.")

    def sahte_kullanici_olustur(self, miktar=1):
        """İstenilen miktarda sahte kullanıcı verisi üretir."""
        logger.debug(f"{miktar} adet sahte kullanıcı üretiliyor...")
        kullanicilar = []
        
        for _ in range(miktar):
            # C# 'Object' yapısına benzer bir sözlük (dictionary)
            kullanici = {
                "AdSoyad": self.sahte_yonetici.name(),
                "Eposta": self.sahte_yonetici.email(),
                "Adres": self.sahte_yonetici.address(),
                "SiberKod": self.sahte_yonetici.sha256(), # Proje için havalı bir kod
                "Sirket": self.sahte_yonetici.company(),
                "KayitTarihi": self.sahte_yonetici.date_this_century().strftime("%Y-%m-%d")
            }
            kullanicilar.append(kullanici)
            
        return kullanicilar

    def veriyi_kaydet(self, veri, dosya_adi="sahte_cyberia_verileri.json"):
        """Üretilen verileri bir JSON dosyasına kaydeder."""
        try:
            logger.info(f"Veriler {dosya_adi} dosyasına kaydediliyor...")
            with open(dosya_adi, 'w', encoding='utf-8') as f:
                json.dump(veri, f, ensure_ascii=False, indent=4)
            logger.success(f"Kayit Başarılı! {len(veri)} kullanıcı kaydedildi.")
        except Exception as e:
            logger.error(f"Dosya kaydedilirken hata oluştu: {e}")

if __name__ == "__main__":
    # 1. Üretici sınıfı başlat
    uretici = SiberVeriUretici()
    
    # 2. 10 tane sahte kullanıcı üret
    test_verileri = uretici.sahte_kullanici_olustur(10)
    
    # 3. Verileri dosyaya kaydet
    uretici.veriyi_kaydet(test_verileri)
