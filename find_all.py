import re
x= 'olha eu, eu, eu! 21 12 aqui 21eu tambem'
a= input("Pesquisar: ")
y= re.findall(a, x)
print(y)
c = (len(y));
print ("Tem " + str(c) + " ocorrências da sua string" )