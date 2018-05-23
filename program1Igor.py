#!/usr/bin/env python
# -*- coding: utf-8 -*-
# program1.py

# Comentário em uma única linha é com o sustenido

'''
Entre trêss apostrofes é possível fazer comentário em várias linhas.
Primeira parte da aula é sobre a diferença entre o script e o interpretadorself.
Tente usar o python como um calculador com os seguintes comandos.
'''
import os # importa funções do pacote padrão do python para manipular coisas do sistema operacional

5+5 # execute no interpretador e com o script

print(5+5)
print(os.listdir('.'))

#=====================================================
# Operações matemáticas

print ( 5 - 3) #
print ( 4*3)
print ( 3/2)
print ( 5-4/2 )
print ( (5-4)/2)

print ( 5**2 )
print ( 4%2 )
print ( 5%2 )

print (4 == 3 )
print(4 == 4)

print (4>3)
print (4<5)

#======================================================
# Variáveis

a = 56
print (a) # a é uma variável global e pode ser chamada de qualque lugar do programa

def func():
	b = 3
	print(b) # b é uma variável local só pode ser chamada, usada ou modificada dentro do escopo que foi definida
func()

# Varáveis tem que começar com letras, não podendo números ou caracteres especiais.
# Também não pode definir variáveis com nomes já utilizados pela linguagems

# 324numero = 2 # erro de syntax
# print = 2 # syntax inválida

a1 = 3
print(a1)

#======================================================
# Tipos de dados em python
# Os tipos definidos no python são chamados de builtin types
# Os tipos númericos são aqueles tu pode executar operaões matemáticas ou usar como contador.
# Os tipos númericos vão variar dependendo da precisão.

a = 3 # é um inteiro
print(type(3))
print(type(a))

b = 4.0005
c = long(b)
print(type(b))
print(b)
print(c)

a = float(a)
print(a)
a = int(a)
print(a)

d = a+3
print(d)

d = int(a +3.0)
print(d)


#=================================
# usando o help no python

#help(int)
