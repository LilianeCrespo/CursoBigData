# 1) Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.

def multa():
    peso = float(input('Digite o peso: '))
  

    if peso <= 100 :
        print("Sem Multa")
    else: peso >100
    excesso = peso - 100
    multa = excesso * 0.5  # A multa é R$ 0.5 por quilo excedente
    print(f" A Multa é R$ {multa:.2f}")
multa()

#
# 2) Crie um programa que faça a leitura da altura e do peso de N pessoas para o cálculo do IMC, mostrando ao final a classificação de acordo
# com a tabela de IMC.

#https://www.rededorsaoluiz.com.br/calculadora-de-imc


def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Magreza"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    num_pessoas = int(input("Digite o número de pessoas: "))
    for i in range(num_pessoas):
        print(f"\nPessoa {i + 1}:")
        altura = float(input("Digite a altura (em metros): "))
        peso = float(input("Digite o peso (em quilos): "))
        
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        
        print(f"IMC: {imc:.2f} - Classificação: {classificacao}")
        if __name__ == "__main__":
           main()
#
# 3) Crie funções que mostrem um cardápio de um restaurante (pelo menos 4 itens) e que permitam realizar pedidos e fechar a conta.
#

