import os
import torch
import time

# --- SAHTE KİMLİK AYARI ---
# PyTorch'a uyumlu bir mimariyi zorla kabul ettiriyoruz (RTX 4070 mimarisi sm_89'dur)
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["TORCH_CUDA_ARCH_LIST"] = "8.9" 
# Bazı durumlarda bu değişken PyTorch'un hata vermesini engelleyebilir
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"

import torch # Ayarlardan sonra tekrar import etmek gerekebilir

if not torch.cuda.is_available():
    print("HATA: GPU hala tanınmıyor!")
    exit()

device = torch.device("cuda")

# 100 MB veri
size = 100 * 1024 * 1024 // 4 

try:
    print("RTX 5060, şu an 4070 kılığında operasyona başlıyor...")
    
    # KARTIN GÖZÜNÜ BOYUYORUZ
    gpu_yuk = torch.empty(size, dtype=torch.float32, device=device).fill_(1.0)
    
    torch.cuda.synchronize()
    
    print("\n[✓] Kimlik doğrulaması geçildi! 100 MB VRAM'e yüklendi.")
    print("CMD'den 'nvidia-smi' yazıp 100 MB artışı kontrol et.")
    
    while True:
        time.sleep(1)

except Exception as e:
    print(f"\n[!] Eyvah, yakalandık! Hata: {e}")
    print("Not: Kart çok yeni olduğu için bu 'yalan' her zaman yemeyebilir.")

except KeyboardInterrupt:
    print("\nOperasyon bitti.")
