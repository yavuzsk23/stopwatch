# YILAN OYUNU 

import pygame
import random
import sys
import time
import math
import json
import os

pygame.init()
pygame.mixer.init()

# Ekran ayarları - 1000x750
WIDTH, HEIGHT = 1000, 750
CELL = 20
UI_HEIGHT = 100  # UI panel yüksekliği
PLAY_AREA_TOP = UI_HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yilan Oyunu - FINAL 4.0 - Denizli Is Adamlari MTAL")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("consolas", 15)
FONT_BIG = pygame.font.SysFont("consolas", 40)
FONT_SMALL = pygame.font.SysFont("consolas", 11)
FONT_TINY = pygame.font.SysFont("consolas", 9)

TARGET_FPS = 10
SNAKE_SPEED = 10  # Saniyede kaç hücre

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 100, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 150, 255)
PURPLE = (200, 0, 255)
CYAN = (0, 255, 255)
TURQUOISE = (64, 224, 208)
GRAY = (100, 100, 100)
PINK = (255, 192, 203)
BROWN = (139, 69, 19)
LIME = (50, 205, 50)
MAGENTA = (255, 0, 255)

SNAKE_COLORS = [GREEN, CYAN, YELLOW, ORANGE, PURPLE, PINK, LIME, BLUE]

HIGH_SCORE_FILE = "highscore.txt"
LEADERBOARD_FILE = "leaderboard.json"

# Sesler
print("Sesler yukleniyor...")
try:
    yem_sesi = pygame.mixer.Sound("yem_sesi.wav")
    yem_sesi.set_volume(0.5)
    print("+ yem_sesi.wav")
except:
    yem_sesi = None
    print("- yem_sesi.wav")

try:
    olum_sesi = pygame.mixer.Sound("olum_sesi.wav")
    olum_sesi.set_volume(0.7)
    print("+ olum_sesi.wav")
except:
    olum_sesi = None
    print("- olum_sesi.wav")

try:
    double_sesi = pygame.mixer.Sound("double_sesi.wav")
    double_sesi.set_volume(0.6)
    print("+ double_sesi.wav")
except:
    double_sesi = None
    print("- double_sesi.wav")

# Arka plan
print("Arka plan yukleniyor...")
background = None
for ext in ["jpg", "jpeg", "png"]:
    try:
        bg = pygame.image.load(f"okul_arkaplan.{ext}")
        background = pygame.transform.scale(bg, (WIDTH, HEIGHT))
        background.set_alpha(80)
        print(f"+ okul_arkaplan.{ext}")
        break
    except:
        pass
if not background:
    print("- Arka plan bulunamadi")

print("\n=== FINAL OYUN BASLIYOR ===\n")

# Parçacık
class Particle:
    def __init__(self, x, y, color):
        self.x = x + random.randint(-8, 8)
        self.y = y + random.randint(-8, 8)
        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-4, 4)
        self.color = color
        self.life = 40
        self.size = random.randint(3, 8)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.2
        self.life -= 1
        self.size = max(1, self.size - 0.15)
    
    def draw(self, screen):
        if self.life > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

# Ateş
class Fireball:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        angle = math.atan2(target_y - y, target_x - x)
        self.vx = math.cos(angle) * 5
        self.vy = math.sin(angle) * 5
        self.active = True
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT:
            self.active = False
    
    def draw(self, screen):
        pygame.draw.circle(screen, ORANGE, (int(self.x), int(self.y)), 6)
        pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), 3)

