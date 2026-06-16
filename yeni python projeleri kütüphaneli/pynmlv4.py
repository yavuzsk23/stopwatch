import pynvml
import os
from ctypes import CDLL

def get_gpu_status():
    try:
        # Hatanın çözümü: DLL dosyasını elle yüklüyoruz
        try:
            # Önce System32'dekini dene (Laptoplarda genelde buradadır)
            CDLL("C:\\Windows\\System32\\nvml.dll")
        except:
            # Olmazsa NVIDIA'nın standart klasörünü dene
            CDLL("C:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvml.dll")

        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        
        # Ekran kartı adını alalım (RTX 5060 mı görelim)
        name = pynvml.nvmlDeviceGetName(handle)
        # Sıcaklık
        temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        # Bellek
        info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        
        print(f"--- CYBERIA GPU MONITOR ---")
        print(f"Kart Modeli: {name}")
        print(f"Sıcaklık: {temp}°C")
        print(f"VRAM: {info.used / (1024**2):.2f} MB / {info.total / (1024**2):.2f} MB")
        
        pynvml.nvmlShutdown()
        
    except Exception as e:
        print(f"Hala hata var kanka: {e}")

if __name__ == "__main__":
    get_gpu_status()
