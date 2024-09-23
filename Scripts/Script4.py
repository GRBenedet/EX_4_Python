#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

num = float(input('Digite uma distancia em metros: '))

print('a media de {} metros corresponte a: \n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(num , num/1000 , num/100 , num/10 , num*10 , num*100 , num * 1000))