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
print(5+5)
print(os.listdir('.'))
#-------------------------------------------------------
#Operações Matemáticas
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
Variáveis podem começar com letras, mas não com números ou caracteres especiaisself.
Também não é possível utilizar nomes de funções já definidas no próprio Python

'''
#-------------------------------------------------------------------------------
#Tipos de dados em python
#Numéricos
c = 3
print(type(c))
d = 3.5
print(d)
print(type(d))
print(c+2)
print(int(d+2))
#-------------------------------------------------------------------------------
