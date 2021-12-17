vel=int(input('qual velocidade do carro: '))
multa=(vel - 80)*7
if vel >= 80: 
    print('voce foi multado,o valor da multa sera de {} R$'.format(multa))
else: 
    print('tudo ok')