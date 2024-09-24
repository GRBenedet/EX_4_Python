#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

val = float(input('qual o valor do produto? R$'))

print('O produto que custava R${}, na promoção, com desconto de 5%, agora custa R${:.2f}.'.format(val , val - ((val * 5) / 100))) 