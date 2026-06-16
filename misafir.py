import pyautogui
import time

print("5 saniye boyunca fareyi takip edeceğim...")
time.sleep(2)

try:
    for i in range(5):
        # Fare neredeyse onun koordinatlarını al
        x, y = pyautogui.position()
        print(f"Şu an buradasın: X={x}, Y={y}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nDurdu.")
