# #Exercicio 1
x=True
while(x==True):
    nota = int(input("Digite uma nota entre 0 e 10:"))
    if(nota>0 and nota<10):
        x=False
    else:
        x=True

#Exercicio2 
while(x==True):
    user=input("Digite o nome de usuario:")
    password=input("Digite sua senha:")
    if(password==user):
        print("Sua senha deve ser diferente do nome de usuario!")
        x=True
    else:
        x=False


#Exercicio 12
t=int(input("Digite o numero no qual deseja ver a tabuada"))
for number in range(1,11):
    result=t*number
    print(f'{t}x{number}={result}')