import psutil

# İşlemci çekirdek sayısı
print(f"Mantıksal Çekirdek Sayısı: {psutil.cpu_count()}")

# Anlık CPU kullanımı (her thread için ayrı ayrı)
print(f"Thread Kullanımları: {psutil.cpu_percent(interval=1, percpu=True)}")

# RAM Durumu
ram = psutil.virtual_memory()
print(f"Toplam RAM: {ram.total / (1024**3):.2f} GB")
print(f"Kullanılan RAM: {ram.used / (1024**3):.2f} GB")
