import asyncio
from playwright.async_api import async_playwright

async def doviz_avcisi_gizli():
    async with async_playwright() as p:
        # headless=False yaptık ki engel çıkarsa görebilelim
        # slow_mo ekledik ki her hareketi 500ms yavaş yapsın (İnsan hızı)
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        
        # Gerçek bir tarayıcı gibi görünmek için 'User Agent' ekliyoruz
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        print("🌐 Google'a giriş yapılıyor...")
        await page.goto("https://www.google.com")

        # Eğer önüne çerez onayı çıkarsa diye bekleyelim
        await asyncio.sleep(1)

        # Arama kutusuna yavaşça yazıyoruz
        print("🔍 Sorgu yazılıyor...")
        await page.fill('textarea[name="q"]', 'Dolar kac tl')
        await page.press('textarea[name="q"]', 'Enter')

        # Google'ın sonucu yüklemesi için biraz daha süre verelim (10 saniye)
        try:
            print("⏳ Fiyat aranıyor...")
            # Google sınıf isimlerini bazen değiştirir, o yüzden genel bir seçici deniyoruz
            await page.wait_for_selector('span[data-precision="2"]', timeout=10000)
            fiyat = await page.inner_text('span[data-precision="2"]')
            
            print("\n" + "="*30)
            print(f"📈 CYBERIA FİNANS RAPORU")
            print(f"💵 1 DOLAR = {fiyat} TL")
            print("="*30 + "\n")
        except Exception as e:
            print(f"Kanka Google yine engel koydu veya sınıf değişti. Hata: {e}")
            # Engel çıkarsa ekranı gör diye hemen kapatmıyoruz
            await asyncio.sleep(10)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(doviz_avcisi_gizli())
