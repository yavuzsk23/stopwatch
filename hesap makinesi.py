import pygame
import sys

pygame.init()

# Ekran ayarları
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Hesap Makinesi")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Font
font = pygame.font.SysFont("Arial", 40)

# Butonlar
buttons = [
    "7","8","9","+",
    "4","5","6","-",
    "1","2","3","*",
    "C","0","=","/"
]

# Hesaplama için değişken
current_input = ""

def draw_buttons():
    screen.fill(WHITE)
    # Input alanı
    input_surface = font.render(current_input, True, BLACK)
    screen.blit(input_surface, (20, 20))

    # Butonları çiz
    for i, text in enumerate(buttons):
        x = (i % 4) * 100
        y = (i // 4) * 100 + 100
        pygame.draw.rect(screen, GRAY, (x, y, 100, 100))
        btn_text = font.render(text, True, BLACK)
        screen.blit(btn_text, (x+35, y+35))

    pygame.display.update()

def calculate(expr):
    try:
        return str(eval(expr))
    except:
        return "Error"

# Ana döngü
running = True
while running:
    draw_buttons()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y > 100:
                col = x // 100
                row = (y - 100) // 100
                idx = row * 4 + col
                if idx < len(buttons):
                    value = buttons[idx]
                    if value == "C":
                        current_input = ""
                    elif value == "=":
                        current_input = calculate(current_input)
                    else:
                        current_input += value
