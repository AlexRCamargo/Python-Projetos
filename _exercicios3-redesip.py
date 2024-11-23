print('\t_____ Redes IP _____')

ip = raw_input('Entre com o endereço IP exemplo: (192.168.2.1): ').split('.')
mask = raw_input('Entre com a máscara de rede exemplo: (255.255.255.0): ').split('.') 

broadcast, ip_rede = [], []

for i in range(len(ip)):
    ip_rede.append(int(ip[i]) & int(mask[i]))   
    broadcast.append((~int(mask[i])&0xff) | int(ip_rede[i]))
    
print('-'*10, 'Informações', '-'*10)
print('IP:        %s.%s.%s.%s' % (ip[0], ip[1], ip[2], ip[3])) 
print('Mask:      %s.%s.%s.%s' % (mask[0], mask[1], mask[2], mask[3]))
print('Rede:      %d.%d.%d.%d' % (ip_rede[0], ip_rede[1], ip_rede[2], ip_rede[3]))
print('Broadcast: %d.%d.%d.%d' % (broadcast[0], broadcast[1], broadcast[2], broadcast[3]))
print('-'*33)

