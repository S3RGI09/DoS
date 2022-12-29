# DoS
### Script creado en Python para hacer ataques DoS.
Este pequeño script programado en Python es mas potente de lo que parece. Este script es un ejemplo de que no te debes fiar de las apariencias, el script cuenta con **9 lineas de codigo**, y, en general, poca programacion, el resultado seria un **programa muy simple**, pero que sea simple no significa que no sea **util y potente**.
El script funciona de la siguiente manera:

```from scapy.all import *```: Esta linea importa la libreria **scapy** que se utiliza para poder comunicarse con otros ordenadores.

```server_ip = 'IP victima'```: En esta linea **se tiene que añadir la IP/DNS victima manualmente**, por eso para manejar bien el script se necesita conocimientos basicos de Python y editores de texto como Nano o Vim.

```num_packets = Nº de paquetes```: En esta linea **se tiene que añadir la cantidad de paquetes que se quiere enviar al host victima**, por eso para manejar bien el script se necesita conocimientos basicos de Python y editores de texto como Nano o Vim.

```packets = IP(dst=server_ip)```: Esta linea sirve para crear los paquetes con los que vas a atacar a la victima.

```send(packets, count=num_packets)```: Esta linea sirve para enviar los paquetes al host victima.

Como puedes ver, son 5 lineas de accion y 4 de informacion ```#``` para que sepas cambiar las cosas y arreglar problemas si es que quieres mejorarlo, en el codigo del script veras algunas lineas con el ```#```,es informacion adicional para que sepas que hace cada linea y si tienes que hacer cambios, te indicaran donde. Cave destacar que el script esta totalmente libre de Licencias, ya que es un programa muy sencillo y es solo la **version beta de otra herramienta DOS que estoy programando** y que prometo publicarla cuando este acabada :)

Tengo que decir que como siempre tu eres el responsable de lo que haces, yo creo estas herramientas educativos y no maliciosos. Te recuerdo que **hacer ataques DOS a un computador de otra persona si su consentimiento es una actividad ilegal y las penas suelen ser muy serias dependiendo de las leyes de tu pais**. Si quieres asumir el riesgo, adelante, pero primero se consciente de lo que vas a hacer y las consecuencias de ello. Lo que haces tu es culpa tuya, no mia, mi script es totalmente legal y tu eres el que recibira las consecuencias.
