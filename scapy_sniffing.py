# Sniffing de pacotes, e a captura de trafego consiste em interceptar e registrar o trafego que passa por uma interface de rede.

# Abaixo um exemplo bascio de captura de pacotes.

from scapy.all import sniff

def processar_pacotes(pacote):
    print(pacote.summary())
    
# Capturando 12 pacotes

print('[*] Iniciando o Sniffing...')
sniff(count=12, prn=processar_pacotes)

# Colocando um filtro, semelhante ao do Wireshark

sniff(filter='tcp port 80', count=5, prn=processar_pacotes)