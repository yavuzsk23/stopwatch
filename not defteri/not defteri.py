import pygame
import sys

pygame.init()

# Ekran ayarları
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Not Defteri")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont("Arial", 24)

# Yazı alanı
text = ""

def draw_text():
    screen.fill(WHITE)
    lines = text.split("\n")
    y = 20
    for line in lines:
        surface = font.render(line, True, BLACK)
        screen.blit(surface, (20, y))
        y += 30
    pygame.display.update()

running = True
while running:
    draw_text()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pygame.K_RETURN:
                text += "\n"
            elif event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                text = ""  # Ctrl+C yerine temizleme
            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                with open("not_defteri.txt", "w", encoding="utf-8") as f:
                    f.write(text)
                print("Kaydedildi: not_defteri.txt")
            else:
                text += event.unicode
