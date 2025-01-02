# Orientação a objetos: Paradigma de Programação
# Classes e Objetos 

class Veiculo:
    def movimentar(self):
        print(f'Sou um veiculo e me desloco!')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante # __ representar atributos Privados
        self.__modelo = modelo
        self.__num_registro = None

    # Setter
    def set_num_registro(self, registro):
        self.__num_registro = registro

    # Getter
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, fabricante: {self.__fabricante}./n')

    def get_num_registro(self):
        return self.__num_registro

class Carro(Veiculo):
    # Metodo __init__ será herdado.
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas!')

class Motocicleta(Veiculo):
    # Metodo __init__ será herdado.
    def movimentar(self):
        print(f'Corro muito!')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, Categoria):
        self.__cat = Categoria
        super().__init__(fabricante, modelo)

    def get_categoria(self):
        return self.__cat

    def movimentar(self):
        print(f'Eu voo alto!')

    if __name__ == '__main__':
        meu_veiculo = Veiculo('GM', 'Cadillac Escalade')
        meu_veiculo.movimentar()
        meu_veiculo.get_fabr_modelo()
        meu_veiculo.set_num_registro('490321-1')
        print(f'Registro: {meu_veiculo.get_num_registro()}/n')

        meu_carro = Carro('Volkswagen', 'Polo')
        meu_carro.movimentar()
        meu_carro.get_fabr_modelo()

        seu_carro = Carro('Audi', 'A5 Sportback')
        seu_carro.movimentar()
        seu_carro.get_fabr_modelo()

        moto = Motocicleta('Harley Davidson', 'Nightster Special')
        moto.movimentar()
        moto.get_fabr_modelo()

        meu_aviao = Aviao('Boing', '747', 'Comercial')
        meu_aviao.movimentar()
        meu_aviao.get_fabr_modelo()
        print(f'Categoria{meu_aviao.get_categoria()}')





        