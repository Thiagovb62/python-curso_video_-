ano=int(input('qual ano vai ser analisado? caso queira saber do ano atual digite 0:'))
if ano%4==0 and  ano%100!=0 or ano%400==0:
   print('o ano {} é BISSEXTO'.format(ano))
else:
    print('o ano {} nao é BISSEXTO',format(ano))
