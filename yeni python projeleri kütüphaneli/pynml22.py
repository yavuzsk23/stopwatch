import pynvml

def get_gpu_status():
    pynvml.nvmlInit()
    # 0 numaralı ekran kartını (RTX 5060) seçiyoruz
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    
    # Sıcaklık
    temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
    
    # Bellek Bilgisi
    info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    
    print(f"GPU Sıcaklık: {temp}°C")
    print(f"VRAM Kullanımı: {info.used / (1024**2):.2f} MB / {info.total / (1024**2):.2f} MB")
    
    pynvml.nvmlShutdown()

get_gpu_status()
