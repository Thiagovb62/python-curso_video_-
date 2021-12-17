Preço=float(input('Digite o preço:R$ '))
reajuste=int(input('o reajuste vai ser de quantos porcento:'))
reajusted= 1 + (reajuste/100) 
newprice=Preço*reajusted
print('o novo Preço é {:.2f} R$'.format(newprice))
