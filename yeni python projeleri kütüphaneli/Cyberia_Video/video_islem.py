from moviepy import VideoFileClip
from loguru import logger

video_adi = "video.mp4" 

try:
    logger.info(f"{video_adi} yükleniyor...")
    clip = VideoFileClip(video_adi)
    
    logger.info("Video kesiliyor...")
    # Yeni MoviePy sürümünde fonksiyon adı subclipped oldu kanka!
    sub_clip = clip.subclipped(0, 5) # İlk 5 saniye
    
    cikti_adi = "cyberia_sonuc.mp4"
    
    logger.info(f"Render başlıyor -> {cikti_adi}")
    sub_clip.write_videofile(cikti_adi)
    
    logger.success("İşlem bitti kanka, klasöre bak!")

except Exception as e:
    logger.error(f"Hata çıktı: {e}")
