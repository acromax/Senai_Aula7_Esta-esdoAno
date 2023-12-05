# aula 7 de Python Turma 21
# programa para calcular em qual estação do ano se encontra um determinado mês

# Apresentação
print ('As Estações do Ano no Brasil seguem as seguintes datas: '
       '\nOutono começa 20 de Março,'
       '\nInverno começla 21 de Junho '
       '\nPrimavera começa 23 de Setembro'
       '\nVerão começa 22 de Dezembro')

# Processamento
def estacao(mes):
    if 3 <= mes <= 5:
        return "Outono"
    elif 6 <= mes <= 8:
        return "Inverno"
    elif 9 <= mes <= 11:
        return "Primavera"
    else:
        return "Verão"

# Entrada
mes = int(input("Digite o número do mês (1 a 12): "))

# Saída
print(f'A estação do ano é: {estacao(mes)}')

