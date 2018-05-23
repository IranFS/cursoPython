#!/usr/bin/env python
# -*- coding: utf-8 -*-
#program1.py
#Comentário curto
'''
Comentário longo, com três aspas simples
Diferenças entre scrip e interpretador
'''
import os #Importa funções padrões do Python
5+5 #Este resultado não é mostrado
print(5+5) #Este resultado é mostrado
print(os.listdir('.')) #Utiliza-se a função listdir do módulo os para exibir na tela o conteúdo do diretório atual
#-------------------------------------------------------
#Operações Matemáticas
'''
Utilizando-se a função "print", o valor de cada uma das operações aritméticas
é retornado na saída do código. O python prioriza, do mesmo modo que os humanos,
as operações de multiplicação e divisão, nas sequência vêm as operações de
soma e subtração.
'''
print(5-3)
print(4*3)
print(3/2)
print(5-4/2)
print((5-4)/2)

print(5**2)
print(4%2)
print(5%2)

print(4==3)
print(4==4)

print(4>3)
print(4<5)
#-------------------------------------------------------------------------------
#Variáveis
a = 56
print(a) #Variável global, pode ser acessada em qualquer parte do programa

def func():
    b = 3
    print(b) #Variável local, pode ser chamada, usada ou modificada dentro do escopo de sua definiçãoptimize
func()
'''
Variáveis podem começar com letras, mas não com números ou caracteres especiais.
Também não é possível utilizar nomes de funções já definidas no próprio Python

'''
#-------------------------------------------------------------------------------
#Tipos de dados em python
#Numéricos
c = 3 #Define-se uma variável global "c"
print(type(c)) #Retorna na tela a execução da função "type" com a função "c" como argumento, devendo resultar no tipo "int".
d = 3.5 #Define-se a variável global "d" contendo um valor com ponto flutuante (floating point).
print(d) #Retorna o valor de "d" na tela.
print(type(d)) #Retorna na tela tipo da variável "d", que deve ser "float"
print(c+2) #Retorna na tela o valor da soma entre a variável c e o valor 2 (deve ser 5).
print(int(d+2)) #Retorna o valor da soma entre d e 2, resultando no valor 5.5, um valor float.
#-------------------------------------------------------------------------------
