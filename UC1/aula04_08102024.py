###EESTRUTURAS DE CONDIÇÕES###
#IF ELSE X SWITCH CASE

#Atividades práticas com if/else e switch/case:

#1) IF ELSE

# mes=int(input('Digite um número entre 1 e 12:'))

# if mes==1:
#     print('Janeiro')
# elif mes==2:
#     print("Fevereiro")
# elif mes==3:
#     print("Março")
# elif mes==4:
#     print("Abril")
# elif mes==5:
#     print("Maio")
# elif mes==6:
#     print("Junho")
# elif mes==7:
#     print("Julho")
# elif mes==8:
#     print("Agosto")
# elif mes==9:
#     print("Setembro")
# elif mes==10:
#     print("Outubro")
# elif mes==11:
#     print("Novembro")
# elif mes==12:
#     print("Dezembro")

# else:('Por favor forneça um número válido')

#2) Switch Case

#mes=int(input("digite um número ente 1 e 12:"))
#meses=(1:"Janeiro", 2:"Fevereiro")

#1) Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
#Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que 
#a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada;

#Variáveis simples  - são as que calculam a entrada de dados
#input recebe dados e output exibe os dados


lamp_potencia=float(input("Digite a potência da lâmpada ( watss):")) 
larg_comodo=float(input("Digite a largura do cômodo:"))
comp_comodo=float(input("Digite o comprimento do cômodo:"))

#Variáveis para o cálculo de área e de potência
area_comodo=larg_comodo*comp_comodo
potencia=3*lamp_potencia

#Variáveis para o  cálculo do número de lâmpadas e bocais

numero_lampada=potencia/lamp_potencia
bocais=area_comodo/3

#Exibição dos Resultados
print("lampadas:", numero_lampada)
print(f"Número de lâmpadas necessárias: {numero_lampada:.2f}") #f - formatação de texto / 2f - duas casas após a vírgula
print(f"Número de bocais necessárias: {bocais:.2f}")





#  2) Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de 
# caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa 
# de azulejos possui 1,5 m²;

# 3) Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um 
# programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de combustível gasto e o 
# valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia;

# 4) Escreva um programa que leia o código de origem de um produto e imprima na tela a região de sua procedência, conforme a tabela que foi passada.
 
# Observação: caso o código não seja nenhum dos especificados, o produto deve ser encarado como “Importado”;

# 5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a 
# nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se 
# está em exame, de acordo com as informações abaixo: 
# Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;


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






# 6) Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.


