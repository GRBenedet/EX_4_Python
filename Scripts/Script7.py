#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lar = float(input('Qual a largura da sua parede em metros? '))
alt = float(input('Qual a altura da sua parede em metros? '))
area = alt * lar

print('A dimesão de {}X{} tem uma area de {}m². \npara pintar essa parede ,vocé precisara de {}l de tinta.'.format(lar , alt , area , area / 2))