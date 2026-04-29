def dobro(a): 
    return a * 2

def quadrado(a): 
    return a ** 2


n1 = int(input('Digite um número: '))

resultado = dobro(n1)
resultadoQuadrado = quadrado(n1)

print(f'O dobro é {resultado} e o quadrado é {resultadoQuadrado}')