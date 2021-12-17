txt=str(input('digite uma Frase: ')).strip()#.upper()
print('seu nome tem {} A'.format( txt.upper().count('A')))
print('A primeira letra A esta na posiçao {}'.format( txt.upper().find('A')+1))
print('A Ultima letra A esta na posiçao {}'.format( txt.upper().rfind('A')+1))