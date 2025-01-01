from scapy.all import sniff
wpcap = "Ethernet" 

def packet_callback(packet):
    print(packet.summary())

# Démarrer la capture de paquets  Utilisez le paramètre filter pour capturer uniquement certains types de paquets (par exemple, TCP ou UDP) 
sniff(prn=packet_callback, filter='tcp', count=10)

#Sauvegardez les paquets capturés dans un fichier .pcap
#packets = sniff(count=10)
#wrpcap("captured_packets.pcap", packets)

sniff(iface=wpcap, prn=packet_callback, count=10)