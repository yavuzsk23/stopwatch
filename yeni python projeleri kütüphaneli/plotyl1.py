import plotly.graph_objects as go
import psutil
import time

# Verileri toplayalım (Örnek olarak 5 saniyelik veri)
zamanlar = []
cpu_verileri = []
ram_verileri = []

print("Kanka 5 saniye boyunca sistemini analiz ediyorum, bekle...")

for i in range(5):
    zamanlar.append(time.strftime("%H:%M:%S"))
    cpu_verileri.append(psutil.cpu_percent())
    ram_verileri.append(psutil.virtual_memory().percent)
    time.sleep(1)

# Plotly ile grafik oluşturma
fig = go.Figure()

# CPU Çizgisi
fig.add_trace(go.Scatter(x=zamanlar, y=cpu_verileri, name='CPU Kullanımı (%)',
                         line=dict(color='firebrick', width=4)))

# RAM Çizgisi
fig.add_trace(go.Scatter(x=zamanlar, y=ram_verileri, name='RAM Kullanımı (%)',
                         line=dict(color='royalblue', width=4)))

# Grafik Tasarımı (Cyberia Teması)
fig.update_layout(title='CYBERIA INTERACTIVE MONITOR',
                   xaxis_title='Zaman',
                   yaxis_title='Yüzde (%)',
                   template='plotly_dark')

# Grafiği tarayıcıda aç
fig.show()
