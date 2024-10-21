### Estruturas de Repetição ###

# FOR: Sabemos a quantidade de vezes que o laço de repetição foi executado
#Variáveis simples  - são as que calculam a entrada de dados
nota1=float(input("Nota 1:"))
nota2=float(input("Nota 2:"))
nota_opt=float(input("Nota Optativa:"))

if nota_opt != -1: #true
    menor_nota=min(nota1,nota2) #minimo e máximo para comparar variáveis "Igual no Excel"
    if nota_opt>menor_nota: #true
        if nota1==menor_nota:
            nota1=nota_opt
        else:
            nota2=nota_opt
            
media=(nota1+nota2)/2
print("Média:", media)

if media >=6.0:
    print("Aprovado")
elif media <=6.0:
    print("Reprovado")
else:
    print("Está em recuperação")


# FOR: sabemos a quantidade de vezes que o laço de repetição foi executado.

for i in range(5):
    numero=int(input('Digite um número:'))
    print(f'Dobro:{numero*2}')

#Exemplo1:
# contador=0
# while True:
#     numero=int(input('Digite um número:'))
#     print(f'Triplo:{numero*3}')
#     contador=contador+1

#Exemplo2:
num=5
while num<3:
    print('teste')

# DO WHILE: similar ao 'WHILE', mas garante que o bloco seja lido ao menos 1 vez
# antes da verificação da condição.

num=5
while True:
    print('teste')
    if not(num<3):
        break