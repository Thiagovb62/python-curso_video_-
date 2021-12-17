print('-=-'*20)
print('Analisador de triangulos')
print('-=-'*20)
l1=int(input('primeiro segmento: '))
l2=int(input('segundo segmento: '))
l3=int(input('terceiro segmento: '))
if l1<l2 +l3 and l2<l1+l3 and l3<l1+l2:
    print ('Os segmentos  formam um trinagulo!') 
else: 
    print ('Os segmentos nao formam um tringulo!')