import qrcode
from PIL import Image

def gerar_qr_code(dados, nome_arquivo="qr_code.png", logo_path=None):
    """
    Gera um QR Code.

    Args:
        dados: Os dados a serem codificados no QR Code.
        nome_arquivo: O nome do arquivo para salvar o QR Code (padrão: qr_code.png).
        logo_path: O caminho para um arquivo de logo (opcional).
    """

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(dados)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    if logo_path:
        try:
            logo = Image.open(logo_path).convert("RGB")
            tamanho_logo = img.size[0] // 4
            logo = logo.resize((tamanho_logo, tamanho_logo))
            posicao = ((img.size[0] - tamanho_logo) // 2, (img.size[1] - tamanho_logo) // 2)
            img.paste(logo, posicao)
        except FileNotFoundError:
            print(f"Aviso: Logo não encontrado em {logo_path}")
        except Exception as e:
            print(f"Erro ao adicionar logo: {e}")

    img.save(nome_arquivo)
    print(f"QR Code salvo em {nome_arquivo}")

# Exemplo de uso
dados = "https://www.google.com"  # Substitua pelos dados desejados
gerar_qr_code(dados, "meu_qr_code.png", "caminho/para/seu/logo.png")  # Substitua pelo caminho do seu logo ou deixe em branco para None