def calculoMulta(a):
    if a >= 100:
        return (a - 100) * 4
    
pesoPeixes = float(input('Digite a qtd de kg de peixes pescados: '))

if pesoPeixes >= 100:
    total = calculoMulta(pesoPeixes)
    print(f'O total de kg peixes pescados foi de: {pesoPeixes}kg e deverá pagar uma multa de: R${total:.2f}')
else:
    print(f'O total de kg peixes pescados foi de: {pesoPeixes}kg e não houve multa')
