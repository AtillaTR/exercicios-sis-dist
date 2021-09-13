import math

#Exercicio 16
print("Digite o tamanho e metros quadrados da area ser pintada\n")
area = int(input(">"))

value_paint_18 = 80.00
value_paint_3 = 25.00

total_paint_18 = math.ceil((area / 6) / 18)
total_paint_3 = math.ceil((area / 6) / 3.6)

total_mist_paint = area / 6

value_paint_18 = 80.00 * total_paint_18
value_paint_3 = 25.00 * total_paint_3


print (f'Voce precisara de :{total_paint_18} latas de 18L \n e o valor sera: R${value_paint_18:.2f}')
print (f'Voce precisara de :{total_paint_3} latas de 3.6L \n e o valor sera: R${value_paint_3:.2f}')

# Exercicio 18
print("Digite o tamanho do arquivo e Mb")
size = float(input(">"))
print("Digite a sua velocidade de internet em Mbps")
internet = float(input(">"))

time_min = (size / internet) /60

print(f'O tempo aproximado do download e de : 1{time_min:.1f} min')


#Exercicio 1 

print('Ola mundo')