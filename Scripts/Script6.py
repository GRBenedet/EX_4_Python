#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Valor de dólares utilizado é de 5,46.

num = float(input('Quantos reais você tem na carteira? R$'))

print('com R${} você consegue comprar US${:.2f}.'.format(num , num / 5.46))