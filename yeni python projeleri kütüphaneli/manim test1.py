from manim import *
from loguru import logger

# Manim'de her görsel senaryo bir sınıf (Scene) olarak yazılır kanka
class CyberiaIlkAnimasyon(Scene):
    def construct(self):
        logger.info("Manim render motoru sahneyi hazırlıyor...")

        # 1. Siber bir çember oluşturuyoruz
        cember = Circle()
        # Çemberin rengini neon mavi (Cyberia rengi!) yapalım ve içini dolduralım
        cember.set_fill(BLUE, opacity=0.5)
        cember.set_color(CYAN)

        # 2. Ekrana bir yazı ekleyelim
        yazi = Text("Cyberia Uzay Üssü", font_size=40).next_to(cember, DOWN)

        # 3. Şov başlıyor: Animasyonu ekrana çizdiriyoruz
        logger.success("Render başlatıldı! Çember çiziliyor...")
        self.play(Create(cember)) # Çemberi dönerek çizme animasyonu
        self.play(Write(yazi))    # Yazıyı klavyeyle yazılıyormuş gibi getirme
        
        # Ekranda 2 saniye bekle ve sahneyi bitir
        self.wait(2)
        logger.success("Animasyon sahnesi başarıyla tamamlandı!")
