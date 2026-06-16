from manim import *

class CyberiaIlkAnimasyon(Scene):
    def construct(self):
        # 1. Siber bir çember oluşturuyoruz
        cember = Circle()
        cember.set_fill(BLUE, opacity=0.5) # İçini mavi yap
        cember.set_color(TEAL)             # Hata veren yeri TEAL (Turkuaz) yaptık kanka!

        # 2. Ekrana bir yazı ekleyelim
        yazi = Text("Cyberia Almanyası", font_size=40).next_to(cember, DOWN)

        # 3. Animasyonu ekrana çizdiriyoruz
        self.play(Create(cember)) # Çemberi çiz
        self.play(Write(yazi))    # Yazıyı getir
        self.wait(2)              # 2 saniye ekranda beklet
