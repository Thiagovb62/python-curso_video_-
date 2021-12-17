num=int(input('digite um numero: '))
resto=num%2
if resto==0:
    print('o numero  {}, com resto={} é par'.format(num,resto))
else:
    print('o numero {}, com resto={} é impar '.format(num,resto))