import pyautogui
import time

# Fren sistemini hatırlatıyoruz (0,0 noktası)
pyautogui.FAILSAFE = True

print("Sistemi başlatıyorum... Lütfen fareyi serbest bırak!")
time.sleep(3)

# 1. ADIM: Ekranın ortasını bul ve oraya tıkla (Not defterini seçmek için)
genislik, yukseklik = pyautogui.size()
print(f"Ekranın ortasına gidiliyor: {genislik/2}, {yukseklik/2}")
pyautogui.click(genislik / 2, yukseklik / 2) 

# 2. ADIM: Küçük bir bekleme (Bilgisayarın tıklamayı algılaması için)
time.sleep(1)

# 3. ADIM: Klavye şov başlasın
pyautogui.write("Selam kanka! Su an hem fare hem klavye bende.", interval=0.1)
pyautogui.press("enter")
pyautogui.write("Az once buraya tikladim ve yazmaya basladim.", interval=0.1)

# 4. ADIM: Fareyi daire çizdirerek kutlama yapalım (Ekstra artistik hareket)
print("Kutlama dansı başlıyor...")
pyautogui.moveTo(400, 400, duration=0.5)
pyautogui.moveTo(600, 400, duration=0.5)
pyautogui.moveTo(600, 600, duration=0.5)
pyautogui.moveTo(400, 600, duration=0.5)

pyautogui.alert("Operasyon başarıyla tamamlandı, hızlı yazılımcı!")
