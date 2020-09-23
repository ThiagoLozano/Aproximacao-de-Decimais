class Aproximacao:
    def __init__(self):
        while True:
            # Valida o dado de entrada.
            try:
                self.decimal = float(input('Digite um valor entre 0 e 1: '))
                if self.decimal <= 0 or self.decimal >= 1:
                    print("Erro: Entrada de valor incorreto. Tente Novamente!\n")
                else:
                    self.Quantidade_bits()
                    break
            except ValueError:
                print("Erro: Tipo de Dado inválido\n")

    @staticmethod
    # Calcula a porcentagem do erro de aproximação.
    def Err(nd, no):
        err = (nd - no) / nd
        if err < 0:
            err = err * (-1)
        print("Err = {:.2f}%".format((err * 100)))

    # Converte o valor binário aproximado pra um decimal aproximado.
    def Converter_Binario(self, bn):
        dc = []
        # Converte o Binário em um Decimal com Vírgulas.
        for i, v in enumerate(bn):
            if v == 1:
                # Pega os valores exponenciais correspondentes de cada posição
                dc.append(2 ** -(i + 1))
        # Faz a soma total dos expoentes.
        soma = sum(dc)
        # Retorna a soma de cada posição.
        print(' ({})10'.format(soma), end=' ')
        self.Err(self.decimal, soma)

    # Gera os valores binários com base no tamanho de bits.
    def Calcular(self, vd, b):
        vb = []
        # Faz a multiplicação até gerar os valores binários.
        for c in range(b):
            vd * 2
            if int(vd) == 1:
                vd = vd - 1
            vd = vd * 2
            vb.append(int(vd))
        print('=' * 40)

        print('APROXIMAÇÕES\n')
        print("A Menor: ", end='')
        v = ''
        for c in vb:
            v += str(c)
        # Mostra o valor aproximado em binário.
        print('({})2'.format(v), end='')
        self.Converter_Binario(vb)

    # Quantidade de Bits que de precisão.
    def Quantidade_bits(self):
        print('=' * 40)
        while True:
            # Valida a escolha do usuário.
            try:
                bits = int(input("Escolha um quantidade de bits(5 até 12): "))
                if bits < 5 or bits > 12:
                    print("Erro: Insira apenas valores inteiros entre 5 e 12.\n")
                else:
                    self.Calcular(self.decimal, bits)
                    break
            except ValueError:
                print("Erro: Tipo de dado inválido\n")


usuario = Aproximacao()
