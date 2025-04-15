def validar_endereco(endereco: list) -> bool:
    """Valida se o endereço IP ou máscara possui 4 octetos entre 0 e 255."""
    if len(endereco) != 4:
        return False
    try:
        for octeto in endereco:
            if not (0 <= int(octeto) <= 255):
                return False
    except ValueError:
        return False
    return True

def calcular_rede_e_broadcast(ip: list, mask: list) -> tuple:
    """Calcula o endereço de rede e o broadcast a partir do IP e máscara."""
    ip_rede = []
    broadcast = []
    for i in range(4):
        ip_rede.append(int(ip[i]) & int(mask[i]))
        broadcast.append((~int(mask[i]) & 0xFF) | ip_rede[i])
    return ip_rede, broadcast

def exibir_resultados(ip: list, mask: list, ip_rede: list, broadcast: list):
    """Exibe os resultados formatados."""
    print('-' * 10, 'Informações', '-' * 10)
    print('IP:        {}.{}.{}.{}'.format(*ip))
    print('Máscara:   {}.{}.{}.{}'.format(*mask))
    print('Rede:      {}.{}.{}.{}'.format(*ip_rede))
    print('Broadcast: {}.{}.{}.{}'.format(*broadcast))
    print('-' * 33)

def main():
    """Função principal."""
    print('\t_____ Redes IP _____')

    ip = input('Entre com o endereço IP (exemplo: 192.168.2.1): ').strip().split('.')
    mask = input('Entre com a máscara de rede (exemplo: 255.255.255.0): ').strip().split('.')

    # Validação
    if not validar_endereco(ip):
        print('Endereço IP inválido! Certifique-se de digitar 4 números entre 0 e 255.')
        return
    if not validar_endereco(mask):
        print('Máscara de rede inválida! Certifique-se de digitar 4 números entre 0 e 255.')
        return

    ip_rede, broadcast = calcular_rede_e_broadcast(ip, mask)
    exibir_resultados(ip, mask, ip_rede, broadcast)

if __name__ == "__main__":
    main()