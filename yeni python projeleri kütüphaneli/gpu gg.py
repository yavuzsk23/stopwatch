import torch
import time

# GPU Kontrolü
if not torch.cuda.is_available():
    print("HATA: GPU bulunamadı!")
    exit()

device = torch.device("cuda")

# 100 MB hesaplaması:
# float32 = 4 byte. 100 MB = 100 * 1024 * 1024 byte.
# 100 * 1024 * 1024 / 4 = 26,214,400 adet sayı tutmamız lazım.
size = 100 * 1024 * 1024 // 4 

try:
    print("GPU'ya 100 MB veri yükleniyor...")
    
    # Tek boyutlu bir dizi (tensor) oluşturup GPU'ya atıyoruz
    gpu_yuk = torch.empty(size, dtype=torch.float32, device=device).fill_(1.0)
    
    # GPU'nun işlemi bitirdiğinden emin olalım
    torch.cuda.synchronize()
    
    print("Yüklendi! Görev Yöneticisi'ni kontrol et.")
    print("Kapatmak için CTRL+C yapabilirsin.")
    
    while True:
        # Bellekte kalması için sonsuz döngü
        time.sleep(1)

except KeyboardInterrupt:
    print("\nVeri boşaltılıyor...")
