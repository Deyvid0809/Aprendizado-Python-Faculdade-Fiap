investimento = input(
    'Qual dos investimentos você deseja resgatar:1 para CDB, 2 para LCI e 3 para LCA?')
Valordoresgate = float(input('Qual Valor deseja resgatar?'))
Dias = int(input('Qunatos dias seu dinheiro está investido?'))
procentagemIR = 0.225
ValorIR = 0
Resgate = 0

# Verificação de qual seria o tipo de investimento.
if investimento == '1':
    # Verificação de dias de investimento juntamente com o calculo do IR encima do valor investido
    if Dias <= 180:
        ValorIR = Valordoresgate * procentagemIR
        Resgate = Valordoresgate - ValorIR
        print('Valor que deseja ser resgatado R${:.2f} Dias de investimento:{} Taxa IR R${: .2f} Valor Final resgatado R$ {: .2f}' .format(
            Valordoresgate, Dias, ValorIR, Resgate))
    elif Dias <= 360:
        procentagemIR = procentagemIR - 0.025
        ValorIR = Valordoresgate * procentagemIR
        Resgate = Valordoresgate - ValorIR
        print('Valor que deseja ser resgatado R${:.2f} Dias de investimento:{} Taxa IR R${: .2f} Valor Final resgatado R$ {: .2f}' .format(
            Valordoresgate, Dias, ValorIR, Resgate))
    elif Dias <= 720:
        procentagemIR = procentagemIR - 0.050
        ValorIR = Valordoresgate * procentagemIR
        Resgate = Valordoresgate - ValorIR
        print('Valor que deseja ser resgatado R${:.2f} Dias de investimento:{} Taxa IR R${: .2f} Valor Final resgatado R$ {: .2f}' .format(
            Valordoresgate, Dias, ValorIR, Resgate))
    elif Dias >= 720:
        procentagemIR = procentagemIR - 0.075
        ValorIR = Valordoresgate * procentagemIR
        Resgate = Valordoresgate - ValorIR
        print('Valor que deseja ser resgatado R${:.2f} Dias de investimento:{} Taxa IR R${: .2f} Valor Final resgatado R$ {: .2f}' .format(
            Valordoresgate, Dias, ValorIR, Resgate))
elif investimento == '2' or investimento == '3':
    print('Isento de taxa valor restado de R${:.2f}' .format(Valordoresgate))
else:
    print('você cometeu algum erro tente novamente')
