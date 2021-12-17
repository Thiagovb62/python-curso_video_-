import math
cateto_adjacente=int(input('qual valor do cateto adjacente:'))
cateto_oposto=int(input('qual valor do cateto oposto:'))
cateto_adjacente=cateto_adjacente**2
cateto_oposto=cateto_oposto**2
hipotenusa=cateto_oposto+cateto_adjacente
hipotenusa=math.sqrt(hipotenusa)
#hipotenusa=(cateto_oposto**2 + cateto_adjacente**2) ** (1/2)
#hip=math.hypot(co,ca)
print('o valor da hipotenusa deu {:.2f}'.format(hipotenusa))