import time

# RAM'i dolduracak olan devasa liste
shisirme_listesi = []

print("RAM doldurma işlemi başlıyor... Durdurmak için Ctrl+C (Tabii yapabilirsen!)")

try:
    while True:
        # Her döngüde listeye devasa bir metin bloğu ekliyoruz
        # 'a' karakterini 1 milyonla çarparak her adımda RAM'e yük bindiriyoruz
        shisirme_listesi.append('X' * 10**6) 
        
        # Ne kadar veri biriktiğini yazdıralım (bir noktadan sonra yazamaz bile)
        if len(shisirme_listesi) % 100 == 0:
            print(f"Şu an RAM'de yaklaşık {len(shisirme_listesi)} MB veri kilitlendi.")
            
except MemoryError:
    print("RAM Tamamen Doldu! İşletim sistemi Python'un eline verdi.")
