#ATIVIDADES:

#1) Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.




# def calcular_multa(peso_peixes):
#     limite_peso = 100
#     valor_multa_por_quilo = 20.0

#     if peso_peixes > limite_peso:
#         excesso = peso_peixes - limite_peso
#         multa = excesso * valor_multa_por_quilo
#         return multa
#     else:
#         return 0.0

# # Exemplo de uso:
# peso = float(input("Digite o peso total dos peixes (em quilos): "))
# multa = calcular_multa(peso)

# if multa > 0:
#     print(f"O pescador deve pagar uma multa de R$ {multa:.2f}.")
# else:
#     print("Não há multa a ser paga.")


def multa():
    peso = float(input('Digite o peso: '))
  

    if peso <= 100 :
        print("Sem Multa")
    else: peso >100
    excesso = peso - 100
    multa = excesso * 0.5  # Supondo que a multa é R$ 0.5 por quilo excedente
    print(f" A Multa é R$ {multa:.2f}")
multa()