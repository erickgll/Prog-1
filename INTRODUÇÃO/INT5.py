#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

anos = int(input('Digite os anos? '))
meses = int(input('Digite os meses? '))
dias = int(input('Digite os dias? '))
v1 = anos * 365
v2 = meses * 30
v3 = (dias + v1 + v2)
print('A idade dessa pessoa em dias é ',v3)