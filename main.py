class Aproximacao:
    def __init__(self):
        self.soma = 0
        self.bits = 0
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

    # Quantidade de Bits de precisão.
    def Quantidade_bits(self):
        print('=' * 40)
        while True:
            # Valida a escolha do usuário.
            try:
                self.bits = int(input("Escolha um quantidade de bits(5 até 12): "))
                if self.bits < 5 or self.bits > 12:
                    print("Erro: Insira apenas valores inteiros entre 5 e 12.\n")
                else:
                    self.A_menor(self.decimal, self.bits)
                    break
            except ValueError:
                print("Erro: Tipo de dado inválido\n")

    # Retorna a aproximação a menor.
    def A_menor(self, valor_decimal, bit):
        valor_binario = []
        # Faz a multiplicação até gerar os valores binários.
        for c in range(bit):
            valor_decimal * 2
            if int(valor_decimal) == 1:
                valor_decimal = valor_decimal - 1
            valor_decimal = valor_decimal * 2
            valor_binario.append(int(valor_decimal))
        print('=' * 40)
        print('APROXIMAÇÕES\n')
        print("A Menor: ", end='')
        v = ''
        for c in valor_binario:
            v += str(c)
        # Mostra o valor aproximado em binário.
        print('({})2'.format(v), end='')
        self.Converter_para_Decimal(valor_binario)
        self.A_maior()

    # Retorna a aproximação a maior.
    def A_maior(self):
        """
        Para mostrar o valor Binário de "A maior", preciso somar o Binário
        de "A menor" conforme a quantidade de bits que tiver,
        Ex: 5 bits
        Binário de "A menor" + 00001
        Ex: 7 bits
        Binário de "A menor" + 0000001
        Obs: Só falta apenas esse pedaço.
        """
        print("A Maior: ", end='')
        print('()2'.format(), end='')
        binario = []
        decimal = []
        # Cria o Binário que corresponde ao número de bits para a soma em decimal.
        for c in range(self.bits):
            binario.append(0)
        ultimo = len(binario) - 1
        binario[ultimo] = 1
        # Converte o Binário em Decimal.
        for i, v in enumerate(binario):
            if v == 1:
                decimal.append(2 ** (-i - 1))
        a_menor = self.soma
        decimal.append(a_menor)
        # Soma com o valor de A menor já descoberto.
        soma = sum(decimal)
        print(' ({})10'.format(soma), end=' ')
        self.Erro(self.decimal, soma)

    # Converte os valor binário para de decimal da aproximação a menor.
    def Converter_para_Decimal(self, binario):
        decimal = []
        # Converte o Binário em um Decimal com vírgula.
        for i, v in enumerate(binario):
            if v == 1:
                # Pega os valores exponenciais correspondentes de cada posição
                decimal.append(2 ** -(i + 1))
        # Faz a soma total dos expoentes.
        self.soma = sum(decimal)
        # Retorna a soma de cada posição.
        print(' ({})10'.format(self.soma), end=' ')
        self.Erro(self.decimal, self.soma)

    @staticmethod
    # Calcula a porcentagem do erro de aproximação.
    def Erro(nd, no):
        erro = (nd - no) / nd
        if erro < 0:
            erro = erro * (-1)
        print("Err = {:.2f}%".format(erro * 100))


usuario = Aproximacao()
