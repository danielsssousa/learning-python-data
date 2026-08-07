import json
import nmap
from datetime import datetime

def criar_scanner_portas(alvo, argumentos='-sV, -T4'):
    scanner = nmap.PortScanner()
    print(f'[*] Iniciando a varredura do alvo {alvo}')
    print(f'[*] Argumentos do nmap {argumentos}')
    
    try:
        scanner.scan(hosts=alvo, arguments=argumentos)
        return scanner
    
    except Exception as e:
        print(f"[!] Erro ao executar o namap: {e}")
        return None
    
def gerar_relatorio(scanner, alvo):
    if not scanner or alvo not in scanner.all_hosts():
        print('[!] Nenhum dado encontrado para gerar o relatorio.')
        return None

    relatorio = {
        'data_execucao': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'alvo': alvo,
        'status_host': scanner[alvo].state(),
        'portas_abertas': []     
    }
        
# Itera sobre os protocolos (tcp/udp) encontrados

    for proto in scanner[alvo].all_protocols():
        portas = scanner[alvo][proto].keys()
        
        for porta in portas:
            dados_porta = scanner[alvo][proto][porta]
            
            #Filtra apenas portas abertas
            
            if dados_porta['state'] == 'open':
                info_porta = {
                    'porta': porta,
                    'protocolo': proto,
                    'estado': dados_porta['state'],
                    'servico': dados_porta.get('name', ''),
                    'produto': dados_porta.get('product', ''),
                    'versao': dados_porta.get('version', '')              
                }
                relatorio['portas_abertas'].append(info_porta)
                
    return relatorio 

def salvar_json(relatorio, nome_arquivo='relatorio_nmap.json'):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(relatorio, f, indent=4, ensure_ascii=False)
    print(f'[+] Relatorio salvo com sucesso em {nome_arquivo}')
    
if __name__ == '__main__':
    
    ALVO = '192.168.0.1'
    #192.168.0.3
    
# EXECUTA O SCANNER
resultado_scan = criar_scanner_portas(ALVO, argumentos='-sV -p 21,22,8080,443,3306')

if resultado_scan:
    relatorio_final = gerar_relatorio(resultado_scan, ALVO)
    
    if relatorio_final:
        print('\n--- RESUMO DA VARREDURA ---')
        print(f'Host: {relatorio_final['alvo']} ({relatorio_final['status_host']})')
        print(f'Total de portas abertas encontradas: {len(relatorio_final['portas_abertas'])}')
        
        for p in relatorio_final['portas_abertas']:
            print(f'-> Porta {p['porta']}/{p['protocolo']} | Servico: {p['servico']} {p['produto']} {p['versao']}')
    
        salvar_json(relatorio_final)


