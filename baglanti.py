import requests

# 1. Sunucunun adresini tanımlıyoruz (Hani o tarayıcıya yazdığın adres)
url = "http://127.0.0.1:8000"

print("--- Sunucuya istek gönderiliyor... ---")

try:
    # 2. GET isteği gönderiyoruz (Sunucudan veri istiyoruz)
    response = requests.get(url)

    # 3. Eğer bağlantı başarılıysa (Statü kodu 200 ise)
    if response.status_code == 200:
        veri = response.json() # Gelen JSON verisini Python sözlüğüne çeviriyoruz
        print("Bağlantı Başarılı! ✅")
        print(f"Gelen Durum: {veri['durum']}")
        print(f"Yazılımcı: {veri['yavuz']}")
    else:
        print(f"Bir sorun var kanka! Hata kodu: {response.status_code}")

except Exception as e:
    print(f"Eyvah! Sunucu kapalı mı acaba? Hata: {e}")

print("--- İşlem tamamlandı. ---")
