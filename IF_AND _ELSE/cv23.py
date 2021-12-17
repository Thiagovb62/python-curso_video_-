viagem=int(input(' quantos km a viagem tem de distancia? '))
curta=viagem*0.50
longa=viagem*0.45
#if viagem<=200:
    #print('o valor da vaigem deu {}R$'.format(viagem*0.50))
#else:
    #print('o valor da vaigem deu {}R$'.format(viagem*0.45))
if viagem<=200:
    print('o valor da vaigem vai dar R${:.2F} !'.format(curta))
else:
    print('o valor da vaigem vai dar R${:.2F}R$ !'.format(longa))