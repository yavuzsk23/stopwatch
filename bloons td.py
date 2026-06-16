import pygame
import math
import sys
import random

# --- AYARLAR ---
GENISLIK, YUKSEKLIK = 900, 650
FPS = 60

# Renkler (Bloons Katmanları)
KIRMIZI = (255, 0, 0)    # 1 Can
MAVI = (0, 0, 255)       # 2 Can (Patlayınca Kırmızı çıkar)
YESIL = (0, 255, 0)      # 3 Can (Patlayınca Mavi çıkar)
SARI = (255, 255, 0)     # 4 Can (Patlayınca Yeşil çıkar)
BEYAZ = (255, 255, 255)
CIMEN = (124, 252, 0)
YOL_RENK = (210, 180, 140)

# Yol (Zikzak Çizen Klasik Harita)
YOL = [(0, 100), (700, 100), (700, 300), (100, 300), (100, 500), (900, 500)]

class Balon:
    def __init__(self, katman=1, yol_noktasi=0, pos=None):
        self.katman = katman
        self.yol = YOL
        self.nokta_index = yol_noktasi
        self.pos = pygame.Vector2(self.yol[0]) if pos is None else pygame.Vector2(pos)
        self.hiz = 1.5 + (katman * 0.3) # Üst katmanlar daha hızlı
        self.yok_et = False
        self.guncelle_renk()

    def guncelle_renk(self):
        renkler = {1: KIRMIZI, 2: MAVI, 3: YESIL, 4: SARI}
        self.renk = renkler.get(self.katman, KIRMIZI)
        self.boyut = 12 + (self.katman * 2)

    def guncelle(self):
        if self.nokta_index < len(self.yol) - 1:
            hedef = pygame.Vector2(self.yol[self.nokta_index + 1])
            yon = (hedef - self.pos)
            if yon.length() > self.hiz:
                self.pos += yon.normalize() * self.hiz
            else:
                self.nokta_index += 1
        else:
            self.yok_et = True # Sona ulaştı

    def vur(self, yeni_balonlar):
        if self.katman > 1:
            # Bir alt katmana düş ve aynı yerden devam et
            yeni_balonlar.append(Balon(self.katman - 1, self.nokta_index, self.pos))
        self.yok_et = True

    def ciz(self, ekran):
        # Balon şekli (üstü yuvarlak, altı hafif sivri)
        pygame.draw.circle(ekran, self.renk, (int(self.pos.x), int(self.pos.y)), self.boyut)
        pygame.draw.line(ekran, BEYAZ, (self.pos.x, self.pos.y + self.boyut), (self.pos.x, self.pos.y + self.boyut + 10))

class MaymunKulesi:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.menzil = 160
        self.ates_hizi = 20 # Bloons'da kuleler hızlı ateş eder
        self.sayac = 0

    def guncelle(self, balonlar, igneler):
        self.sayac += 1
        if self.sayac >= self.ates_hizi:
            for b in balonlar:
                if self.pos.distance_to(b.pos) < self.menzil:
                    igneler.append(Igne(self.pos.x, self.pos.y, b))
                    self.sayac = 0
                    break

    def ciz(self, ekran):
        # Maymunu temsil eden kahverengi daire
        pygame.draw.circle(ekran, (139, 69, 19), (int(self.pos.x), int(self.pos.y)), 18)
        pygame.draw.circle(ekran, (210, 180, 140), (int(self.pos.x), int(self.pos.y - 5)), 10) # Kafa

class Igne:
    def __init__(self, x, y, hedef):
        self.pos = pygame.Vector2(x, y)
        self.hedef = hedef
        self.hiz = 12
        self.yok_et = False

    def guncelle(self, balonlar, yeni_balonlar):
        yon = (self.hedef.pos - self.pos)
        if yon.length() > self.hiz:
            self.pos += yon.normalize() * self.hiz
        else:
            if self.hedef in balonlar:
                self.hedef.vur(yeni_balonlar)
            self.yok_et = True

    def ciz(self, ekran):
        pygame.draw.circle(ekran, (200, 200, 200), (int(self.pos.x), int(self.pos.y)), 4)

# --- ANA OYUN ---
pygame.init()
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
saat = pygame.time.Clock()

balonlar = []
kuleler = []
igneler = []
para = 250
dalga_sayaci = 0

while True:
    ekran.fill(CIMEN)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if para >= 100:
                kuleler.append(MaymunKulesi(*pygame.mouse.get_pos()))
                para -= 100

    # Balon Gönderme Mantığı
    dalga_sayaci += 1
    if dalga_sayaci % 40 == 0:
        # Rastgele katmanlı balon gönder
        katman = random.choices([1, 2, 3, 4], weights=[40, 30, 20, 10])[0]
        balonlar.append(Balon(katman))

    # Güncellemeler
    pygame.draw.lines(ekran, YOL_RENK, False, YOL, 45)
    
    yeni_balonlar = []
    for b in balonlar[:]:
        b.guncelle()
        if b.yok_et:
            if b.pos.x < GENISLIK: para += 5 # Patlatıldıysa para ver
            balonlar.remove(b)
        else:
            b.ciz(ekran)

    for k in kuleler:
        k.guncelle(balonlar, igneler)
        k.ciz(ekran)

    for i in igneler[:]:
        i.guncelle(balonlar, yeni_balonlar)
        if i.yok_et: igneler.remove(i)
        else: i.ciz(ekran)
    
    balonlar.extend(yeni_balonlar) # Yeni katmanları ekle

    # Arayüz
    font = pygame.font.SysFont("Comic Sans MS", 26, bold=True)
    ekran.blit(font.render(f"PARA: ${para}", True, (0, 0, 0)), (20, 20))
    ekran.blit(font.render("Dart Monkey: $100", True, (0, 0, 0)), (20, 50))

    pygame.display.flip()
    saat.tick(FPS)
