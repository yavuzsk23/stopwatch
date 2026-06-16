from pathlib import Path
from loguru import logger

def pathlib_ussunu_atesle():
    logger.info("Pathlib Dosya Motoru aktif edildi.")

    # 1. Bulunduğumuz klasörü (Current Working Directory) nesne olarak alıyoruz
    su_anki_klasor = Path.cwd()
    logger.info(f"Üs olarak seçilen dizin: {su_anki_klasor}")

    print(f"\n--- 📁 {su_anki_klasor.name.upper()} KLASÖRÜ İÇERİĞİ ---")
    
    # 2. Klasörün içindeki HER ŞEYİ tek hamlede tarıyoruz (iterdir() fonksiyonu)
    for dosya in su_anki_klasor.iterdir():
        # Dosya mı yoksa klasör mü olduğunu tek tıkla anlıyoruz
        durum = "📄 Dosya" if dosya.is_file() else "📁 Klasör"
        
        # dosya.suffix bize .py, .txt gibi uzantıları doğrudan verir kanka
        uzanti = dosya.suffix if dosya.is_file() else "KLASÖR"
        
        print(f"{durum} -> İsim: {dosya.name} | Uzantı: {uzanti}")

    print("\n--- 🛠️ AKILLI DOSYA KONTROLÜ ---")
    # 3. Klasörde "Cyberia_Bot_Yol_Haritasi.txt" adında bir not defteri var mı?
    hedef_dosya = su_anki_klasor / "Cyberia_Bot_Yol_Haritasi.txt" # Sırf eğik çizgi (/) ile yol birleştirme!
    
    if hedef_dosya.exists():
        logger.success(f"Bulundu! Starblast planlarının olduğu not defteri siber üste mevcut: {hedef_dosya.name}")
    else:
        logger.warning(f"Hedef dosya ({hedef_dosya.name}) bu klasörde bulunamadı ağa, sıkıntı yok.")

if __name__ == "__main__":
    pathlib_ussunu_atesle()
