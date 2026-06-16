import multiprocessing
import os
import numpy as np # Eğer yüklü değilse 'pip install numpy' yapman gerekir

def hardcore_kastirici():
    # Bu fonksiyon hem işlemciyi hem RAM veri yolunu yorar
    while True:
        # 1. Devasa matrisler oluştur (RAM ve CPU Cache yorar)
        matrix_size = 5000
        a = np.random.rand(matrix_size, matrix_size)
        b = np.random.rand(matrix_size, matrix_size)
        
        # 2. Matris çarpımı yap (CPU'nun içindeki tüm transistörleri ateşler)
        # Bu işlem en ağır CPU işlemlerinden biridir.
        c = np.dot(a, b)
        
        # 3. Gereksiz bir döngüyle sistemi meşgul et
        _ = [i**2 for i in range(1000)]

if __name__ == "__main__":
    # Çekirdek sayısının 2 katı kadar işlem başlatıyoruz (Hyper-threading'i de patlatmak için)
    counts = multiprocessing.cpu_count() * 2
    print(f"{counts} koldan saldırı başlıyor. Şimdi gör bakalım kasmıyor mu...")
    
    processes = []
    for i in range(counts):
        p = multiprocessing.Process(target=hardcore_kastirici)
        p.daemon = True # Ana program kapanınca bunlar da kapansın (eğer kapanabilirse)
        p.start()
        processes.append(p)
    
    # Bilgisayar hala yaşıyorsa bekle
    for p in processes:
        p.join()
