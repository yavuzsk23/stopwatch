import pyautogui
import time

# GÜVENLİK FRENİNİ KAPATIK (Artık sol üste gitsen de hata vermez)
pyautogui.FAILSAFE = False

print("Sistem hazırlanıyor, lütfen bekleyin...")
time.sleep(3)

genislik, yukseklik = pyautogui.size()
print(f"Ekran Çözünürlüğünüz: {genislik}x{yukseklik}")

print("Fare ekranın ortasına ışınlanıyor...")
pyautogui.moveTo(genislik / 2, yukseklik / 2)
time.sleep(2)

print("Fare sol üste doğru yavaşça hareket ediyor...")
# (200, 200) noktasına giderken artık hata tetiklenmeyecek
pyautogui.moveTo(200, 200, duration=2.0)
time.sleep(1)

print("Fare mevcut konumundan biraz sağa ve aşağı kayıyor...")
pyautogui.move(300, 100, duration=1.5)

print("İşlem tamamlandı!")
