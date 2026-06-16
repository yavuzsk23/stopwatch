from PIL import Image
import customtkinter as ctk
import os

# Pencereyi kuralım
root = ctk.CTk()
root.title("CYBERIA IMAGE LAB")
root.geometry("500x500")

# DİKKAT: Buradaki yolu senin bilgisayarındaki gerçek bir resimle değiştir kanka!
# Örnek: "E:/cyberia_logo.png" veya "C:/Users/yavuz/Pictures/resim.jpg"
resim_yolu = "E:/logo.png" 

def ekranı_doldur(yol):
    try:
        # 1. Kontrol: Dosya gerçekten orada mı?
        if not os.path.exists(yol):
            print(f"Kanka {yol} adresinde resim bulamadım, o yüzden beyaz kaldı!")
            return

        # 2. Resmi aç ve boyutlandır
        img = Image.open(yol)
        
        # 3. CustomTkinter formatına çevir
        # Sende RTX 5060 var, görüntü kaliteli olsun diye size'ı büyütüyoruz
        ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(350, 350))
        
        # 4. Etikete (Label) resmi yapıştır
        label = ctk.CTkLabel(root, image=ctk_img, text="")
        label.pack(pady=40)
        
        print("Kanka resim başarıyla yüklendi, beyazlık bitti!")

    except Exception as e:
        print(f"Hata çıktı kanka: {e}")

# KİTİT NOKTA: Fonksiyonu burada çağırıyoruz!
ekranı_doldur(resim_yolu)

root.mainloop()
