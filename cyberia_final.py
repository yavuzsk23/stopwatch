import sys
import pyautogui
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

def hedefi_vur():
    try:
        # Az önceki gibi resmi ara
        konum = pyautogui.locateOnScreen('hedef.png', confidence=0.7)
        if konum:
            merkez = pyautogui.center(konum)
            pyautogui.moveTo(merkez, duration=1)
            pyautogui.click()
            print("Hedef vuruldu!")
        else:
            print("Ekrandan kaçmış kanka!")
    except Exception as e:
        print(f"Hata: {e}")

app = QApplication(sys.argv)
pencere = QWidget()
pencere.setWindowTitle("Cyberia v1.0")
pencere.resize(300, 150)

duzen = QVBoxLayout()
etiket = QLabel("Cyberia Kontrol Ünitesi")
btn_bul = QPushButton("Gözcü'yü Çalıştır ve Tıkla")

btn_bul.clicked.connect(hedefi_vur)

duzen.addWidget(etiket)
duzen.addWidget(btn_bul)
pencere.setLayout(duzen)

pencere.show()
sys.exit(app.exec())
