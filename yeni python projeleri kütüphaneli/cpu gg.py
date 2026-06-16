import multiprocessing
import numpy as np
import time

def solo_kastirici():
    print("Tek koldan hafif antrenman başladı... Sistem yağ gibi akar.")
    while True:
        # Matris boyutu yine 2000, tek çekirdek için ideal
        matrix_size = 2000 
        a = np.random.rand(matrix_size, matrix_size)
        b = np.random.rand(matrix_size, matrix_size)
        # Sadece çarpıyoruz, başka işe bulaşmıyoruz
        c = np.dot(a, b)

if __name__ == "__main__":
    # Sadece 1 tane süreç başlatıyoruz
    p = multiprocessing.Process(target=solo_kastirici)
    p.daemon = True
    p.start()
    
    print("Şu an sadece 1 çekirdek meşgul. Görev yöneticisinden izleyebilirsin.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Durduruldu.")
