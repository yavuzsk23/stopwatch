from PIL import Image, ImageChops
import os

resim_adi = "resim.jpg.png"

if os.path.exists(resim_adi):
    img = Image.open(resim_adi)
    
    # RGB modunda olduğumuzdan emin olalım (Yoksa hata verebilir)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # İŞTE O SİHİRLİ SATIR: Renkleri tersine çevir (Invert)
    # Beyazlar siyah, kırmızılar turkuaz olur!
    ters_resim = ImageChops.invert(img)
    
    # Kaydet ve göster
    ters_resim.save("cyberia_negatif.png")
    ters_resim.show()
    
    print("Kanka renkler kriz geçirdi! 'cyberia_negatif.png' hazır.")
else:
    print("Kanka dosyayı yine mi kaybettin?")
