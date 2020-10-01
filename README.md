# PROJETO PYTHON: Aproximação de Decimais

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
```
![Classe](https://github.com/ThiagoLozano/Aproximacao-de-Decimais/blob/master/Screenshot/Classe.PNG)

### Função Erro de Aproximação
```
@staticmethod
    def Erro(nd, no):
        erro = (nd - no) / nd
        if erro < 0:
            erro = erro * (-1)
        print("\033[33mErr\033[m = {:.2f}%".format(erro * 100))
```
![Erro](https://github.com/ThiagoLozano/Aproximacao-de-Decimais/blob/master/Screenshot/Erro.PNG)

### Representação

![Multiplicacao](https://github.com/ThiagoLozano/Aproximacao-de-Decimais/blob/master/Screenshot/Multiplicacao.PNG)

![Aproximação3](https://github.com/ThiagoLozano/Aproximacao-de-Decimais/blob/master/Screenshot/Aproximacao.PNG)
