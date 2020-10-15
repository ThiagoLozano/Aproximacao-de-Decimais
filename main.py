class Conversor:
    # Método Construtor.
    def __init__(self):
        self.valor_decimal = 0
        self.quantidade_bits = 0
        self.binario_a_menor = '0.'
        self.decimal_a_menor = 0
        self.binario_a_maior = '0.'
        self.decimal_a_maior = 0
        self.erro_menor = 0
        self.erro_maior = 0

    # Função que recebe o Valor Decimal e a Quantidade de Bits.
    def Set_Valores(self):
        # Valida a entrada do número Real.
        while True:
            try:
                self.valor_decimal = float(input("Digite uma valor real entre 0 e 1: "))
                if self.valor_decimal <= 0 or self.valor_decimal >= 1:
                    print("\n\033[31mErro: Valor incorreto para a operação. Tente Novamente!\033[m")
                else:
                    break
            except ValueError:
                print("\n\033[31mErro: Insira um valor\033[m")

        # Valida a entrada da quantidade de Bits.
        while True:
            try:
                self.quantidade_bits = int(input("Digite a quantidade de bits entre 5 e 12: "))
                if self.quantidade_bits < 5 or self.quantidade_bits > 12:
                    print("\n\033[31mErro: Valor incorreto para a operação. Tente Novamente!\033[m")
                else:
                    break
            except ValueError:
                print("\n\033[31mErro: Insira um valor\033[m")
        self.Binario_a_Menor(self.quantidade_bits, self.valor_decimal)
        self.Decimal_a_Maior()

    # Faz a aproximaçao 'A Menor' em Binário.
    def Binario_a_Menor(self, quant_bits, valor_decimal):
        binario = []
        # Faz as multiplicações sucessivas até gerar os valores binários.
        for c in range(quant_bits):
            valor_decimal * 2
            if int(valor_decimal) == 1:
                valor_decimal = valor_decimal - 1
            valor_decimal = valor_decimal * 2
            binario.append(int(valor_decimal))
        # Passa os valores da lista para uma String única.
        for c in binario:
            self.binario_a_menor += str(c)
        self.Decimal_a_Menor(binario)

    # Faz a conversão para Decimal do valor 'A Menor' que está em Binário.
    def Decimal_a_Menor(self, lista_binario):
        decimal = []
        # Converte o Binário em um Decimal com vírgula.
        for i, v in enumerate(lista_binario):
            if v == 1:
                # Pega os valores exponenciais correspondentes de cada posição
                decimal.append(2 ** -(i + 1))
        # Faz a soma total dos valores expoentes.
        self.decimal_a_menor = sum(decimal)
        # Chama a função para calcular a porcentagem de erro.
        self.Erro_Menor(self.decimal_a_menor)

    # Faz a aproximaçao 'A Maior' em Binário.
    def Binario_a_Maior(self, valor_decimal):
        binario = []
        # Faz as multiplicações sucessivas até gerar os valores binários.
        for c in range(self.quantidade_bits):
            valor_decimal * 2
            if int(valor_decimal) == 1:
                valor_decimal = valor_decimal - 1
            valor_decimal = valor_decimal * 2
            binario.append(int(valor_decimal))
        # Passa os valores da lista para uma String única.
        for c in binario:
            self.binario_a_maior += str(c)

    # Faz a conversão para Decimal do valor 'A Maior' que está em Binário.
    def Decimal_a_Maior(self):
        """ Etapa 1: Gera Binário """
        binario = []
        decimal = []
        # Cria o Binário que corresponde ao número de bits para a soma em decimal.
        for c in range(self.quantidade_bits):
            binario.append(0)
        ultimo = len(binario) - 1
        binario[ultimo] = 1

        """ Etapa 2: Converte Binário em Decimal """
        # Converte o Binário em Decimal.
        for i, v in enumerate(binario):
            if v == 1:
                decimal.append(2 ** (-i - 1))
        a_menor = self.decimal_a_menor
        decimal.append(a_menor)

        """ Etapa 3: Soma o Decimal 'A Menor' com o Decimal do Binário """
        # Soma com o valor de A menor já descoberto.
        self.decimal_a_maior = sum(decimal)

        # Chama as funções para converter em binário e para mostrar a porcentagem de erro.
        self.Binario_a_Maior(self.decimal_a_maior)
        self.Erro_Maior(self.decimal_a_maior)

    # Faz o cálculo para o Erro Menor.
    def Erro_Menor(self, valor_obtido):
        self.erro_menor = ((self.valor_decimal - valor_obtido) / self.valor_decimal) * 100
        if self.erro_menor < 0:
            self.erro_menor = self.erro_menor * (-1)

    # Faz o cálculo para o Erro Maior.
    def Erro_Maior(self, valor_obtido):
        self.erro_maior = ((self.valor_decimal - valor_obtido) / self.valor_decimal) * 100
        if self.erro_maior < 0:
            self.erro_maior = self.erro_maior * (-1)

    # Mostra o Resultado Final.
    def Resultado(self):
        print(
            "\n\033[36mA Menor:\033[m ({})10 ~= ({})2 = ({})10 => \033[33mErr\033[m {:.2f}%".format(self.valor_decimal,
                                                                                                    self.binario_a_menor,
                                                                                                    self.decimal_a_menor,
                                                                                                    self.erro_menor))
        print("\033[36mA Maior:\033[m ({})10 ~= ({})2 = ({})10 => \033[33mErr\033[m {:.2f}%".format(self.valor_decimal,
                                                                                                    self.binario_a_maior,
                                                                                                    self.decimal_a_maior,
                                                                                                    self.erro_maior))


usuario = Conversor()
usuario.Set_Valores()
usuario.Resultado()
