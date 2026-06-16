import polars as pl
from loguru import logger

def polars_motorunu_atesle():
    logger.info("Polars motoru Rust altyapısıyla başlatılıyor...")

    # 1. Veri Seti Oluşturma (Faker'dan gelen veriler gibi düşün kanka)
    # Polars veri yapısına 'DataFrame' denir.
    veri = {
        "Ajan_Adi": ["Yavuz", "Mete", "Hakan", "Asena", "Oğuz"],
        "Departman": ["Siber Güvenlik", "Backend", "Siber Güvenlik", "Frontend", "Backend"],
        "Kod_Hizi_Saniye": [120, 85, 150, 95, 110],
        "Almanca_Seviyesi": ["B1", "A2", "B2", "A1", "B1"]
    }
    
    # Veriyi Polars DataFrame'ine çeviriyoruz
    df = pl.DataFrame(veri)
    logger.success("Veri seti Polars DataFrame formatına başarıyla yüklendi!")
    
    # 2. Hızlıca Veriye Göz Atma
    print("\n--- 📊 CYBERIA AKILLI VERİ TABLOSU ---")
    print(df)
    
    # 3. SİBER FİLTRELEME (Sadece Siber Güvenlik departmanındakileri bulalım)
    logger.info("Filtreleme işlemi başlatılıyor: Departman == Siber Güvenlik")
    siber_ekip = df.filter(pl.col("Departman") == "Siber Güvenlik")
    
    print("\n--- 🛡️ SİBER GÜVENLİK EKİBİ ---")
    print(siber_ekip)
    
    # 4. HIZLI ANALİZ (Ortalama Kod Yazma Hızını Bulma)
    # Polars bunu işlemcinin tüm çekirdeklerini kullanarak şimşek gibi yapar
    ortalama_hiz = df.select(pl.col("Kod_Hizi_Saniye").mean()).item()
    logger.success(f"Analiz Tamamlandı! Ekibin Ortalama Kod Hızı: {ortalama_hiz:.2f} saniye.")

if __name__ == "__main__":
    polars_motorunu_atesle()
