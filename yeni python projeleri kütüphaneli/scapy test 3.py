from scapy.all import sniff

def paket_analiz(packet):
    # Sadece IP protokolü olan paketleri göster ki terminal çöplüğe dönmesin
    if packet.haslayer("IP"):
        ip_layer = packet.getlayer("IP")
        print(f"🌐 [IP] {ip_layer.src} ---> {ip_layer.dst} | Protokol: {ip_layer.proto}")

print("--- CYBERIA NETWORK MONITOR V2 ---")
print("Paketler yakalanıyor... Durdurmak için: Ctrl + C")

# Sniff fonksiyonunu en sade haliyle çağırıyoruz
# Eğer Npcap yüklüyse, hiçbir ekstra ayara gerek kalmadan çalışır.
try:
    sniff(prn=paket_analiz, count=15, store=False)
except Exception as e:
    print(f"Kanka hala bir sorun var: {e}")
