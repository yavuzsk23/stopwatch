import pygame
import sys
import time

pygame.init()

# Ekran ayarları
WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dijital Saat")

# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font
font = pygame.font.SysFont("Arial", 80)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    # Şu anki saat
    current_time = time.strftime("%H:%M:%S")

    # Ekranı temizle
    screen.fill(BLACK)

    # Saat yazısı
    text_surface = font.render(current_time, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(text_surface, text_rect)

    # Güncelle
    pygame.display.update()
    clock.tick(1)  # saniyede 1 kez güncelle
