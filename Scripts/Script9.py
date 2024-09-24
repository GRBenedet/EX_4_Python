#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com o aumento sendo definido pelo usuário.

sal = float(input('qual se salário atual? R$'))
aut = float(input('qual o percentual de aumento? '))

print('o seu salario de R${} aumentou em {}% e agora é {:.2f}'.format(sal, aut , sal + (sal * aut / 100)))