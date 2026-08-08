# Incluindo a biblioteca

from scapy import IP, ICMP, send

# Criacao do codigo

pacote_adulterado = IP(scr='10.0.0.99', dts='192.168.1.15') / ICMP

# Enviando o pacote

send(pacote_adulterado)
print('Pacote adulterado enviado com IP de origem falsificado')
