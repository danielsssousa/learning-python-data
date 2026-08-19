# Em Python, a biblioteca padrão para manipulação de pacotes de rede em baixo nível é a Scapy. Ela nos permite construir e enviar pacotes ARP facilmente.
import json
import os
import sys
from scapy.all import ARP, Ether, srp

def varrer_rede(ip_rede):
    
    """
    Envia pacotes ARP para a rede e retorna uma lista de dicionários 
    com os IPs e MACs encontrados.
    """
    # Cria o pacote ARP solicitando o ip da rede:
    
    pacote_arp = ARP(pdst=ip_rede) 
    
    # Cria o pacote ethernet para o broadcast   
    
    pacote_ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Junta os dois pacotes
    
    pacote_completo = pacote_ether / pacote_arp
    
    #  Envia o pacote e aguarda a resposta (srp = Send and Receive Packets at Layer 2)
    # timeout=2 define o tempo limite de espera; verbose=0 silencia a saída padrão do Scapy
    
    resultados, _ = srp(pacote_completo, timeout=2, verbose=0)
    
    dispositivos = []
    
    # Processa as respostas recebidas
    
    for enviado, recebido in resultados:
        dispositivos.append({
            'ip': recebido.psrc,
            'mac': recebido.hwsrc
        })
        
    return dispositivos
    
    
def carregar_lista_branca(caminho_arquivo='lista_branca.json'):
    if not os.path.exists(caminho_arquivo):
        # Se o arquivo não existir, retorna um dicionário vazio
        return {}
    
    with open(caminho_arquivo, 'r') as arquivo:
        return json.load(arquivo)
    

def detectar_intrusos(encontrados, lista_branca):
    print('\n---Relatorio de Varredura de rede---')
    
    for dispositivos in encontrados:
        ip_atual = dispositivos['ip']
        mac_atual = dispositivos['mac'].lower()
        
        # Verifica se o IP ou MAC está na whitelist
        
        if ip_atual in lista_branca:
            if lista_branca[ip_atual].lower() == mac_atual:
                print(f"[CONHECIDO] IP: {ip_atual} - MAC: {mac_atual}")
            else:
                print(f"[ALERTA DE SEGURANÇA] IP {ip_atual} mudou de MAC! Esperado: {lista_branca[ip_atual]}, Encontrado: {mac_atual}")
                
        else:
            print(f"[DISPOSITIVO DESCONHECIDO!] IP: {ip_atual} - MAC: {mac_atual} - ATENÇÃO NECESSÁRIA!")
        
def main():
    # Defina a faixa de IP da sua rede local
    ALVO_REDE = '192.168.0.1/24'
    
    print(f"Iniciando varredura na rede: {ALVO_REDE}...")
    
    try:
        # Executa a varredura
        dispositivos = varrer_rede(ALVO_REDE)
        
        # Carrega dispositivos confiaveis
        
        lista_branca = carregar_lista_branca()
        
        # Analisa os resultador
        
        detectar_intrusos(dispositivos, lista_branca)
    except PermissionError:
        print("\n[ERRO] Este script precisa ser executado com privilégios de Administrador (Root).")
        print("Tente rodar novamente usando 'sudo python' (Linux/Mac) ou como Administrador (Windows).")
        
    except Exception as e:
        print(f"\n[ERRO INESPERADO]: {e}")
        
if __name__ == '__main__':
    main()
