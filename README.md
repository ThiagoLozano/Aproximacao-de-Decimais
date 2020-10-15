# PROJETO PYTHON: Conversor Reais para Binário
> Um programa que mostra a aproximação de um valor Binário em Decimal, simulando a lógica computacional.

O programa deve receber um valor entre > 0 e < 1, depois o usuário deve escolher o espaço de bits que ele 
quer visualizar (5, 6, 7, 8, 9, 10, 11 ou 12). O programa deve retornar o valor aproximado correspondente ao 
número de bits com a porcentagem da aproximação A maior e A menor.Fazendo também todas as validações necessárias
de entrada de dados.

# Tecnologias Utilizadas
* **_PyCharm;_**
* **_Python 3;_**

# Exemplo de Uso
### Classe
```
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
```
![Classe](https://github.com/ThiagoLozano/Conversor-Reais-para-Binario/blob/master/Screenshot/Classe.PNG)

### Função Binário A Menor
```
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
```
![Binario A Menor](https://github.com/ThiagoLozano/Conversor-Reais-para-Binario/blob/master/Screenshot/Binario_A_Menor.PNG)

### Função Erro de Aproximação
```
    def Erro_Menor(self, valor_obtido):
        self.erro_menor = ((self.valor_decimal - valor_obtido) / self.valor_decimal) * 100
        if self.erro_menor < 0:
            self.erro_menor = self.erro_menor * (-1)
```
![Erro](https://github.com/ThiagoLozano/Conversor-Reais-para-Binario/blob/master/Screenshot/Erro.PNG)

### Representação

![Multiplicacao](https://github.com/ThiagoLozano/Conversor-Reais-para-Binario/blob/master/Screenshot/Modelo_Conversao_Binario.PNG)

![Aproximação](https://github.com/ThiagoLozano/Conversor-Reais-para-Binario/blob/master/Screenshot/Modelo_Conversao.PNG)
