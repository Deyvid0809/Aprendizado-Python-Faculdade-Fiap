ValordoCarro = float(input('Qual valor do carro? '))
Vista20 = ValordoCarro * 0.20
parcela = 6
procentagem = 0.03
valorparcela = ValordoCarro * procentagem

# Valor do carro a vista
print('O preço final à vista com 20% de desconto é: R${:.2f}'.format(
    ValordoCarro - Vista20))

# Repetição para mostra o valor do carro em 6/12/18/24/30/36/42/48/54 ou 60 parcelas com juros inicial de 3% aumentando de 3 em 3 porcento.
for i in range(0, 10, 1):

    print('O preço final parcelado em {:} X é de R${:.2f} com parcelas de R${:.2f}'.format(parcela,
          ValordoCarro + valorparcela, (valorparcela + ValordoCarro) / parcela))
    procentagem = procentagem + 0.03
    valorparcela = ValordoCarro * procentagem
    parcela = parcela + 6
