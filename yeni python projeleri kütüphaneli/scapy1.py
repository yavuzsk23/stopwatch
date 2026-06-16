from scapy.all import sniff

def paket_yakala(packet):
    # Yakalanan paketin özetini basıyoruz
    if packet.haslayer("IP"):
        kaynak_ip = packet["IP"].src
        hedef_ip = packet["IP"].dst
        print(f"📡 Paket Yakalandı: {kaynak_ip} -> {hedef_ip}")

print("--- CYBERIA NETWORK SNIFFER BAŞLATILDI ---")
print("Ağdaki trafik izleniyor... (Durdurmak için Ctrl+C)")

# 10 tane paket yakalayıp duracak şekilde ayarladım (count=10)
# Eğer sonsuza kadar sürsün istersen count kısmını sil kanka
sniff(prn=paket_yakala, count=10)
