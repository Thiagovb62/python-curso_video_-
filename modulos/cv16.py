cidade=str(input('qual nome da cidade: ')).strip()
#print(cidade[:5].upper() == 'SANTO') outro metodo
cidade=cidade.split()
cidade[0]=cidade[0].upper()
print(cidade[0] == 'SANTO') 
