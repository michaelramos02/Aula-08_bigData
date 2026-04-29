def calculoIMC(a, b):
    return a / (b * b)
   
reposta = 'S'

while reposta != 'N':
    aluno =  input('Digite o nome do aluno: ')
    altura = float(input('Digite a altura do aluno: '))
    peso = float(input('Digite o peso do aluno: '))
    resultado = calculoIMC(peso, altura)
    if resultado > 40:
         print(f'{aluno} está com {peso}kg e tem {altura:.2f}m o IMC é : {resultado:.2f} Obesidade grau III')
    elif resultado >= 40:
        print(f'{aluno} está com {peso}kg e tem {altura:.2f}m o IMC é : {resultado:.2f} Obesidade grau II')
    elif resultado > 35:
        print(f'{aluno} está com {peso}kg e tem {altura:.2f}m o IMC é : {resultado:.2f} Obesidade grau I')
    elif resultado > 29.9:
        print(f'{aluno} está com {peso}kg e tem {altura:.2f}m o IMC é : {resultado:.2f} Acima do peso')
    elif resultado > 24.9:
        print(f'{aluno} está com {peso}kg e tem {altura:.2f}m o IMC é : {resultado:.2f} Peso normal')
    elif resultado > 18.4:
        print(f'{aluno} está com {peso}kg e tem {altura:.2f}m o IMC é : {resultado:.2f} Abaixo do peso')
    else:
        print(f'{aluno} está com {peso}kg e tem {altura:.2f}m o IMC é : {resultado:.2f} Muito abaixo do peso')


    resposta = input('Quer continuar? ')
    
    







 
    