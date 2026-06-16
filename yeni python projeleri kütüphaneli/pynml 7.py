import pynvml

pynvml.nvmlInit()
handle = pynvml.nvmlDeviceGetHandleByIndex(0) # İlk GPU'yu seçer
info = pynvml.nvmlDeviceGetMemoryInfo(handle)

print(f"Toplam VRAM: {info.total / 1024**2} MB")
print(f"Kullanılan VRAM: {info.used / 1024**2} MB")
print(f"Boş VRAM: {info.free / 1024**2} MB")
