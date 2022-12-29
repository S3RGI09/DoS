from scapy.all import *

# Dirección IP del servidor de destino
server_ip = '192.168.0.1'

# Número de paquetes a enviar
num_packets = 1000000

# Crear paquetes IP con la dirección del servidor de destino
packets = IP(dst=server_ip)

# Enviar los paquetes al servidor de destino
send(packets, count=num_packets)
