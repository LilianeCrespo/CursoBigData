


##Atividade  Aula 7###
# Crie um código que seja capaz de ler e armazenar uma sequência de 20 números pares e 20 números ímpares.
# Obs: utilize estruturas de repetição para fechar esse conjunto  de números.



# def ler_numeros():
#     numeros_pares = []
#     numeros_impares = []

#     while len(numeros_pares) < 20 or len(numeros_impares) < 20:
#         try:
#             numero = int(input("Digite um número inteiro: "))
#             if numero % 2 == 0:
#                 if len(numeros_pares) < 20:
#                     numeros_pares.append(numero)
#                     print(f"Número par {numero} adicionado. Total de pares: {len(numeros_pares)}.")
#                 else:
#                     print("Já foram adicionados 20 números pares.")
#             else:
#                 if len(numeros_impares) < 20:
#                     numeros_impares.append(numero)
#                     print(f"Número ímpar {numero} adicionado. Total de ímpares: {len(numeros_impares)}.")
#                 else:
#                     print("Já foram adicionados 20 números ímpares.")
#         except ValueError:
#             print("Entrada inválida! Por favor, insira um número inteiro.")

#     return numeros_pares, numeros_impares


# pares, impares = ler_numeros()


# print("Números Pares:", pares)
# print("Números Ímpares:", impares)



    
#ATIVIDADES aula 8:

# 2) Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.


# def multa():
#     peso = float(input('Digite o peso: '))
    
#     if peso <= 100:
#         print("Sem Multa")
#     else:
#         excesso = peso - 100
#         multa = excesso * 0.5  # Multa de 0.5 por quilo excedente
#         print(f"A multa é R$ {multa:.2f}")

# multa()
#

# 3) Crie um programa que faça a leitura da altura e do peso de N pessoas para o cálculo do IMC, mostrando ao final a classificação de acordo
# com a tabela de IMC.
#https://abeso.org.br/obesidade-e-sindrome-metabolica/calculadora-imc/

# def classificar_imc(imc):
#     if imc < 18.5:
#         return "Abaixo do peso"
#     elif imc < 24.9:
#         return "Peso normal"
#     elif imc < 29.9:
#         return "Sobrepeso"
#     elif imc < 34.9:
#         return "Obesidade Grau I"
#     elif imc < 39.9:
#         return "Obesidade Grau II"
#     return "Obesidade Grau III (mórbida)"

# def calcular_imc(peso, altura):
#     return peso / (altura ** 2)

# def calcular_imc_para_n_pessoas():
#     n = int(input("Digite o número de pessoas: "))

#     for i in range(n):
#         print(f"Pessoa {i + 1}:")
#         altura = float(input("Digite a altura: "))
#         peso = float(input("Digite o peso: "))

#         imc = calcular_imc(peso, altura)
#         classificacao = classificar_imc(imc)

#         print(f"IMC: {imc:.2f}")
#         print(f"Classificação: {classificacao}")

# calcular_imc_para_n_pessoas()





# 4) Crie funções que mostrem um cardápio de um restaurante (pelo menos 4 itens) e que permitam realizar pedidos e fechar a conta. - Função para mostrar o cardápio -


# def mostrar_cardapio():
#     cardapio = {
#         1: ("Hambúrguer", 40.00),
#         2: ("Pizza", 60.00),
#         3: ("Refrigerante", 10.00),
#         4: ("Suco", 8.00)
#     }
    
#     print("Cardápio")
#     for numero, (item, preco) in cardapio.items():
#         print(f"{numero}. {item} - R$ {preco:.2f}")
    
#     return cardapio

# # Função para realizar pedidos
# def realizar_pedido(cardapio):
#     pedido = []
#     while (opcao := input("Digite o número do item que deseja pedir (ou '0' para finalizar): ")) != '0':
#         if opcao.isdigit() and int(opcao) in cardapio:
#             item, preco = cardapio[int(opcao)]
#             pedido.append((item, preco))
#             print(f"{item} adicionado ao pedido.")
#         else:
#             print("Opção inválida. Tente novamente.")
    
#     return pedido

# # Função para fechar a conta
# def fechar_conta(pedido):
#     total = sum(preco for _, preco in pedido)
#     print(" Seu Pedido ")
#     for item, preco in pedido:
#         print(f"{item} - R$ {preco:.2f}")
#     print(f"Total a pagar: R$ {total:.2f}")

# # Função principal para executar o fluxo do restaurante
# def restaurante():
#     print("Bem-vindo ao Restaurante Python!")
#     cardapio = mostrar_cardapio()
#     pedido = realizar_pedido(cardapio)
    
#     if pedido:
#         fechar_conta(pedido)
#     else:
#         print("Você não fez nenhum pedido.")

# # Executa o restaurante
# restaurante()




# 5) Leia três pares de números inteiros fornecidos pelo usuário, calcule e imprima a soma de cada par separadamente. Utilize 
#tratamento de erros para garantir que os valores inseridos sejam válidos e, se o número for ÍMPAR, ter uma exceção personalizada.



class NumeroImparError(Exception):
    pass

def ler_inteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if numero % 2 != 0:
                raise NumeroImparError(f"O número {numero} é ímpar Insira um número par.")
            return numero
        except (NumeroImparError, ValueError) as e:
            print(f"Erro: {e} Tente novamente.")

def somar_pares():
    for i in range(1, 4):
        print(f"Par {i}:")
        num1 = ler_inteiro("Digite o primeiro número par: ")
        num2 = ler_inteiro("Digite o segundo número par: ")
        print(f"Soma do par {i}: {num1 + num2}")

# Simulação de teste (sem input)
def somar_pares_simulado(pares):
    for i, (num1, num2) in enumerate(pares, start=1):
        print(f"Par {i}:")
        print(f"Primeiro número: {num1}")
        print(f"Segundo número: {num2}")
        print(f"Soma do par {i}: {num1 + num2}")

# Teste simulado
#pares_teste = [(2, 4), (6, 8), (10, 12)]
#somar_pares_simulado(pares_teste)
somar_pares()