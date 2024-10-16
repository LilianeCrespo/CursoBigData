##EESTRUTURAS DE CONDIÇÕES###
#IF ELSE X SWITCH CASE

#Atividades práticas com if/else e switch/case:

#1 IF ELSE
mes=int(input('Digite um número entre 1 e 12:'))

if mes==1:
    print('Janeiro')
elif mes==2:
    print("Fevereiro")
elif mes==3:
    print("Março")
elif mes==4:
    print("Abril")
elif mes==5:
    print("Maio")
elif mes==6:
    print("Junho")
elif mes==7:
    print("Julho")
elif mes==8:
    print("Agosto")
elif mes==9:
    print("Setembro")
elif mes==10:
    print("Outubro")
elif mes==11:
    print("Novembro")
elif mes==12:
    print("Dezembro")

else:('Por favor forneça um número válido')

#2) Switch Case

#mes=int(input("digite um número ente 1 e 12:"))
#meses= ( 1: "Janeiro",2: "Fevereiro")

#1) Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
#Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que 
#a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada;

pot_lamp=int(input('Digite a potência da lampada em watts:')) #Potêcia da lampada
largura=float(input('Digite a largura do comodo:'))
comprimento=float(input("Digite o comprimento do comodo:"))
area=largura*comprimento

if(pot_lamp>=9):
 total_lamp=area/pot_lamp
 print('Será necessário: ', total_lamp,' Lâmpadas')
else:
 print('Potência da lampada insuficiente,potencia mínima de 9 watts')


#  2) Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de 
# caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa 
# de azulejos possui 1,5 m²;

comprimento=float(input("Digite o comprimento da cozinha:"))
largura=float(input('Digite a largura da cozinha:'))
altura=float(input('Digite a altura da cozinha: '))
azulejos=1.5

area_1=(comprimento*altura)*2
area_2=(largura*altura)*2
area_total=area_1+area_2

total_azulejos=area_total/azulejos

print('Serão necessárias :',total_azulejos,' caixas de azulejos')

# 3) Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um 
# programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de combustível gasto e o 
# valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia;


preco_combustivel=4.87

inicio_dia=float(input('Informe o número  odômetro (km) do inicio do dia: '))
fim_dia=float(input('Infoeme o número  odômetro (km) do fim do dia: '))
combustivel=float(input('informe o total de combustível gasto (litros): '))
total_bruto=float(input('Informe o total arrecadado(r$): '))

total_combustivel=combustivel*preco_combustivel
total_km=fim_dia-inicio_dia
media=combustivel/total_km
total_liquido=total_bruto-total_combustivel

print('A média de consumo por km/l: ',media)
print('O lucro líquido do dia: R$',total_liquido)

# 4) Escreva um programa que leia o código de origem de um produto e imprima na tela a região de sua procedência, conforme a tabela que foi passada.
 
# Observação: caso o código não seja nenhum dos especificados, o produto deve ser encarado como “Importado”;

codigo=int(input('Por favor informe o código de origem do produto: '))

if codigo==1:
 print('Região Sul')
elif codigo==2: 
 print('Região Norte')
elif codigo==3:
 print('Região Leste')
elif codigo==4: 
 print('Região Oeste')
elif codigo==5: 
 print('Região Nordeste')
elif codigo==6: 
 print('Região Nordeste')
elif codigo==7: 
 print('Região Sudeste')
elif codigo==8:  
 print('Região Sudeste')
elif codigo==9: 
 print('Região Sudeste')
elif codigo==10: 
 print('Região Centro-oeste')
elif codigo==11: 
 print('Região Noroeste')
else:
 print('Por favor infome um código de 1 ao 11; ') 
 codigo=int(input('Por favor informe o código de origem do produto: '))

# 5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a 
# nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se 
# está em exame, de acordo com as informações abaixo: 
# Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;

avaliacao_1=float(input('Informe a nota da primeira avaliação:'))
avaliacao_2=float(input('Informe a nota da segunda avaliação:'))
optativa=int(input('O aluno realizou a prova optativa? (Sim=1/Não=0)'))

if optativa==1:
 avaliacao_optativa=float(input('Informe a nota da avaliação optativa :'))
 if avaliacao_1<avaliacao_2:
   media=(avaliacao_optativa+avaliacao_2)/2
 else:
   media=(avaliacao_optativa+avaliacao_1)/2
elif optativa==0:
 avaliacao_optativa=-1
 media=(avaliacao_1+avaliacao_2)/2
else:
  print('Por favor,informe uma opção válida!')
 

if media>=6.0:
   print('A média: ',media,'Aprovado!')
elif media<3.0:
  print('A média: ',media,'Reprovado')
else :
  print('A média: ',media,'Exame') 

# 6) Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.

valor = float(input("Digite um número: "))

if valor >= 0:
    print("O número é positivo.")
else:
    print("O número é negativo.")