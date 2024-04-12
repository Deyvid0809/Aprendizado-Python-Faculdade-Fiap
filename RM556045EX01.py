segunda = 0
terça = 0
quarta = 0
quinta = 0
sexta = 0
invalido = 0

# Verificar se houve empate


def empate():
    if segunda == terça or segunda == quarta or segunda == quinta or segunda == sexta:
        print('Teve empate!')
    elif terça == segunda or terça == quarta or terça == quinta or terça == sexta:
        print('Teve empate!')
    elif quarta == segunda or quarta == terça or quarta == quinta or quarta == sexta:
        print('Teve empate!')
    elif quinta == segunda or quinta == terça or quinta == quarta or quinta == sexta:
        print('Teve empate!')
    elif sexta == segunda or sexta == terça or sexta == quarta or sexta == quinta:
        print('Teve empate!')

# Repetir a quantidade de vezes necessaria para todos os funcionarios votarem e um print do relatorio de votação no final


def votacao(segunda, terça, quarta, quinta, sexta, invalido):

    escolha = ('Dia da semana')

    for i in range(0, Funcionarios, 1):

        escolha = input('Qual dia da semana é o melhor de sua preferência para realização das lives com o time da mentoria financeira (opções:segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira)? ')

        if escolha == ('segunda-feira') or escolha == ('2') or escolha == ('segunda'):
            print('Você escolheu: Segunda-feira')
            segunda = segunda + 1
        elif escolha == ('terça-feira') or escolha == ('3') or escolha == ('terça'):
            print('Você escolheu: Terça-feira')
            terça = terça + 1
        elif escolha == ('quarta-feira') or escolha == ('4') or escolha == ('quarta'):
            print('Você escolheu: Quarta-feira')
            quarta = quarta + 1
        elif escolha == ('quinta-feira') or escolha == ('5') or escolha == ('quinta'):
            print('Você escolheu: Quinta-feira')
            quinta = quinta + 1
        elif escolha == ('sexta-feira') or escolha == ('6') or escolha == ('sexta'):
            print('Você escolheu: Sexta-feira')
            sexta = sexta + 1
        else:
            invalido = invalido + 1
            print('escreve um dos seguintes dias da seguinte forma:segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira')
    print("Relação da votação: Numero de funcionarios que votaram:{}, Segunda:{}, Terça:{}, Quarta:{}, Quinta:{}, Sexta:{}, Invalido:{}" .format(
        Funcionarios, segunda, terça, quarta, quinta, sexta, invalido))


# Número de funcionarios que iram particpar da votação
Funcionarios = int(
    input('Qual número de funcionarios que iram participar da pesquisa? '))

votacao(segunda, terça, quarta, quinta, sexta, invalido)


empate()
