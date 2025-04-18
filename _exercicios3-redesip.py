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

    ip = input('Entre com o endereço IP (exemplo: 192.168.2.1): ').split('.')
    mask = input('Entre com a máscara de rede (exemplo: 255.255.255.0): ').split('.')

    # Validação simples (não obrigatória, mas profissional)
    if len(ip) != 4 or len(mask) != 4:
        print('IP ou Máscara inválidos.')
        return

    ip_rede, broadcast = calcular_rede_e_broadcast(ip, mask)
    exibir_resultados(ip, mask, ip_rede, broadcast)

if __name__ == "__main__":
    main()

