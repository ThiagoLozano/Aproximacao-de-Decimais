class Aproximacao:
    def __init__(self):
        self.soma_a_menor = 0
        self.qnt_bits = 0
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
                self.qnt_bits = int(input("Escolha um quantidade de bits(5 até 12): "))
                if self.qnt_bits < 5 or self.qnt_bits > 12:
                    print("Erro: Insira apenas valores inteiros entre 5 e 12.\n")
                else:
                    self.A_Menor(self.decimal, self.qnt_bits)
                    self.A_Maior()
                    break
            except ValueError:
                print("Erro: Tipo de dado inválido\n")

    # Retorna a aproximações A Menor.
    def A_Menor(self, valor_decimal, bit):
        valor_binario = []
        # Faz as multiplicações sucessivas até gerar os valores binários.
        for c in range(bit):
            valor_decimal * 2
            if int(valor_decimal) == 1:
                valor_decimal = valor_decimal - 1
            valor_decimal = valor_decimal * 2
            valor_binario.append(int(valor_decimal))
        print('=' * 40)
        print('APROXIMAÇÕES\n')
        print("\033[36mA Menor: \033[m", end='')
        v = ''
        for c in valor_binario:
            v += str(c)
        # Retorna o valor Binário para a aproximação A Menor.
        print('({})2'.format(v), end='')
        self.Decimal_A_Menor(valor_binario)

    # Retorna o valor Decimal para a aproximação A Menor.
    def Decimal_A_Menor(self, binario):
        decimal = []
        # Converte o Binário em um Decimal com vírgula.
        for i, v in enumerate(binario):
            if v == 1:
                # Pega os valores exponenciais correspondentes de cada posição
                decimal.append(2 ** -(i + 1))
        # Faz a soma total dos expoentes.
        self.soma_a_menor = sum(decimal)
        # Retorna a soma de cada posição.
        print(' ({})10'.format(self.soma_a_menor), end=' ')
        self.Erro(self.decimal, self.soma_a_menor)

    # Retorna as aproximações A Maior.
    def A_Maior(self):
        """ Etapa 1: Gera Binário """
        binario = []
        decimal = []
        # Cria o Binário que corresponde ao número de bits para a soma em decimal.
        for c in range(self.qnt_bits):
            binario.append(0)
        ultimo = len(binario) - 1
        binario[ultimo] = 1

        """ Etapa 2: Converte Binário em Decimal """
        # Converte o Binário em Decimal.
        for i, v in enumerate(binario):
            if v == 1:
                decimal.append(2 ** (-i - 1))
        a_menor = self.soma_a_menor
        decimal.append(a_menor)

        """ Etapa 3: Soma o Decimal 'A Menor' com o Decimal do Binário """
        # Soma com o valor de A menor já descoberto.
        soma = sum(decimal)

        """ Etapa 4: Converte a Soma do Decimal em Binário """
        valor_binario = []
        # Faz as multiplicações sucessivas até gerar os valores binários.
        for c in range(self.qnt_bits):
            soma * 2
            if int(soma) == 1:
                soma = soma - 1
            soma = soma * 2
            valor_binario.append(int(soma))
        print("\033[36mA Maior: \033[m", end='')
        v = ''
        for c in valor_binario:
            v += str(c)
        # Retorna o valor Binário para a aproximação A Maior.
        print('({})2'.format(v), end='')
        self.Decimal_A_Maior()

    # Retorna o valor Decimal para a aproximação A Maior.
    def Decimal_A_Maior(self):
        binario = []
        decimal = []
        # Cria o Binário que corresponde ao número de bits para a soma em decimal.
        for c in range(self.qnt_bits):
            binario.append(0)
        ultimo = len(binario) - 1
        binario[ultimo] = 1
        # Converte o Binário em Decimal.
        for i, v in enumerate(binario):
            if v == 1:
                decimal.append(2 ** (-i - 1))
        a_menor = self.soma_a_menor
        decimal.append(a_menor)
        # Soma com o valor de A menor já descoberto.
        soma = sum(decimal)
        print(' ({})10'.format(soma), end=' ')
        self.Erro(self.decimal, soma)

    # Calcula a porcentagem do erro de aproximação.
    @staticmethod
    def Erro(nd, no):
        erro = (nd - no) / nd
        if erro < 0:
            erro = erro * (-1)
        print("\033[33mErr\033[m = {:.2f}%".format(erro * 100))


usuario = Aproximacao()
