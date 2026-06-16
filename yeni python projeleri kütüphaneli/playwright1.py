import asyncio
from playwright.async_api import async_playwright

async def cyberia_bot():
    async with async_playwright() as p:
        # Tarayıcıyı başlatıyoruz (headless=False yaptık ki açıldığını göresin)
        # Sende sistem sağlam olduğu için yavaşlamaz
        browser = await p.chromium.launch(headless=False) 
        page = await browser.new_page()

        print("🌐 Cyberia Botu Google'a gidiyor...")
        await page.goto("https://www.google.com")

        # Sayfanın yüklenmesi için 2 saniye bekleyelim
        await asyncio.sleep(2)

        # Ekran görüntüsü alalım
        print("📸 Ekran görüntüsü alınıyor...")
        await page.screenshot(path="cyberia_google.png")

        print("✅ Başarılı! 'cyberia_google.png' dosyası oluşturuldu kanka.")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(cyberia_bot())
