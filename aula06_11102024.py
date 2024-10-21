###AULA06 - 11/10/2024###
-
#RESOLUÇÃO EXERCÍCIO 5
-
# Definindo o número de alunos
num_alunos = 20

# Estrutura de repetição para processar as notas de cada aluno
for i in range(1, num_alunos + 1):
    print(f"Aluno {i}:")
    
    # Entrada de dados
    nota1 = float(input("Digite a nota da primeira avaliação: "))
    nota2 = float(input("Digite a nota da segunda avaliação: "))
    nota_optativa = float(input("Digite a nota da avaliação optativa (ou -1 se não fez): "))

    # Substituir a menor nota pela optativa, se ela for maior
    if nota_optativa != -1:
        menor_nota = min(nota1, nota2)
        if nota_optativa > menor_nota:
            if nota1 == menor_nota:
                nota1 = nota_optativa
            else:
                nota2 = nota_optativa

    # Cálculo da média
    media = (nota1 + nota2) / 2

    # Exibindo resultado e status
    print(f"Média do semestre: {media:.2f}")
    
    if media >= 6.0:
        print("Aprovado")
    elif media < 3.0:
        print("Reprovado")
    else:
        print("Exame")

#ATIVIDADE DE FIXAÇÃO:

#>>>Desenvolva um programa que guarde os dados de 10 pessoas que estão se candidatando a uma vaga de emprego, sabendo que candidatos 
menores de 18 anos não podem participar. Os dados coletados são: nome, data de nascimento, telefone, e-mail, formação acadêmica e a 
experiência profissional.