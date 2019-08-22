#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""for random(100)
	if random > 50
		yang
	else
		ying
return 0 or 1"""
from random import randint
print ""
print "    \t\t\tTirada para I Ching\n"
print "     Hexagrama principal:                      Hexagrama transmutado: \n"
x=0
while x < 6:
    line = randint(6,9)
    x = x + 1
    if line == 9:
	print " linea yang fuerte"
	print "\t\t\t_________*               ____ ____"
    elif line == 8:
	print " linea ying debil"
	print "\t\t\t____ ____                ____ ____"
    elif line == 7:
	print " linea yang debil"
	print "\t\t\t_________                _________"
    elif line == 6:
	print " linea ying fuerte"
	print "\t\t\t____ ____*               _________"
print ""	
print "Leer hexagrama principal y líneas con asteristo del I Ching."
print "La primera línea es la de abajo, la sexta la de arriba."
print "Leer hexagrama transmutado para la mutación o futuro."
    
