Valordivida = float(input('Qual valor da divida? '))
parcela = 3
procentagem = 0.10
juros = Valordivida * procentagem
Divida = juros + Valordivida

# Valor da divida em apenas uma parcela sem juros adicional
print('Total:R${:.2f} Juros: R$0.00 Número de parcelas:1 Valor da parcella:R${:.2f}'.format(
    Valordivida, Valordivida))

# Repetição para fazer o calculo da divida para ser paga em até 3/6/9 ou 12 vezes com juros inicial de 10% e aumentando em 5%.
for i in range(0, 4, 1):

    print('Total:R${:.2f} Juros: R${:.2f} Número de parcelas:{} Valor da parcella:R${:.2f}'.format(
        Divida, juros, parcela, Divida / parcela))
    procentagem = procentagem + 0.05
    juros = Valordivida * procentagem
    Divida = juros + Valordivida
    parcela = parcela + 3
