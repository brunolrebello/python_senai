from lib2to3.pgen2.literals import simple_escapes


aladdin = input('Aladdin apareceu? \n')
jasmine = input('Jasmin apareceu? \n')



if not ((aladdin == 'sim') or (jasmine =='sim')):
    print('Teve o seu encontro')
else:
    print('Não teve encontro')