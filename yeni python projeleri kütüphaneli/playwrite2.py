import asyncio
from playwright.async_api import async_playwright

async def doviz_avcisi():
    async with async_playwright() as p:
        # Arka planda çalışsın (headless=True), hız kazanalım
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("🌐 Google'da sorgu başlatılıyor...")
        await page.goto("https://www.google.com")

        # Google arama kutusuna 'Dolar kac tl' yaz ve Enter'a bas
        # 'textarea' etiketi modern Google arama kutusudur
        await page.fill('textarea[name="q"]', 'Dolar kac tl')
        await page.press('textarea[name="q"]', 'Enter')

        # Sonuçların yüklenmesini bekle (Döviz kutusu sınıfı genelde .DMMBqb olur)
        await page.wait_for_selector('.DMMBqb', timeout=5000)

        # Fiyat bilgisini çekiyoruz
        fiyat = await page.inner_text('.DMMBqb')
        
        print("\n" + "="*30)
        print(f"📈 CYBERIA FİNANS RAPORU")
        print(f"💵 1 DOLAR = {fiyat} TL")
        print("="*30 + "\n")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(doviz_avcisi())
