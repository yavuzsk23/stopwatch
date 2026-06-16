import pyautogui
import os

# Dosya yolunu garantiye alalım
mevcut_klasor = os.getcwd()
print(f"Şu an bu klasördeyim: {mevcut_klasor}")

try:
    # Ekranın fotoğrafını çekip kaydetmeyi deneyelim (Yetki testi)
    pyautogui.screenshot("test_ekran.png")
    print("Ekran görüntüsü başarıyla alındı! Kütüphane çalışıyor.")
    
    # Şimdi resim aramayı dene (Hata çıkarsa burası yakalayacak)
    konum = pyautogui.locateOnScreen('hedef.png', confidence=0.7)
    
    if konum:
        print(f"Hedef bulundu: {konum}")
    else:
        print("Hata: 'hedef.png' ekranda görünmüyor veya dosya bu klasörde değil.")

except Exception as e:
    print(f"Sistemsel bir hata oluştu: {e}")
