from scapy.all import sniff, conf, L3RawSocket

# Sürücü hatasını bypass etmek için Layer 3 soketi kullanıyoruz
conf.L3socket = L3RawSocket

def paket_yakala(packet):
    if packet.haslayer("IP"):
        print(f"📡 Paket: {packet['IP'].src} -> {packet['IP'].dst}")

print("--- CYBERIA L3 SNIFFER AKTİF ---")
sniff(prn=paket_yakala, count=10)
