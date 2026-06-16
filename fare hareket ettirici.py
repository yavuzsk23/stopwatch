import pyautogui
import time

# Kodun aniden başlamaması için 3 saniye süre veriyoruz.
# Bu sırada ekranı hazırlayabilirsin.
print("Sistem hazırlanıyor, lütfen bekleyin...")
time.sleep(3)

# 1. Ekran Çözünürlüğünü Öğrenme
genislik, yukseklik = pyautogui.size()
print(f"Ekran Çözünürlüğünüz: {genislik}x{yukseklik}")

# 2. Fareyi Belirli Bir Noktaya IŞINLAMA (Mutlak Konum)
# Fareyi ekranın tam ortasına anında götürür
print("Fare ekranın ortasına ışınlanıyor...")
pyautogui.moveTo(genislik / 2, yukseklik / 2)
time.sleep(2)

# 3. Fareyi AKICI ve YAVAŞÇA Hareket Ettirme (Süre Belirterek)
# X: 200, Y: 200 koordinatına 2 saniye içinde yavaşça gider
print("Fare sol üste doğru yavaşça hareket ediyor...")
pyautogui.moveTo(200, 200, duration=2.0)
time.sleep(1)

# 4. Fareyi Mevcut Konumuna Göre Göreceli (Göreceli) Hareket Ettirme
# Fare o an neredeyse, oradan 300 piksel sağa ve 100 piksel aşağı kayar
print("Fare mevcut konumundan biraz sağa ve aşağı kayıyor...")
pyautogui.move(300, 100, duration=1.5)

print("İşlem tamamlandı!")
