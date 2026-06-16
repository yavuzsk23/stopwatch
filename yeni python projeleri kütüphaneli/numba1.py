import numpy as np
from numba import jit
import time

# 1. NORMAL PYTHON FONKSİYONU
def normal_hesaplama(n):
    sonuc = 0
    for i in range(n):
        sonuc += (i ** 0.5)
    return sonuc

# 2. NUMBA İLE GÜÇLENDİRİLMİŞ FONKSİYON
# @jit(nopython=True) demek; Python'u devreden çıkar, direkt makine diline geç demek!
@jit(nopython=True)
def numba_hesaplama(n):
    sonuc = 0
    for i in range(n):
        sonuc += (i ** 0.5)
    return sonuc

# TEST BAŞLIYOR
sayi_limit = 10_000_000 # 10 Milyon işlem

print(f"🚀 Cyberia Hız Testi Başlıyor ({sayi_limit} işlem)...")

# Normal Python Testi
start = time.time()
normal_hesaplama(sayi_limit)
print(f"🐢 Normal Python Süresi: {time.time() - start:.4f} saniye")

# Numba Testi (İlk çalıştırmada derleme yaptığı için çok az bekletebilir)
start = time.time()
numba_hesaplama(sayi_limit)
print(f"⚡ Numba (Cyberia Mode) Süresi: {time.time() - start:.4f} saniye")
