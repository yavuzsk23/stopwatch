from pydub import AudioSegment

def sesi_manipule_et(dosya_yolu):
    print(f"🎚️ {dosya_yolu} Cyberia Stüdyo'da işleniyor...")

    try:
        # 1. Ses dosyasını yüklüyoruz
        ses = AudioSegment.from_file(dosya_yolu)

        # 2. Ses seviyesini 10 dB artırıyoruz (Kulağına dikkat et!)
        yuksek_ses = ses + 10

        # 3. İlk 2 saniyeyi (2000 milisaniye) kesip atıyoruz
        kesilmis_ses = yuksek_ses[2000:]

        # 4. Sonuna 3 saniyelik bir yavaşça sönme (fade-out) ekliyoruz
        final_ses = kesilmis_ses.fade_out(3000)

        # 5. Yeni dosyayı kaydediyoruz
        cikti_adi = "cyberia_remix.wav"
        final_ses.export(cikti_adi, format="wav")

        print(f"✅ İşlem tamam kanka!")
        print(f"📁 Yeni dosyan: {cikti_adi}")
        print(f"⏳ Uzunluk: {len(final_ses) / 1000} saniye")

    except Exception as e:
        print(f"Kanka bir sorun çıktı: {e}")

# Kodu ateşle
sesi_manipule_et("test_ses.wav")
