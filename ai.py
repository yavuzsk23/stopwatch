import os
# BURASI KRİTİK: PyTorch'a diyoruz ki "Kartı RTX 40 serisi gibi çalıştır"
os.environ['TORCH_CUDA_ARCH_LIST'] = '8.6'
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

import torch

print("🚀 RTX 5060 'Kandirma' Testi Basliyor...")

try:
    # 1. Küçük bir veri oluştur
    # .cuda() yerine .to("cuda") kullanmak bazen daha stabildir
    x = torch.tensor([1.0, 2.0, 3.0]).to("cuda")
    
    # 2. Basit bir işlem yap
    y = x * 2
    
    print(f"✅ HİLE BAŞARILI! Karttan gelen veri: {y}")
    print(f"📡 Kullanilan Cihaz: {torch.cuda.get_device_name(0)}")
    print("\nKanka karti kandirdik, su an calisiyor olmali!")

except Exception as e:
    print(f"❌ Kandirma operasyonu yemedi: {e}")
    print("\nKanka bu durumda tek care NVIDIA ve PyTorch'un")
    print("RTX 50 serisi icin resmi guncelleme yayinlamasini beklemek.")
