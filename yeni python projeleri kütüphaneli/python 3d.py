from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# --- DÜNYA AYARLARI ---
Sky(texture='sky_sunset')
player = FirstPersonController(y=5, speed=10, jump_height=3)
player.cursor.visible = True # Ekran ortasındaki imleç

# --- PLATFORMLAR (Bölüm Tasarımı) ---
# Başlangıç platformu
Entity(model='cube', color=color.dark_gray, collider='box', scale=(10, 1, 10), position=(0,0,0))

# Zıplama platformları
platforms = [
    Entity(model='cube', color=color.azure, collider='box', scale=(3, 1, 3), position=(0, 2, 10)),
    Entity(model='cube', color=color.azure, collider='box', scale=(3, 1, 3), position=(5, 4, 18)),
    Entity(model='cube', color=color.azure, collider='box', scale=(3, 1, 3), position=(-5, 6, 25))
]

# Hareketli Engel (Dönen çubuk)
obstacle = Entity(model='cube', color=color.red, collider='box', scale=(8, 1, 1), position=(0, 8, 35))

# Bitiş Noktası
finish_line = Entity(model='sphere', color=color.green, collider='box', scale=3, position=(0, 10, 50))

# --- OYUN MANTIĞI ---
def update():
    # Engeli döndür
    obstacle.rotation_y += 100 * time.dt
    
    # Aşağı düşersen yanarsın (Reset sistemi)
    if player.y < -10:
        player.position = (0, 5, 0)
        print("Düştün! Tekrar dene.")

    # Bitiş çizgisine ulaştın mı?
    if distance(player, finish_line) < 3:
        print("TEBRİKLER! Bölümü bitirdin.")
        finish_line.color = color.yellow
        # Buraya bir sonraki bölüme geçiş kodu yazılabilir

# Işıklandırma (Daha iyi görünmesi için)
EditorCamera() # Geliştirici kamerası (İstersen sağ tıkla dünyayı izleyebilirsin)

app.run()
