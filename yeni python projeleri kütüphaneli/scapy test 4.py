from scapy.all import sniff

# 1. Önce paketi analiz edecek fonksiyonu tanımlıyoruz
def analiz_et(packet):
    # 'packet' değişkeni bu fonksiyonun içinde geçerlidir
    if packet.haslayer("IP"):
        ip_layer = packet.getlayer("IP")
        
        # Eğer UDP paketi ise (senin az önce gördüğün 17 nolu protokol)
        if packet.haslayer("UDP"):
            udp_layer = packet.getlayer("UDP")
            print(f"📡 [UDP] {ip_layer.src}:{udp_layer.sport} ---> {ip_layer.dst}:{udp_layer.dport}")
        
        # Eğer TCP paketi ise (Web siteleri, Discord vb.)
        elif packet.haslayer("TCP"):
            tcp_layer = packet.getlayer("TCP")
            print(f"🔒 [TCP] {ip_layer.src}:{tcp_layer.sport} ---> {ip_layer.dst}:{tcp_layer.dport}")
        
        # Diğerleri
        else:
            print(f"🌐 [IP] {ip_layer.src} ---> {ip_layer.dst} | Proto: {ip_layer.proto}")

print("--- CYBERIA NETWORK MONITOR V3 ---")
print("Ağ dinleniyor... Durdurmak için Ctrl+C")

# 2. Şimdi 'sniff' komutuyla paketleri yakalayıp 'analiz_et' fonksiyonuna yolluyoruz
try:
    sniff(prn=analiz_et, count=20, store=False)
except Exception as e:
    print(f"Hata kanka: {e}")
