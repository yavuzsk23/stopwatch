import requests

url = "http://127.0.0.1:8000/selamla"

# Sunucuya göndereceğimiz veri paketi
benim_verim = {
    "isim": "Yavuz",
    "yas": 14
}

print("--- Sunucuya veri paketi gönderiliyor... ---")

# POST isteği fırlatıyoruz
response = requests.post(url, json=benim_verim)

if response.status_code == 200:
    print("Sunucudan Gelen Cevap: ✅")
    print(response.json()["mesaj"])
else:
    print("Bir hata oldu kanka!")