# Yaratık
class Monster:
    def __init__(self, score):
        self.y = random.randint((UI_HEIGHT // CELL) + 2, (HEIGHT // CELL) - 3) * CELL
        self.x = random.choice([0, WIDTH - CELL])
        self.base_speed = 2
        self.speed = self.base_speed + ((score - 35) // 5)
        self.direction = 1 if self.x == 0 else -1
        self.chase_mode = False
        self.fire_timer = 0
        self.fire_rate = 2.0
    
    def update(self, snake_head, score, dt):
        if score >= 43:
            self.chase_mode = True
            dx = snake_head[0] - self.x
            dy = snake_head[1] - self.y
            distance = math.sqrt(dx**2 + dy**2)
            if distance > 0:
                self.x += (dx / distance) * self.speed
                self.y += (dy / distance) * self.speed
        else:
            self.x += self.speed * self.direction
            if self.x >= WIDTH - CELL or self.x <= 0:
                self.direction *= -1
        
        self.speed = self.base_speed + ((score - 35) // 5)
        
        if score >= 60:
            self.fire_rate = 1.0
        elif score >= 50:
            self.fire_rate = 2.0
        
        self.fire_timer += dt
    
    def can_fire(self, score):
        return score >= 50 and self.fire_timer >= self.fire_rate
    
    def fire(self, target_x, target_y):
        self.fire_timer = 0
        return Fireball(self.x + CELL//2, self.y + CELL//2, target_x, target_y)
    
    def draw(self, screen, pulse):
        color = (255, 0, 255) if pulse > 3 else (200, 0, 200)
        pygame.draw.rect(screen, color, (int(self.x), int(self.y), CELL, CELL))
        pygame.draw.rect(screen, WHITE, (int(self.x), int(self.y), CELL, CELL), 2)
        eye_size = 3
        pygame.draw.circle(screen, RED, (int(self.x + 8), int(self.y + 8)), eye_size)

def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, 'r') as f:
            return int(f.read())
    except:
        return 0

def save_high_score(score):
    with open(HIGH_SCORE_FILE, 'w') as f:
        f.write(str(score))

def load_leaderboard():
    """Skor tablosunu yükle"""
    try:
        with open(LEADERBOARD_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_leaderboard(leaderboard):
    """Skor tablosunu kaydet"""
    with open(LEADERBOARD_FILE, 'w', encoding='utf-8') as f:
        json.dump(leaderboard, f, ensure_ascii=False, indent=2)

def add_to_leaderboard(name, score):
    """Skor tablosuna ekle"""
    leaderboard = load_leaderboard()
    leaderboard.append({"name": name, "score": score})
    leaderboard.sort(key=lambda x: x["score"], reverse=True)
    leaderboard = leaderboard[:10]  # En iyi 10
    save_leaderboard(leaderboard)
    return leaderboard

def get_player_name():
    """Oyuncu ismini al"""
    name = ""
    entering = True
    
    while entering:
        screen.fill(BLACK)
        if background:
            screen.blit(background, (0, 0))
        
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        draw_text("ISMINIZI GIRIN", (WIDTH//2 - 100, HEIGHT//2 - 80), CYAN, FONT_BIG)
        draw_text("(En fazla 15 karakter)", (WIDTH//2 - 100, HEIGHT//2 - 30), GRAY, FONT_SMALL)
        
        # İsmi göster
        name_display = name + "_"
        draw_text(name_display, (WIDTH//2 - 150, HEIGHT//2 + 20), WHITE, FONT_BIG)
        
        draw_text("ENTER - Onayla  |  ESC - Atla", (WIDTH//2 - 130, HEIGHT//2 + 80), GREEN, FONT_SMALL)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Oyuncu"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if name.strip():
                        entering = False
                    else:
                        name = "Oyuncu"
                        entering = False
                elif event.key == pygame.K_ESCAPE:
                    name = "Oyuncu"
                    entering = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < 15:
                    if event.unicode.isprintable():
                        name += event.unicode
    
    return name if name else "Oyuncu"

def draw_text(text, pos, color=WHITE, font=None):
    if font is None:
        font = FONT
    surf = font.render(text, True, color)
    screen.blit(surf, pos)

def random_position(avoid_positions):
    """Oyun alanında rastgele pozisyon"""
    while True:
        x = random.randint(0, (WIDTH - CELL) // CELL) * CELL
        y = random.randint(0, (HEIGHT - CELL) // CELL) * CELL
        pos = (x, y)
        if pos not in avoid_positions:
            return pos

def play_sound(sound):
    if sound:
        sound.play()

def find_closest_food(head, foods):
    if not foods:
        return None
    closest = min(foods, key=lambda f: math.sqrt((f[0]-head[0])**2 + (f[1]-head[1])**2))
    return closest

def draw_apple(x, y):
    """Elma yem"""
    pygame.draw.circle(screen, RED, (x + CELL//2, y + CELL//2), CELL//2)
    pygame.draw.circle(screen, (255, 100, 100), (x + CELL//2, y + CELL//2), CELL//2, 2)
    pygame.draw.rect(screen, BROWN, (x + CELL//2 - 1, y, 2, 5))
    pygame.draw.ellipse(screen, GREEN, (x + CELL//2 + 2, y - 2, 6, 4))

def draw_snake_smooth(snake, direction, ghost_active, shield_active, stealth_active, in_ui_area, blink, tongue_out, closest_food, dt, snake_color):
    """Yılan - smooth 60 FPS"""
    # Renk
    if in_ui_area:
        # UI'da şeffaf
        color = snake_color
        alpha = 100
    elif ghost_active:
        color = TURQUOISE
        alpha = 128
    elif stealth_active:
        color = (150, 150, 150)
        alpha = 100
    elif shield_active:
        color = BLUE
        alpha = 255
    else:
        color = snake_color
        alpha = 255
    
    # Gövde
    for i in range(len(snake) - 1):
        start = snake[i]
        end = snake[i + 1]
        
        if alpha < 255:
            s = pygame.Surface((abs(end[0] - start[0]) + CELL, abs(end[1] - start[1]) + CELL))
            s.set_alpha(alpha)
            s.fill(color)
            screen.blit(s, (min(start[0], end[0]), min(start[1], end[1])))
        
        thickness = max(4, CELL - i // 2)
        pygame.draw.line(screen, color, 
                        (start[0] + CELL//2, start[1] + CELL//2),
                        (end[0] + CELL//2, end[1] + CELL//2), 
                        thickness)
    
    # Kuyruk
    if len(snake) > 2:
        tail = snake[-1]
        tail_wave = int(math.sin(time.time() * 5) * 3)
        pygame.draw.circle(screen, color, 
                          (tail[0] + CELL//2 + tail_wave, tail[1] + CELL//2), 
                          4)
    
    # Kafa
    head = snake[0]
    head_x, head_y = head
    
    if direction == (CELL, 0) or direction == (-CELL, 0):
        pygame.draw.ellipse(screen, color, (head_x + 2, head_y + 4, CELL - 4, CELL - 8))
    else:
        pygame.draw.ellipse(screen, color, (head_x + 4, head_y + 2, CELL - 8, CELL - 4))
    
    # Göz
    eye_size = 5 if not blink else 1
    
    if closest_food:
        dx = closest_food[0] - head[0]
        dy = closest_food[1] - head[1]
        eye_offset_x = 2 if dx > 0 else -2 if dx < 0 else 0
        eye_offset_y = 2 if dy > 0 else -2 if dy < 0 else 0
    else:
        eye_offset_x = 0
        eye_offset_y = 0
    
    if direction == (CELL, 0):
        eye1 = (head_x + 13 + eye_offset_x, head_y + 6 + eye_offset_y)
        eye2 = (head_x + 13 + eye_offset_x, head_y + 12 + eye_offset_y)
        tongue_start = (head_x + CELL, head_y + CELL//2)
        tongue_dir = (15, 0)
    elif direction == (-CELL, 0):
        eye1 = (head_x + 3 + eye_offset_x, head_y + 6 + eye_offset_y)
        eye2 = (head_x + 3 + eye_offset_x, head_y + 12 + eye_offset_y)
        tongue_start = (head_x, head_y + CELL//2)
        tongue_dir = (-15, 0)
    elif direction == (0, -CELL):
        eye1 = (head_x + 6 + eye_offset_x, head_y + 3 + eye_offset_y)
        eye2 = (head_x + 12 + eye_offset_x, head_y + 3 + eye_offset_y)
        tongue_start = (head_x + CELL//2, head_y)
        tongue_dir = (0, -15)
    else:
        eye1 = (head_x + 6 + eye_offset_x, head_y + 13 + eye_offset_y)
        eye2 = (head_x + 12 + eye_offset_x, head_y + 13 + eye_offset_y)
        tongue_start = (head_x + CELL//2, head_y + CELL)
        tongue_dir = (0, 15)
    
    pygame.draw.ellipse(screen, BLACK, (eye1[0], eye1[1], 4, eye_size))
    pygame.draw.ellipse(screen, BLACK, (eye2[0], eye2[1], 4, eye_size))
    
    # Dil
    if tongue_out > 0:
        progress = min(1.0, tongue_out / 1.75)
        if tongue_out > 1.75:
            progress = 1.0 - min(1.0, (tongue_out - 1.75) / 1.75)
        tongue_end = (tongue_start[0] + tongue_dir[0] * progress,
                     tongue_start[1] + tongue_dir[1] * progress)
        pygame.draw.line(screen, RED, tongue_start, tongue_end, 2)

def draw_powerup_icon(x, y, ptype, color, pulse, remaining_time):
    """Power-up ikon"""
    glow = int(pulse)
    pygame.draw.rect(screen, color, (x - glow, y - glow, CELL + glow*2, CELL + glow*2), 2)
    
    pygame.draw.rect(screen, color, (x, y, CELL, CELL))
    pygame.draw.rect(screen, WHITE, (x, y, CELL, CELL), 2)
    
    if ptype == "ghost":
        draw_text("H", (x + 5, y + 2), WHITE, FONT_SMALL)
        pygame.draw.circle(screen, WHITE, (x + CELL//2, y + CELL//2), 4, 1)
    elif ptype == "magnet":
        draw_text("M", (x + 5, y + 2), WHITE, FONT_SMALL)
        pygame.draw.rect(screen, WHITE, (x + 4, y + 8, 3, 8), 1)
        pygame.draw.rect(screen, WHITE, (x + 12, y + 8, 3, 8), 1)
    elif ptype == "tail_cut":
        draw_text("K", (x + 5, y + 2), WHITE, FONT_SMALL)
        pygame.draw.line(screen, WHITE, (x + 5, y + 10), (x + 15, y + 14), 2)
    elif ptype == "double":
        draw_text("2X", (x + 2, y + 4), WHITE, FONT_SMALL)
    elif ptype == "wall":
        draw_text("D", (x + 5, y + 2), WHITE, FONT_SMALL)
        pygame.draw.rect(screen, WHITE, (x + 6, y + 10, 8, 6), 1)
    elif ptype == "shield":
        draw_text("K", (x + 5, y + 2), WHITE, FONT_SMALL)
        pygame.draw.polygon(screen, WHITE, [(x + CELL//2, y + 8), 
                                            (x + 4, y + 14), 
                                            (x + CELL - 4, y + 14)], 1)
    elif ptype == "stealth":
        draw_text("G", (x + 5, y + 2), WHITE, FONT_SMALL)
        pygame.draw.circle(screen, WHITE, (x + CELL//2, y + 12), 3, 1)
    elif ptype == "golden":
        draw_text("A", (x + 5, y + 2), WHITE, FONT_SMALL)
        pygame.draw.circle(screen, YELLOW, (x + CELL//2, y + CELL//2), 6)
    
    if remaining_time:
        draw_text(f"{int(remaining_time)}s", (x - 5, y - 15), color, FONT_SMALL)

def screen_shake():
    offset_x = random.randint(-5, 5)
    offset_y = random.randint(-5, 5)
    return offset_x, offset_y

def power_selection_screen(score):
    """Power-up seçim"""
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))
    
    draw_text("POWER-UP SEC", (WIDTH//2 - 100, 50), CYAN, FONT_BIG)
    draw_text("Ok tuslari ile sec, ENTER ile onayla", (WIDTH//2 - 140, 100), WHITE, FONT_SMALL)
    
    powers = [
        ("ghost", "Hayalet", TURQUOISE),
        ("magnet", "Miknatıs", PINK),
        ("tail_cut", "Kuyruk Kes", WHITE),
        ("double", "2X Puan", ORANGE),
        ("wall", "Duvar Delen", CYAN),
        ("shield", "Kalkan", BLUE),
        ("stealth", "Gizlenme", GRAY)
    ]
    
    selected = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected = (selected - 1) % len(powers)
                elif event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % len(powers)
                elif event.key == pygame.K_UP:
                    selected = (selected - 3) % len(powers)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 3) % len(powers)
                elif event.key == pygame.K_RETURN:
                    return powers[selected][0]
                elif event.key == pygame.K_ESCAPE:
                    return None
        
        for i, (ptype, name, color) in enumerate(powers):
            col = i % 3
            row = i // 3
            x = WIDTH//2 - 150 + col * 100
            y = 200 + row * 100
            
            if i == selected:
                pygame.draw.rect(screen, YELLOW, (x - 5, y - 5, 60, 80), 3)
            
            draw_powerup_icon(x, y, ptype, color, 0, None)
            draw_text(name, (x - 15, y + 30), color, FONT_SMALL)
        
        pygame.display.flip()
        clock.tick(60)

def fade_out(duration_ms=800):
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill(BLACK)
    steps = 20
    for alpha in range(0, 256, 256 // steps):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(duration_ms // steps)

def pause_screen():
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))
    
    draw_text("DURAKLADI", (WIDTH//2 - 80, HEIGHT//2 - 40), YELLOW, FONT_BIG)
    draw_text("P - Devam", (WIDTH//2 - 50, HEIGHT//2 + 20), WHITE)
    draw_text("ESC - Cikis", (WIDTH//2 - 50, HEIGHT//2 + 50), WHITE)
    pygame.display.flip()
    
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    return False
    return True

def leaderboard_screen(leaderboard, player_score):
    """Skor tablosu + Tebrik"""
    fade_out(800)
    screen.fill(BLACK)
    
    if background:
        screen.blit(background, (0, 0))
    
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))
    
    draw_text("SKOR TABLOSU", (WIDTH//2 - 120, 60), GOLD, FONT_BIG)
    
    # Tebrik mesajı
    player_rank = None
    for i, entry in enumerate(leaderboard):
        if entry["score"] == player_score:
            player_rank = i + 1
            break
    
    if player_rank:
        if player_rank == 1:
            msg = "MUHTEŞEM! 1. OLDUNUZ!"
            color = GOLD
        elif player_rank <= 3:
            msg = f"HARIKA! {player_rank}. OLDUNUZ!"
            color = ORANGE
        elif player_rank <= 5:
            msg = f"GÜZEL! {player_rank}. OLDUNUZ!"
            color = GREEN
        else:
            msg = f"{player_rank}. sıra! Devam edin!"
            color = CYAN
        
        draw_text(msg, (WIDTH//2 - 120, 120), color, FONT)
    
    # Tablo
    y = 180
    draw_text("#  İSİM              SKOR", (WIDTH//2 - 150, y), WHITE, FONT)
    y += 30
    draw_text("=" * 35, (WIDTH//2 - 150, y), GRAY, FONT_SMALL)
    y += 25
    
    for i, entry in enumerate(leaderboard):
        rank_color = GOLD if i == 0 else ORANGE if i < 3 else WHITE
        name = entry["name"][:15]
        score = entry["score"]
        
        # Highlight player
        if entry["score"] == player_score:
            pygame.draw.rect(screen, (50, 50, 50), (WIDTH//2 - 160, y - 3, 320, 22))
        
        draw_text(f"{i+1:2}.  {name:15}  {score:5}", (WIDTH//2 - 150, y), rank_color, FONT_SMALL)
        y += 25
    
    draw_text("R - Tekrar Oyna  |  ESC - Çıkış", (WIDTH//2 - 130, HEIGHT - 60), GREEN, FONT)
    
    pygame.display.flip()
    
    waiting = True
    restart = False
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart = True
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    waiting = False
    
    return restart

def main():
    high_score = load_high_score()
    
    while True:
        # İsim al
        player_name = get_player_name()
        
        # Değişkenler
        snake = [(WIDTH//2, HEIGHT//2)]
        direction = (CELL, 0)
        ghost_trail = []
        food = random_position(snake)
        
        # Power-ups
        golden_food = None
        golden_spawn_time = None
        ghost_powerup = None
        ghost_spawn_time = None
        magnet_powerup = None
        magnet_spawn_time = None
        tail_cut_powerup = None
        tail_cut_spawn_time = None
        double_powerup = None
        double_spawn_time = None
        wall_powerup = None
        wall_spawn_time = None
        shield_powerup = None
        shield_spawn_time = None
        stealth_powerup = None
        stealth_spawn_time = None
        
        # Aktif
        ghost_active = False
        ghost_end = 0
        magnet_active = False
        magnet_end = 0
        double_active = False
        double_end = 0
        wall_active = False
        wall_end = 0
        wall_in_wall = False
        shield_active = False
        shield_end = 0
        stealth_active = False
        stealth_end = 0
        special_powerup_active = False
        special_powerup_end = 0
        special_powerup_type = None
        
        # Engeller
        static_obstacles = []
        monsters = []
        fireballs = []
        
        # İstatistik
        score = 0
        speed = SNAKE_SPEED
        base_speed = SNAKE_SPEED
        distance = 0
        normal_foods_eaten = 0
        golden_foods_eaten = 0
        powerup_foods_eaten = 0
        last_food_time = 0
        last_m_press = 0
        start_time = time.time()
        
        # Yılan rengi
        snake_color_index = 0
        snake_color = SNAKE_COLORS[snake_color_index]
        
        # Görsel
        particles = []
        pulse = 0
        blink_timer = 0
        tongue_timer = 0
        tongue_out = 0
        
        # 60 FPS için
        move_accumulator = 0
        move_interval = 1.0 / speed
        
        running = True
        
        while running:
            dt = clock.tick(TARGET_FPS) / 1000.0
            current_time = time.time()
            time_played = current_time - start_time
            fps = int(clock.get_fps())
            
            pulse = (pulse + 0.3) % 6
            
            # Göz & dil
            blink_timer += dt
            blink = (blink_timer % 3.5) < 0.1
            
            tongue_timer += dt
            if tongue_timer >= 3.5:
                tongue_timer = 0
                tongue_out = 3.5
            if tongue_out > 0:
                tongue_out -= dt
            
            # Engeller (15. puan)
            if score >= 15 and len(static_obstacles) == 0:
                for _ in range(8):
                    obs_x = random.randint(5, (WIDTH - CELL) // CELL - 5) * CELL
                    obs_y = random.randint((UI_HEIGHT // CELL) + 5, (HEIGHT // CELL) - 5) * CELL
                    obs = (obs_x, obs_y)
                    if obs not in snake and obs != food:
                        static_obstacles.append(obs)
            
            # Yaratıklar (35. puan)
            if score >= 35 and len(monsters) == 0:
                for _ in range(3):
                    monsters.append(Monster(score))
            
            # Power-up spawn
            if golden_food is None and random.randint(1, 600) == 1:
                golden_food = random_position(snake + [food] + static_obstacles)
                golden_spawn_time = current_time
            
            if ghost_powerup is None and score >= 10 and random.randint(1, 900) == 1:
                ghost_powerup = random_position(snake + [food] + static_obstacles)
                ghost_spawn_time = current_time
            
            if magnet_powerup is None and score >= 10 and random.randint(1, 900) == 1:
                magnet_powerup = random_position(snake + [food] + static_obstacles)
                magnet_spawn_time = current_time
            
            if tail_cut_powerup is None and score >= 10 and random.randint(1, 1200) == 1:
                tail_cut_powerup = random_position(snake + [food] + static_obstacles)
                tail_cut_spawn_time = current_time
            
            if double_powerup is None and score >= 10 and random.randint(1, 850) == 1:
                double_powerup = random_position(snake + [food] + static_obstacles)
                double_spawn_time = current_time
            
            if wall_powerup is None and score >= 10 and random.randint(1, 900) == 1:
                wall_powerup = random_position(snake + [food] + static_obstacles)
                wall_spawn_time = current_time
            
            if shield_powerup is None and len(monsters) > 0 and random.randint(1, 800) == 1:
                shield_powerup = random_position(snake + [food] + static_obstacles)
                shield_spawn_time = current_time
            
            if stealth_powerup is None and len(monsters) > 0 and random.randint(1, 900) == 1:
                stealth_powerup = random_position(snake + [food] + static_obstacles)
                stealth_spawn_time = current_time
            
            # 5 sn kontrol
            if golden_food and (current_time - golden_spawn_time) > 5:
                golden_food = None
            if ghost_powerup and (current_time - ghost_spawn_time) > 5:
                ghost_powerup = None
            if magnet_powerup and (current_time - magnet_spawn_time) > 5:
                magnet_powerup = None
            if tail_cut_powerup and (current_time - tail_cut_spawn_time) > 5:
                tail_cut_powerup = None
            if double_powerup and (current_time - double_spawn_time) > 5:
                double_powerup = None
            if wall_powerup and (current_time - wall_spawn_time) > 5:
                wall_powerup = None
            if shield_powerup and (current_time - shield_spawn_time) > 5:
                shield_powerup = None
            if stealth_powerup and (current_time - stealth_spawn_time) > 5:
                stealth_powerup = None
            
            # Aktif kontrol
            if ghost_active and current_time > ghost_end:
                ghost_active = False
            if magnet_active and current_time > magnet_end:
                magnet_active = False
            if double_active and current_time > double_end:
                double_active = False
            if wall_active and current_time > wall_end:
                if not wall_in_wall:
                    wall_active = False
            if shield_active and current_time > shield_end:
                shield_active = False
            if stealth_active and current_time > stealth_end:
                stealth_active = False
            if special_powerup_active and current_time > special_powerup_end:
                special_powerup_active = False
                special_powerup_type = None
            
            # Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != (0, CELL):
                        direction = (0, -CELL)
                    elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                        direction = (0, CELL)
                    elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                        direction = (-CELL, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                        direction = (CELL, 0)
                    elif event.key == pygame.K_p:
                        if not pause_screen():
                            running = False
                    elif event.key == pygame.K_m:
                        if score >= 30 and (current_time - last_m_press) > 30:
                            selected = power_selection_screen(score)
                            if selected:
                                special_powerup_active = True
                                special_powerup_end = current_time + 15
                                special_powerup_type = selected
                                last_m_press = current_time
                                
                                if selected == "ghost":
                                    ghost_active = True
                                    ghost_end = current_time + 15
                                elif selected == "magnet":
                                    magnet_active = True
                                    magnet_end = current_time + 15
                                elif selected == "wall":
                                    wall_active = True
                                    wall_end = current_time + 15
                                elif selected == "shield":
                                    shield_active = True
                                    shield_end = current_time + 15
                                elif selected == "stealth":
                                    stealth_active = True
                                    stealth_end = current_time + 15
                                elif selected == "double":
                                    double_active = True
                                    double_end = current_time + 15
                                elif selected == "tail_cut":
                                    if len(snake) > 3:
                                        snake = snake[:max(1, len(snake) - 3)]
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            # Hareket (60 FPS smooth)
            move_accumulator += dt
            move_interval = 1.0 / speed
            
            if move_accumulator >= move_interval:
                move_accumulator -= move_interval
                
                head_x, head_y = snake[0]
                dx, dy = direction
                new_head = (head_x + dx, head_y + dy)
                
                # Duvar delen/kalkan wrap
                if wall_active or shield_active:
                    wall_in_wall = False
                    if new_head[0] < 0:
                        new_head = (WIDTH - CELL, new_head[1])
                        wall_in_wall = True
                    elif new_head[0] >= WIDTH:
                        new_head = (0, new_head[1])
                        wall_in_wall = True
                    if new_head[1] < 0:
                        new_head = (new_head[0], HEIGHT - CELL)
                        wall_in_wall = True
                    elif new_head[1] >= HEIGHT:
                        new_head = (new_head[0], 0)
                        wall_in_wall = True
                else:
                    if (new_head[0] < 0 or new_head[0] >= WIDTH or
                       new_head[1] < 0 or new_head[1] >= HEIGHT):
                        play_sound(olum_sesi)
                        running = False
                        continue
                
                # Kendine çarpma
                if not ghost_active and new_head in snake:
                    play_sound(olum_sesi)
                    running = False
                    continue
                
                # Engel
                if not ghost_active and not shield_active and new_head in static_obstacles:
                    play_sound(olum_sesi)
                    running = False
                    continue
                
                # Yaratık
                if not ghost_active and not stealth_active:
                    for mon in monsters:
                        if (new_head[0] >= mon.x and new_head[0] < mon.x + CELL and
                            new_head[1] >= mon.y and new_head[1] < mon.y + CELL):
                            play_sound(olum_sesi)
                            running = False
                            break
                
                if not running:
                    continue
                
                snake.insert(0, new_head)
                distance += 1
                
                # Ghost trail
                ghost_trail.append(new_head)
                if len(ghost_trail) > 15:
                    ghost_trail.pop(0)
                
                # Mıknatıs animasyonlu
                if magnet_active:
                    all_foods = []
                    if food: all_foods.append(('food', food))
                    if golden_food: all_foods.append(('golden', golden_food))
                    if ghost_powerup: all_foods.append(('ghost', ghost_powerup))
                    if magnet_powerup: all_foods.append(('magnet', magnet_powerup))
                    if tail_cut_powerup: all_foods.append(('tail', tail_cut_powerup))
                    if double_powerup: all_foods.append(('double', double_powerup))
                    if wall_powerup: all_foods.append(('wall', wall_powerup))
                    if shield_powerup: all_foods.append(('shield', shield_powerup))
                    if stealth_powerup: all_foods.append(('stealth', stealth_powerup))
                    
                    for fname, fpos in all_foods:
                        dist = math.sqrt((fpos[0]-new_head[0])**2 + (fpos[1]-new_head[1])**2)
                        if dist <= CELL * 3 and dist > CELL:
                            dx = new_head[0] - fpos[0]
                            dy = new_head[1] - fpos[1]
                            pull_speed = 3
                            new_x = fpos[0] + int(dx / dist * pull_speed)
                            new_y = fpos[1] + int(dy / dist * pull_speed)
                            new_pos = (new_x, new_y)
                            
                            if fname == 'food': food = new_pos
                            elif fname == 'golden': golden_food = new_pos
                            elif fname == 'ghost': ghost_powerup = new_pos
                            elif fname == 'magnet': magnet_powerup = new_pos
                            elif fname == 'tail': tail_cut_powerup = new_pos
                            elif fname == 'double': double_powerup = new_pos
                            elif fname == 'wall': wall_powerup = new_pos
                            elif fname == 'shield': shield_powerup = new_pos
                            elif fname == 'stealth': stealth_powerup = new_pos
                
                # Yem çarpışma
                ate = False
                head_rect = pygame.Rect(new_head[0], new_head[1], CELL, CELL)
                
                if food:
                    food_rect = pygame.Rect(food[0], food[1], CELL, CELL)
                    if head_rect.colliderect(food_rect):
                        pts = 2 if double_active else 1
                        score += pts
                        normal_foods_eaten += 1
                        ate = True
                        play_sound(yem_sesi)
                        for _ in range(15):
                            particles.append(Particle(food[0] + CELL//2, food[1] + CELL//2, RED))
                        food = random_position(snake + static_obstacles)
                        if score % 5 == 0:
                            if base_speed < 25:
                                base_speed += 1
                                speed = base_speed
                            # Renk değişimi
                            snake_color_index = (snake_color_index + 1) % len(SNAKE_COLORS)
                            snake_color = SNAKE_COLORS[snake_color_index]
                        screen_shake()
                
                if not ate and golden_food:
                    golden_rect = pygame.Rect(golden_food[0], golden_food[1], CELL, CELL)
                    if head_rect.colliderect(golden_rect):
                        pts = 20 if double_active else 10
                        score += pts
                        golden_foods_eaten += 1
                        ate = True
                        play_sound(yem_sesi)
                        for _ in range(25):
                            particles.append(Particle(golden_food[0] + CELL//2, golden_food[1] + CELL//2, GOLD))
                        golden_food = None
                        screen_shake()
                
                if not ate and ghost_powerup:
                    ghost_rect = pygame.Rect(ghost_powerup[0], ghost_powerup[1], CELL, CELL)
                    if head_rect.colliderect(ghost_rect):
                        ghost_active = True
                        ghost_end = current_time + 10
                        powerup_foods_eaten += 1
                        ate = True
                        play_sound(yem_sesi)
                        for _ in range(20):
                            particles.append(Particle(ghost_powerup[0] + CELL//2, ghost_powerup[1] + CELL//2, TURQUOISE))
                        ghost_powerup = None
                
                if not ate and magnet_powerup:
                    magnet_rect = pygame.Rect(magnet_powerup[0], magnet_powerup[1], CELL, CELL)
                    if head_rect.colliderect(magnet_rect):
                        magnet_active = True
                        magnet_end = current_time + 10
                        powerup_foods_eaten += 1
                        ate = True
                        play_sound(yem_sesi)
                        for _ in range(20):
                            particles.append(Particle(magnet_powerup[0] + CELL//2, magnet_powerup[1] + CELL//2, PINK))
                        magnet_powerup = None
                
                if not ate and tail_cut_powerup:
                    tail_rect = pygame.Rect(tail_cut_powerup[0], tail_cut_powerup[1], CELL, CELL)
                    if head_rect.colliderect(tail_rect):
                        if len(snake) > 3:
                            snake = snake[:max(1, len(snake) - 3)]
                        powerup_foods_eaten += 1
                        ate = True
                        play_sound(yem_sesi)
                        for _ in range(20):
                            particles.append(Particle(tail_cut_powerup[0] + CELL//2, tail_cut_powerup[1] + CELL//2, WHITE))
                        tail_cut_powerup = None
                
                if not ate and double_powerup:
                    double_rect = pygame.Rect(double_powerup[0], double_powerup[1], CELL, CELL)
                    if head_rect.colliderect(double_rect):
                        double_active = True
                        double_end = current_time + 13
                        powerup_foods_eaten += 1
                        ate = True
                        play_sound(yem_sesi)
                        for _ in range(20):
                            particles.append(Particle(double_powerup[0] + CELL//2, double_powerup[1] + CELL//2, ORANGE))
                        double_powerup = None
                
                if not ate and wall_powerup:
                    wall_rect = pygame.Rect(wall_powerup[0], wall_powerup[1], CELL, CELL)
                    if head_rect.colliderect(wall_rect):
                        wall_active = True
                        wall_end = current_time + 15
                        powerup_foods_eaten += 1
                        ate = True
                        play_sound(yem_sesi)
                        for _ in range(20):
                            particles.append(Particle(wall_powerup[0] + CELL//2, wall_powerup[1] + CELL//2, CYAN))
                        wall_powerup = None
                
                if not ate and shield_powerup:
                    shield_rect = pygame.Rect(shield_powerup[0], shield_powerup[1], CELL, CELL)
                    if head_rect.colliderect(shield_rect):
                        shield_active = True
                        shield_end = current_time + 10
                        powerup_foods_eaten += 1
                        ate = True
                        play_sound(yem_sesi)
                        for _ in range(20):
                            particles.append(Particle(shield_powerup[0] + CELL//2, shield_powerup[1] + CELL//2, BLUE))
                        shield_powerup = None
                
                if not ate and stealth_powerup:
                    stealth_rect = pygame.Rect(stealth_powerup[0], stealth_powerup[1], CELL, CELL)
                    if head_rect.colliderect(stealth_rect):
                        stealth_active = True
                        stealth_end = current_time + 10
                        powerup_foods_eaten += 1
                        ate = True
                        play_sound(yem_sesi)
                        for _ in range(20):
                            particles.append(Particle(stealth_powerup[0] + CELL//2, stealth_powerup[1] + CELL//2, GRAY))
                        stealth_powerup = None
                
                if not ate:
                    snake.pop()
                
                # Double ses
                if ate:
                    if current_time - last_food_time < 2:
                        play_sound(double_sesi)
                    last_food_time = current_time
            
            # Yaratıklar
            for mon in monsters:
                mon.update(snake[0], score, dt)
                
                if not stealth_active and mon.can_fire(score):
                    fireballs.append(mon.fire(snake[0][0], snake[0][1]))
            
            # Ateş
            for fb in fireballs[:]:
                fb.update()
                if not fb.active:
                    fireballs.remove(fb)
                    continue
                
                if not ghost_active:
                    for seg in snake[:]:
                        if (abs(fb.x - seg[0] - CELL//2) < CELL and 
                            abs(fb.y - seg[1] - CELL//2) < CELL):
                            if seg in snake:
                                snake.remove(seg)
                                for _ in range(10):
                                    particles.append(Particle(seg[0], seg[1], ORANGE))
                                fireballs.remove(fb)
                                if len(snake) == 0:
                                    running = False
                                break
            
            # Parçacık
            particles = [p for p in particles if p.life > 0]
            for p in particles:
                p.update()
            
            # ÇİZİM
            screen.fill(BLACK)
            if background:
                screen.blit(background, (0, 0))
            
            # Ghost trail
            for i, pos in enumerate(ghost_trail):
                alpha = int(80 * (i / len(ghost_trail)))
                s = pygame.Surface((CELL, CELL))
                s.set_alpha(alpha)
                s.fill(snake_color)
                screen.blit(s, pos)
            
            # Engel
            for obs in static_obstacles:
                pygame.draw.rect(screen, GRAY, (obs[0], obs[1], CELL, CELL))
                pygame.draw.rect(screen, WHITE, (obs[0], obs[1], CELL, CELL), 2)
            
            # Yaratık
            for mon in monsters:
                mon.draw(screen, pulse)
            
            # Ateş
            for fb in fireballs:
                fb.draw(screen)
            
            # Yılan
            closest = find_closest_food(snake[0], [food] + ([golden_food] if golden_food else []))
            in_ui_area = snake[0][1] < UI_HEIGHT
            
            draw_snake_smooth(snake, direction, ghost_active, shield_active, stealth_active, 
                            in_ui_area, blink, tongue_out, closest, dt, snake_color)
            
            # Yemler
            draw_apple(food[0], food[1])
            
            if golden_food:
                remaining = 5 - (current_time - golden_spawn_time)
                draw_powerup_icon(golden_food[0], golden_food[1], "golden", GOLD, pulse, remaining)
            
            if ghost_powerup:
                remaining = 5 - (current_time - ghost_spawn_time)
                draw_powerup_icon(ghost_powerup[0], ghost_powerup[1], "ghost", TURQUOISE, pulse, remaining)
            
            if magnet_powerup:
                remaining = 5 - (current_time - magnet_spawn_time)
                draw_powerup_icon(magnet_powerup[0], magnet_powerup[1], "magnet", PINK, pulse, remaining)
            
            if tail_cut_powerup:
                remaining = 5 - (current_time - tail_cut_spawn_time)
                draw_powerup_icon(tail_cut_powerup[0], tail_cut_powerup[1], "tail_cut", WHITE, pulse, remaining)
            
            if double_powerup:
                remaining = 5 - (current_time - double_spawn_time)
                draw_powerup_icon(double_powerup[0], double_powerup[1], "double", ORANGE, pulse, remaining)
            
            if wall_powerup:
                remaining = 5 - (current_time - wall_spawn_time)
                draw_powerup_icon(wall_powerup[0], wall_powerup[1], "wall", CYAN, pulse, remaining)
            
            if shield_powerup:
                remaining = 5 - (current_time - shield_spawn_time)
                draw_powerup_icon(shield_powerup[0], shield_powerup[1], "shield", BLUE, pulse, remaining)
            
            if stealth_powerup:
                remaining = 5 - (current_time - stealth_spawn_time)
                draw_powerup_icon(stealth_powerup[0], stealth_powerup[1], "stealth", GRAY, pulse, remaining)
            
            # Parçacık
            for p in particles:
                p.draw(screen)
            
            # UI - YENİ DÜZEN
            panel = pygame.Surface((WIDTH, UI_HEIGHT))
            panel.set_alpha(150)
            panel.fill(BLACK)
            screen.blit(panel, (0, 0))
            
            # Sol üst
            draw_text(f"FPS: {fps}", (10, 8), GREEN, FONT_TINY)
            draw_text(f"Skor: {score}", (10, 25), WHITE, FONT)
            draw_text(f"Rekor: {high_score}", (10, 45), YELLOW, FONT_SMALL)
            draw_text(f"Hiz: {speed}", (10, 62), ORANGE, FONT_SMALL)
            draw_text(f"Mesafe: {distance//50}m", (10, 79), GREEN, FONT_SMALL)
            
            # Orta üst - OKUL + POWER-UP AÇIKLAMA
            draw_text("Denizli Is Adamlari MTAL", (WIDTH//2 - 110, 8), GREEN, FONT_SMALL)
            draw_text("H:Hayalet(Turkuaz) M:Miknatıs(Pembe) K:Kuyruk(Beyaz)", (WIDTH//2 - 220, 28), GRAY, FONT_TINY)
            draw_text("2X:Puan(Turuncu) D:Duvar(Mavi) K:Kalkan(Mavi) G:Gizlenme(Gri) A:Altin(Sari)", (WIDTH//2 - 270, 42), GRAY, FONT_TINY)
            
            # Sağ üst - Aktif power-up'lar
            px = WIDTH - 200
            py = 8
            draw_text("AKTIF GUCLER:", (px, py), CYAN, FONT_TINY)
            py += 15
            if ghost_active:
                draw_text(f"Hayalet: {int(ghost_end - current_time)}s", (px, py), TURQUOISE, FONT_TINY)
                py += 12
            if magnet_active:
                draw_text(f"Miknatıs: {int(magnet_end - current_time)}s", (px, py), PINK, FONT_TINY)
                py += 12
            if double_active:
                draw_text(f"2X Puan: {int(double_end - current_time)}s", (px, py), ORANGE, FONT_TINY)
                py += 12
            if wall_active:
                draw_text(f"Duvar: {int(wall_end - current_time)}s", (px, py), CYAN, FONT_TINY)
                py += 12
            if shield_active:
                draw_text(f"Kalkan: {int(shield_end - current_time)}s", (px, py), BLUE, FONT_TINY)
                py += 12
            if stealth_active:
                draw_text(f"Gizli: {int(stealth_end - current_time)}s", (px, py), GRAY, FONT_TINY)
                py += 12
            
            if score >= 30:
                draw_text(f"M tuşu: {max(0, int(30 - (current_time - last_m_press)))}s", 
                         (WIDTH - 200, 85), YELLOW, FONT_TINY)
            
            draw_text(f"P-Duraklat | Oyuncu: {player_name}", (WIDTH//2 - 120, 58), GRAY, FONT_TINY)
            
            pygame.display.flip()
        
        # Oyun bitti
        if score > high_score:
            high_score = score
            save_high_score(high_score)
        
        # Skor tablosuna ekle
        leaderboard = add_to_leaderboard(player_name, score)
        
        # Skor tablosu + tebrik
        restart = leaderboard_screen(leaderboard, score)
        
        if not restart:
            break
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
