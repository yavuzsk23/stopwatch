import customtkinter as ctk
import psutil
import subprocess

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green") # Siber tema için yeşil

class CyberiaFullMonitor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CYBERIA ULTIMATE MONITOR")
        self.geometry("450x400")

        # Başlık
        self.label_title = ctk.CTkLabel(self, text="CYBERIA SYSTEM STATUS", font=("Orbitron", 22, "bold"), text_color="#00FF00")
        self.label_title.pack(pady=15)

        # CPU & RAM Bölümü
        self.cpu_label = ctk.CTkLabel(self, text="CPU: %0", font=("Consolas", 16))
        self.cpu_label.pack(pady=5)
        
        self.ram_label = ctk.CTkLabel(self, text="RAM: %0", font=("Consolas", 16))
        self.ram_label.pack(pady=5)

        # GPU Bölümü (Senin 5060 için)
        self.gpu_temp_label = ctk.CTkLabel(self, text="GPU Temp: 0°C", font=("Consolas", 16), text_color="#FF8C00")
        self.gpu_temp_label.pack(pady=5)
        
        self.vram_label = ctk.CTkLabel(self, text="VRAM: 0 MB", font=("Consolas", 16))
        self.vram_label.pack(pady=5)

        self.update_all()

    def get_gpu_data(self):
        try:
            command = "nvidia-smi --query-gpu=temperature.gpu,memory.used --format=csv,noheader,nounits"
            result = subprocess.check_output(command, shell=True).decode('utf-8').strip()
            temp, vram = result.split(', ')
            return temp, vram
        except:
            return "N/A", "N/A"

    def update_all(self):
        # Sistem Verileri
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        g_temp, g_vram = self.get_gpu_data()

        # Arayüzü Güncelle
        self.cpu_label.configure(text=f"CPU Kullanımı: %{cpu}")
        self.ram_label.configure(text=f"RAM Kullanımı: %{ram}")
        self.gpu_temp_label.configure(text=f"GPU Sıcaklık: {g_temp}°C")
        self.vram_label.configure(text=f"VRAM Kullanımı: {g_vram} MB")

        # 1 saniye sonra tekrarla
        self.after(1000, self.update_all)

if __name__ == "__main__":
    app = CyberiaFullMonitor()
    app.mainloop()
