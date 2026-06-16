import nvidia_smi

def get_gpu_status():
    nvidia_smi.nvmlInit()
    # 0 numaralı ekran kartını (RTX 5060) seçiyoruz
    handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0)
    
    # Sıcaklık
    temp = nvidia_smi.nvmlDeviceGetTemperature(handle, nvidia_smi.NVML_TEMPERATURE_GPU)
    # Bellek Bilgisi
    info = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
    # Fan Hızı
    try:
        fan_speed = nvidia_smi.nvmlDeviceGetFanSpeed(handle)
    except:
        fan_speed = "N/A" # Bazı laptoplarda fan hızı kilitli olabilir

    print(f"GPU Sıcaklık: {temp}°C")
    print(f"VRAM Kullanımı: {info.used / (1024**2):.2f} MB / {info.total / (1024**2):.2f} MB")
    print(f"Fan Hızı: %{fan_speed}")
    
    nvidia_smi.nvmlShutdown()

get_gpu_status()
