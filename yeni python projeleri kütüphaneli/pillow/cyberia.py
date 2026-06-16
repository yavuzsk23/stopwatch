from PIL import Image, ImageDraw, ImageFont

resim_adi = "resim.jpg.png"

try:
    img = Image.open(resim_adi)
    
    # 1. Havalı bir efekt: Siyah-Beyaz yapalım
    bw_img = img.convert("L")
    
    # 2. Üzerine yazı yazmak için bir kalem (Draw) alalım
    cizici = ImageDraw.Draw(bw_img)
    
    # 3. Yazıyı basalım (Resmin sol üstüne)
    # Not: Yazı rengi siyah-beyaz modda 255 beyaz, 0 siyahtır.
    cizici.text((20, 20), "Cyberia - RTX 5060 Power", fill=255)
    
    # 4. Kaydet ve göster
    bw_img.save("cyberia_v1.png")
    bw_img.show()
    
    print("Kanka resim modifiye edildi, 'cyberia_v1.png' olarak hazır!")

except Exception as e:
    print(f"Hata çıktı kanka: {e}")
