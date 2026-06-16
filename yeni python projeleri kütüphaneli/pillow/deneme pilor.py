from PIL import Image
import os

# Dosya ismini tam olarak listedeki gibi yazıyoruz
resim_adi = "resim.jpg.png" 

if os.path.exists(resim_adi):
    img = Image.open(resim_adi)
    print("Sonunda yakaladık seni!")
    
    # Boyutu değiştirip kaydedelim
    yeni = img.resize((500, 500))
    yeni.save("kurtarildi.png")
    yeni.show()
else:
    print("Kanka isim doğru ama hala göremiyorum...")
