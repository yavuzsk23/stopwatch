import asyncio
from playwright.async_api import async_playwright

async def cyberia_doviz_v2():
    async with async_playwright() as p:
        # headless=True yapabiliriz, bu site Google kadar agresif değil
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("🌐 Doviz.com'a bağlanılıyor...")
        await page.goto("https://www.doviz.com")

        # Sayfanın yüklenmesini bekle
        await page.wait_for_selector('span[data-socket-key="USD"]', timeout=10000)

        # Dolar değerini o özel kutudan çekiyoruz
        dolar_degeri = await page.inner_text('span[data-socket-key="USD"]')
        
        print("\n" + "X"*35)
        print(f"🚀 CYBERIA NETWORK FINANS")
        print(f"💵 GÜNCEL DOLAR: {dolar_degeri} TL")
        print("X"*35 + "\n")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(cyberia_doviz_v2())
