import math
angulo=int(input('qual valor do angulo:'))
seno=math.sin(math.radians(angulo))
coseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print(' o sen do angulo {}, deu {:.2f} ,o seu coseno deu {:.2f} e sua tangente deu {:.2f}'.format(angulo,seno,coseno,tangente))