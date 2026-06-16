import pygame
import random
import time
import os

# --- Başlatma ---
pygame.init()

try:
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init()
except:
    print("Ses sistemi başlatılamadı.")

WIDTH, HEIGHT = 1000, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("İŞ ADAMLARI MTAL - Word Snake")
clock = pygame.time.Clock()

# --- Görsel ve Font Ayarları ---
font_ui = pygame.font.SysFont("Arial", 26, bold=True)
font_game = pygame.font.SysFont("Arial", 32, bold=True)
font_title = pygame.font.SysFont("Verdana", 65, bold=True) 
font_logo = pygame.font.SysFont("Arial", 18)

# --- Logo Yükleme ---
try:
    school_logo = pygame.image.load("logo.png")
    school_logo = pygame.transform.scale(school_logo, (180, 180))
except:
    school_logo = None 


eat_sound = None
crash_sound = None

try:
     
    if os.path.exists("eat.wav"):
        eat_sound = pygame.mixer.Sound("eat.wav")
    if os.path.exists("crash.wav"):
       crash_sound = pygame.mixer.Sound("crash.wav")
    
  
    if os.path.exists("music.mp3"):
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.set_volume(0.4) # Ses seviyesi %40 (Rahatsız etmemesi için)
        pygame.mixer.music.play(-1) # -1 parametresi müziği sonsuz döngüye sokar
    elif os.path.exists("music.wav"):
        pygame.mixer.music.load("music.wav")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
    else:
        print("Müzik dosyası (music.mp3) bulunamadı, sessiz devam ediliyor.")
except Exception as e:
    print(f"Ses yükleme hatası: {e}")

# --- Renkler ---
BLACK = (20, 20, 50)
WHITE = (255, 255, 255)
RED = (220, 20, 60)
GREEN = (57, 255, 20)
BLUE = (0, 255, 255)
PINK = (255, 20, 147)
GOLD = (255, 215, 0)

# --- Sabitler ---
HEDEF_METIN = "IS ADAMLARI MTAL"
SKOR_DOSYASI = "skorlar.txt"

def skoru_kaydet(isim, puan):
    with open(SKOR_DOSYASI, "a", encoding="utf-8") as f:
        f.write(f"{isim}:{puan}\n")

def skorlari_getir():
    if not os.path.exists(SKOR_DOSYASI): return []
    liste = []
    with open(SKOR_DOSYASI, "r", encoding="utf-8") as f:
        for satir in f:
            if ":" in satir:
                isim, puan = satir.strip().split(":")
                liste.append((isim, int(puan)))
    liste.sort(key=lambda x: x[1], reverse=True)
    return liste[:5]

# --- Oyun Değişkenleri ---
game_state = 0 
player_name = ""
score = 0
target_index = 1
snake_chars = ["I"]
snake_coords = [[500, 450]]
snake_dir = [25, 0]
food_pos = [0, 0]

def spawn_food():
    global food_pos
    if target_index < len(HEDEF_METIN):
        x = random.randrange(50, WIDTH - 50, 25)
        y = random.randrange(125, HEIGHT - 50, 25)
        food_pos = [x, y]

def reset_game():
    global snake_chars, snake_coords, snake_dir, target_index, score
    snake_chars = ["I"]
    snake_coords = [[500, 450]]
    snake_dir = [25, 0]
    target_index = 1
    score = 0
    spawn_food()

