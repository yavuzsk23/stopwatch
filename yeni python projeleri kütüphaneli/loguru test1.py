from loguru import logger
import sys

# 1. Logları bir dosyaya kaydetmek için ayar yapalım
# 'rotation' parametresi dosya 10 MB olunca yenisini açar, 'retention' ise eski logları 5 gün saklar.
logger.add("cyberia_logs.log", rotation="10 MB", retention="5 days", compression="zip")

def sistem_baslat():
    logger.info("Sistem başlatılıyor... LGA 1700 soket kontrol edildi.") # Bilgi mesajı
    
    try:
        # Örnek bir işlem: RAM hızı kontrolü simülasyonu
        ram_hizi = 3200 
        logger.debug(f"Tespit edilen RAM hızı: {ram_hizi} MHz") # Detaylı hata ayıklama
        
        if ram_hizi < 3200:
            logger.warning("RAM hızı beklenenden düşük!") # Uyarı
            
    except Exception as e:
        logger.error(f"Beklenmedik bir hata oluştu: {e}") # Hata mesajı

if __name__ == "__main__":
    logger.success("Cyberia Log Sistemi Aktif!") # Başarı mesajı
    sistem_baslat()
