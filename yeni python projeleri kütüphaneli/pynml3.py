import pynvml
import time

def get_gpu_status():
    try:
        pynvml.nvmlInit()
        # 0 numaralı cihaz senin RTX 5060'ın
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        
        # Sıcaklık çekiyoruz
        temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        
        # Bellek (VRAM) bilgisi
        info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        
        print(f"--- Cyberia GPU Raporu ---")
        print(f"GPU Sıcaklık: {temp}°C")
        print(f"VRAM Kullanımı: {info.used / (1024**2):.2f} MB / {info.total / (1024**2):.2f} MB")
        
        pynvml.nvmlShutdown()
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    get_gpu_status()
