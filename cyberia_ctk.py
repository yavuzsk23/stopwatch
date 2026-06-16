import customtkinter as ctk
from PIL import Image
import pyautogui
import os

# Görünüm ayarları: "Dark" mode ve "Blue" tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CyberiaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cyberia v1.0 - Backend Control Panel")
        self.geometry("500x400")

        # Grid düzenini ayarla
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # 1. Başlık ve Logo Alanı
        self.label = ctk.CTkLabel(self, text="CYBERIA SYSTEM", font=ctk.CTkFont(size=25, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        # 2. Gözcü (Robot) Butonu
        self.btn_gozcu = ctk.CTkButton(self, text="Gözcü'yü Başlat (Resim Ara)", 
                                       command=self.gozcu_calistir,
                                       fg_color="green", hover_color="#050")
        self.btn_gozcu.grid(row=1, column=0, padx=20, pady=10)

        # 3. Ayarlar: Benzerlik Oranı (Confidence) Slider
        self.slider_label = ctk.CTkLabel(self, text="Hassasiyet (Confidence): 0.8")
        self.slider_label.grid(row=2, column=0)
        
        self.slider = ctk.CTkSlider(self, from_=0.5, to=1.0, number_of_steps=10, command=self.slider_event)
        self.slider.set(0.8)
        self.slider.grid(row=3, column=0, padx=20, pady=10)

    def slider_event(self, value):
        self.slider_label.configure(text=f"Hassasiyet (Confidence): {round(value, 2)}")

    def gozcu_calistir(self):
        conf_degeri = self.slider.get()
        try:
            konum = pyautogui.locateOnScreen('hedef.png', confidence=conf_degeri)
            if konum:
                merkez = pyautogui.center(konum)
                pyautogui.moveTo(merkez, duration=1)
                self.label.configure(text="HEDEF VURULDU!", text_color="green")
            else:
                self.label.configure(text="HEDEF BULUNAMADI", text_color="red")
        except Exception as e:
            print(f"Hata: {e}")

if __name__ == "__main__":
    app = CyberiaApp()
    app.mainloop()
