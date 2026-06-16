import customtkinter as ctk
import psutil

# Pencere ayarları
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CyberiaMonitor(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CYBERIA SYSTEM MONITOR v1.0")
        self.geometry("400x300")

        # Başlık
        self.label_title = ctk.CTkLabel(self, text="SYSTEM STATUS", font=("Orbitron", 20, "bold"), text_color="#00ff00")
        self.label_title.pack(pady=20)

        # CPU Yüzdesi Göstergesi
        self.cpu_label = ctk.CTkLabel(self, text="CPU Usage: %0", font=("Consolas", 16))
        self.cpu_label.pack(pady=10)

        # RAM Yüzdesi Göstergesi
        self.ram_label = ctk.CTkLabel(self, text="RAM Usage: %0", font=("Consolas", 16))
        self.ram_label.pack(pady=10)

        # Verileri güncelleme fonksiyonunu başlat
        self.update_stats()

    def update_stats(self):
        # Verileri çek
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent

        # Etiketleri güncelle
        self.cpu_label.configure(text=f"CPU Usage: %{cpu_usage}")
        self.ram_label.configure(text=f"RAM Usage: %{ram_usage}")

        # Renk değiştirme (Eğer %80'i geçerse kırmızı yap)
        if ram_usage > 80:
            self.ram_label.configure(text_color="red")
        else:
            self.ram_label.configure(text_color="white")

        # 1 saniye sonra tekrar çalıştır (canlı takip)
        self.after(1000, self.update_stats)

if __name__ == "__main__":
    app = CyberiaMonitor()
    app.mainloop()