# --- Ana Döngü ---
running = True
while running:
    screen.fill(BLACK)
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
        if game_state == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and player_name.strip():
                    reset_game()
                    game_state = 1
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    if len(player_name) < 12:
                        player_name += event.unicode

        elif game_state == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dir[1] == 0: snake_dir = [0, -25]
                elif event.key == pygame.K_DOWN and snake_dir[1] == 0: snake_dir = [0, 25]
                elif event.key == pygame.K_LEFT and snake_dir[0] == 0: snake_dir = [-25, 0]
                elif event.key == pygame.K_RIGHT and snake_dir[0] == 0: snake_dir = [25, 0]

    if game_state == 0:
        if school_logo:
            screen.blit(school_logo, (WIDTH//2 - 90, 20))
        else:
            pygame.draw.rect(screen, (40, 40, 40), (WIDTH//2 - 90, 20, 180, 180), 2)
            lbl = font_logo.render("OKUL LOGOSU", True, (100, 100, 100))
            screen.blit(lbl, (WIDTH//2 - 60, 100))

        title_surf = font_title.render("MTAL WORD SNAKE", True, GOLD)
        screen.blit(title_surf, (WIDTH//2 - title_surf.get_width()//2, 220))
        
        prompt = font_game.render("Lütfen Adınızı Yazın:", True, BLUE)
        name_surf = font_game.render("> " + player_name + " <", True, WHITE)
        enter_msg = font_ui.render("Başlamak için ENTER'a basın", True, (150, 150, 150))
        
        screen.blit(prompt, (WIDTH//2 - 140, 380))
        screen.blit(name_surf, (WIDTH//2 - name_surf.get_width()//2, 440))
        screen.blit(enter_msg, (WIDTH//2 - 160, 580))

    elif game_state == 1:
        new_head = [snake_coords[0][0] + snake_dir[0], snake_coords[0][1] + snake_dir[1]]

        if (new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 100 or new_head[1] >= HEIGHT or new_head in snake_coords):
            if crash_sound: crash_sound.play() 
            skoru_kaydet(player_name, score)
            top_scores = skorlari_getir()
            game_state = 2
            end_time = time.time()
        else:
            snake_coords.insert(0, new_head)
            ate = False
            if new_head == food_pos:
                if eat_sound: eat_sound.play()
                snake_chars.append(HEDEF_METIN[target_index])
                target_index += 1
                score += 150
                if target_index >= len(HEDEF_METIN): target_index = 0
                spawn_food()
                ate = True
            if not ate: snake_coords.pop()

        pygame.draw.rect(screen, (20, 20, 35), (0, 0, WIDTH, 100))
        screen.blit(font_ui.render(f"OYUNCU: {player_name}", True, WHITE), (20, 35))
        screen.blit(font_ui.render(f"SKOR: {score}", True, GREEN), (WIDTH - 180, 35))
        
        for i, char in enumerate(HEDEF_METIN):
            color = GREEN if i < target_index else (70, 70, 70)
            if i == target_index: color = BLUE
            screen.blit(font_ui.render(char if char != " " else "_", True, color), (300 + i*22, 35))
        
        if target_index < len(HEDEF_METIN):
            f_char = HEDEF_METIN[target_index]
            screen.blit(font_game.render(f_char if f_char != " " else "[_]", True, PINK), (food_pos[0], food_pos[1]))

        for i, pos in enumerate(snake_coords):
            color = RED if i == 0 else GREEN
            screen.blit(font_game.render(snake_chars[i], True, color), (pos[0], pos[1]))

    elif game_state == 2:
        title_f = pygame.font.SysFont("Arial", 45, bold=True)
        screen.blit(title_f.render("EN İYİ 5 SKOR", True, GOLD), (WIDTH//2 - 150, 100))
        
        for i, (isim, puan) in enumerate(top_scores):
            color = GREEN if isim == player_name and puan == score else WHITE
            txt = font_game.render(f"{i+1}. {isim}: {puan}", True, color)
            screen.blit(txt, (WIDTH//2 - 120, 220 + (i * 60)))

        passed_time = time.time() - end_time
        remaining = max(0, 5 - int(passed_time))
        
        timer_txt = font_ui.render(f"YENİ OYUN İÇİN GERİ SAYIM: {remaining}", True, RED)
        screen.blit(timer_txt, (WIDTH//2 - 180, 620))

        if passed_time > 5:
            game_state = 0
            player_name = "" 

    pygame.display.flip()
    clock.tick(7)

pygame.quit()
