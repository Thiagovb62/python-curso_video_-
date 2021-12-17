import random
#from  random import randit
print('-=-'*30)
print('vou pensar em numero de 0 a 5,vamos ver se voce acerta qual eh,pensando......')
print('-=-'*30)
usuario=int(input('diga um numero de 0 a 5: '))
#comp=randit
lista=[0,1,2,3,4,5]
num=random.choice(lista)
print('pensei em {}'.format(num))
print('voce chutou {}'.format(usuario))
if num==usuario:
    print('parabens,voce venceu!')
else:
    print('mais sorte na proxima!')