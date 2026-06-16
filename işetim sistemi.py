from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# --- 1. MOTOR VE PENCERE AYARLARI ---
app = Ursina()

window.title = "Cyberia 3D OS - Error Free"
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True
window.vsync = True # Kasmayı önleyen asıl ayar bu

# --- 2. GÜVENLİ ZEMİN ---
ground = Entity(
    model='plane', 
    scale=200, 
    texture='white_cube', 
    texture_scale=(100,100), 
    color=color.dark_gray,
    collider='box'
)

# --- 3. UYGULAMA SINIFI ---
class AppIcon(Button):
    def __init__(self, position=(0,1,5), name="App", app_color=color.cyan, info=""):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            scale=(1.5, 1.5, 1.5),
            color=app_color,
            texture='white_cube',
            highlight_color=color.white
        )
        self.name = name
        self.info = info
        self.label = Text(text=self.name, parent=self, y=0.8, scale=5, origin=(0,0))

    def on_click(self):
        output_panel.enabled = True
        output_text.text = f"--- {self.name} ---\n\n{self.info}\n\n[Esc: Kapat]"

# --- 4. UI ELEMANLARI ---
output_panel = Entity(parent=camera.ui, model='quad', scale=(0.7, 0.4), color=color.black90, enabled=False)
output_text = Text(parent=output_panel, text="", scale=1.3, x=-0.4, y=0.3, color=color.lime)

# --- 5. İKONLAR ---
AppIcon(position=(-5, 1, 10), name="Sistem", app_color=color.red, 
        info="Cyberia OS v1.3\nStatus: Ultra Smooth\nEngine: Ursina 3D")
AppIcon(position=(0, 1, 10), name="Dosyalar", app_color=color.azure, 
        info="> Masaustu/Projeler/\n- Minecraft_Clone\n- Space_War")
AppIcon(position=(5, 1, 10), name="Donanim", app_color=color.yellow, 
        info="GPU: RTX 5060\nRAM: 16GB\nOS Architecture: 3D Interface")

# --- 6. OYUNCU (Titreme Karşıtı Ayar) ---
player = FirstPersonController(y=2, origin_y=-0.5)
player.cursor.color = color.lime

# --- 7. KONTROL VE DÜŞME KORUMASI ---
def update():
    if player.y < -4:
        player.position = (0, 2, 0)

def input(key):
    if key == 'tab':
        mouse.locked = not mouse.locked
    if key == 'escape':
        output_panel.enabled = False
    if key == 'q':
        quit()

# Atmosfer
Sky(color=color.black)
for i in range(25):
    Entity(model='cube', color=color.lime, scale=0.03, 
           position=(random.randint(-30,30), random.randint(0,10), random.randint(-30,30)))

app.run()
