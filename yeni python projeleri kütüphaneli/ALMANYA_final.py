from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from loguru import logger
import datetime

# BotFather'dan gelen gizli anahtarın kanka, koda gömdük!
BOT_TOKEN = "8251356082:AAEBJIf5ojXZXX022Jg8mB3BJshSRg-Zq7o"

# Cyberia Çalışma Programı
PROGRAM = {
    0: "Pazartesi: Almanca ve Genel Tekrar Günü! 🇩🇪 (Almanya BT kelimelerine odaklan)",
    1: "Salı: Backend Günü! Kod motorunu ateşle. 🚀",
    2: "Çarşamba: Almanca Çalışma Günü! Bis bald! 🇩🇪",
    3: "Perşembe: Algoritma ve Pratik Günü! Mantığı geliştir. 💻",
    4: "Cuma: C# Günü! Nesne yönelimli dünyaya giriş. 👑",
    5: "Cumartesi: C# ve Proje Günü! Bugün bota yeni özellik ekleme zamanı! 🔥",
    6: "Pazar: SQL ve Veritabanı Günü! Tabloları uçuracağız. 📊"
}

async def start_komutu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kullanici = update.effective_user.first_name
    logger.info(f"{kullanici} botu başlattı.")
    
    mesaj = (
        f"hoş geldin yavuz {kullanici}  🤖\n"
        f"Cyberia Almanya şu andan itibaren emrinde.\n\n"
        f"Bugünün dersini öğrenmek için: /bugun yazman yeterli!"
    )
    await update.message.reply_text(mesaj)

async def bugun_komutu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Bugün haftanın kaçıncı günü olduğunu bulur (0=Pazartesi, 5=Cumartesi, 6=Pazar)
    kacinci_gun = datetime.datetime.now().weekday()
    gunun_dersi = PROGRAM.get(kacinci_gun, "Program bulunamadı kanka.")
    
    logger.success(f"Ders programı sorgusu başarılı: {gunun_dersi}")
    await update.message.reply_text(f"📊 *Cyberia Planlayıcı* 📊\n\n🎯 {gunun_dersi}", parse_mode="Markdown")

def ana_calistirici():
    logger.info("Cyberia Almanya Botu başlatılıyor... Donanım kontrol ediliyor.")
    
    # Telegram bağlantısını kuruyoruz
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Komutları bota öğretiyoruz
    app.add_handler(CommandHandler("start", start_komutu))
    app.add_handler(CommandHandler("bugun", bugun_komutu))
    
    logger.success("Bot şu an Telegram sunucularına bağlandı, sinyal bekliyor kanka!")
    
    # PC açık olduğu sürece botu aktif tutar
    app.run_polling()

if __name__ == "__main__":
    ana_calistirici()
