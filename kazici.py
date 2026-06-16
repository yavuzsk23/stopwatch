import requests
from bs4 import BeautifulSoup

# Kendimizi gerçek bir kullanıcı gibi tanıtıyoruz
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Eğer Wikipedia yine naz yaparsa bu sefer Google'ı deneyelim
url = "https://www.google.com"

print(f"--- {url} sitesine bağlanılıyor... ---")

try:
    # headers ekleyerek gidiyoruz
    response = requests.get(url, headers=headers, timeout=10)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        site_basligi = soup.title.string
        print(f"Sitenin Başlığı: {site_basligi} ✅")
        print("Bağlantı koptu gidiyor kanka!")
    else:
        print(f"Hata kodu: {response.status_code}. Site kapıyı açmadı.")
except Exception as e:
    print(f"Bağlantı sırasında bir hata oluştu: {e}")
