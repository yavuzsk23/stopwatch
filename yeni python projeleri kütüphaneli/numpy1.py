import numpy as np
import time

def cyberia_numpy_test():
    print("🔢 Cyberia Sayısal Analiz Motoru Başlatılıyor...")
    
    # 1. Devasa bir veri seti oluşturuyoruz (1 Milyon rastgele sayı)
    # Senin sistem bu işlemi saniyeler içinde yapacak
    baslangic = time.time()
    veriler = np.random.randint(1, 1001, size=1000000) 
    
    # 2. Temel İstatistiksel Analiz
    ortalama = np.mean(veriler)
    en_yuksek = np.max(veriler)
    standart_sapma = np.std(veriler)
    
    # 3. Cyberia Filtreleme (Sadece 990'dan büyük sayıları bulalım)
    # Bu işlemi normal Python listesiyle yapsan bilgisayar kasar, NumPy'da ise şov yapar!
    ozel_sayilar = veriler[veriler > 990]
    
    bitis = time.time()
    
    print("\n📊 --- ANALİZ RAPORU ---")
    print(f"✅ 1 Milyon sayı {bitis - baslangic:.4f} saniyede işlendi.")
    print(f"📈 Ortalama Değer: {ortalama}")
    print(f"🔥 En Yüksek Değer: {en_yuksek}")
    print(f"🎯 Standart Sapma: {standart_sapma:.2f}")
    print(f"🛡️ 990'dan Büyük Sayı Adedi: {len(ozel_sayilar)}")
    print("-" * 25)

# Motoru ateşle!
cyberia_numpy_test()
