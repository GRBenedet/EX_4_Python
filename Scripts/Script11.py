#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos quilolemtos foram rodados com o carro? '))
dias = int(input('Quantos dias o carro foi alugado? '))

alg = dias * 60

rod = km * .15

print('O preço do aluguel foi de R${} e o preço dos quilometros rodados foi de R${}, o total a pagar é de R${}.'.format(alg , rod , alg + rod))