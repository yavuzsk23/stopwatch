import matplotlib.pyplot as plt
import matplotlib.animation as animation
import psutil
import seaborn as sns

# Görsel stil ayarları - Havalı bir görünüm için
sns.set_theme(style="darkgrid")
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['figure.facecolor'] = '#121212'
plt.rcParams['axes.facecolor'] = '#1e1e1e'

# Veri saklamak için listeler (Son 20 veri)
x_data = list(range(20))
y_data = [0] * 20

fig, ax = plt.subplots()
line, = ax.plot(x_data, y_data, color='#00ff00', linewidth=2)

# Grafik sınırlarını ayarla
ax.set_ylim(0, 100)
ax.set_title("CYBERIA CPU REAL-TIME TRACKER", fontsize=14, color='#00ff00')
ax.set_ylabel("Kullanım (%)")
ax.set_xlabel("Zaman (sn)")

def update(frame):
    # Yeni veriyi al
    cpu_usage = psutil.cpu_percent()
    
    # Listeyi güncelle (en eskiyi at, yeniye ekle)
    y_data.pop(0)
    y_data.append(cpu_usage)
    
    # Çizgiyi güncelle
    line.set_ydata(y_data)
    return line,

# 500ms (yarım saniye) aralıklarla güncelle
ani = animation.FuncAnimation(fig, update, interval=500, blit=True)

print("Kanka grafik penceresi açılıyor, hazır ol!")
plt.show()
