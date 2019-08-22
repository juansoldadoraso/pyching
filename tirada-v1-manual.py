#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""for random(100)
	if random > 50
		yang
	else
		ying
return 0 or 1"""
#formacion del hexagrama(que son seis lineas una sobre otra)
cadenaiching = "I Ching"
print cadenaiching.center(70, "=")
print " Dijo el Maestro ¿no es el libro de las mutaciones lo Supremo?."
print " El Libro de las Mutaciones es la obra mediante la cual los sabios"
print " santos elevaron su modo de ser y ampliaron su campo de accion."
print ""
print "Primera tirada de seis, linea inferior del hexagrama "
print "Coje tres monedas iguales y a un lado le asignas valor 2 y al otro 3"
print "Tira las monedas y suma los valores, solo pueden ser 6,7,8 y 9"
linea1 = input ('Inserta el valor de la suma de las tres monedas: ')
print ""
print "Segunda tirada..."
linea2 = input ('Inserta el valor de la suma de las tres monedas: ')
print ""
print "Tercera tirada..."
linea3 = input ('Inserta el valor de la suma de las tres monedas: ')
print ""
print "Cuarta tirada..."
linea4 = input ('Inserta el valor de la suma de las tres monedas: ')
print ""
print "Quinta tirada..."
linea5 = input ('Inserta el valor de la suma de las tres monedas: ')
print ""
print "Sexta tirada..."
linea6 = input ('Inserta el valor de la suma de las tres monedas: ')
print ""
#linea1 = self.assert_(True, 'message')
"""listaching = [6,7,8,9]
trigramainf = [linea1,linea2,linea3]
trigramasup = [linea4,linea5,linea6]"""
#Tipos de tirada fuerte o debil
yangf = "_______" #9
yingf = "___ ___" #6
yangd = "_______" #7
yingd = "___ ___" #8
basicyang = 7
basicying = 6
trigramainf = []
trigramasup = []
#trigramas inferiores
if linea1 == 9 or linea1 == 7:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 9 or linea3 == 7:
			print "Trigrama inferior Chien"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 9 or linea1 == 7:
	if linea2 == 8 or linea2 == 6:
		if linea3 == 8 or linea3 == 6:
			print "Trigrama inferior Chen"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 8 or linea1 == 6:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 8 or linea3 == 6:
			print "Trigrama inferior K'an"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 8 or linea1 == 6:
	if linea2 == 8 or linea2 == 6:
		if linea3 == 9 or linea3 == 7:
			print "Trigrama inferior Ken"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 8 or linea1 == 6:
	if linea2 == 8 or linea2 == 6:
		if linea3 == 8 or linea3 == 6:
			print "Trigrama inferior K'un"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 8 or linea1 == 6:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 9 or linea3 == 7:
			print "Trigrama inferior Sun"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 9 or linea1 == 7:
	if linea2 == 8 or linea2 == 6:
		if linea3 == 9 or linea3 == 7:
			print "Trigrama inferior Li"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
if linea1 == 9 or linea1 == 7:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 8 or linea3 == 6:
			print "Trigrama inferior Tui"
			trigramainf = [linea1,linea2,linea3]
			print trigramainf
			print ""
#
if linea4 == 9 or linea4 == 7:
	if linea5 == 9 or linea5 == 7:
		if linea6 == 9 or linea6 == 7:
			print "Trigrama superior Ch'ien"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
#
if linea4 == 9 or linea4 == 7:
	if linea5 == 8 or linea5 == 6:
		if linea6 == 8 or linea6 == 6:
			print "Trigrama superior Chen"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
if linea4 == 8 or linea4 == 6:
	if linea5 == 9 or linea5 == 7:
		if linea6 == 8 or linea6 == 6:
			print "Trigrama superior K'an"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
if linea4 == 8 or linea4 == 6:
	if linea5 == 8 or linea5 == 6:
		if linea6 == 9 or linea6 == 7:
			print "Trigrama superior Ken"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
if linea4 == 8 or linea4 == 6:
	if linea5 == 8 or linea5 == 6:
		if linea6 == 8 or linea6 == 6:
			print "Trigrama superior K'un"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
if linea4 == 8 or linea4 == 6:
	if linea5 == 9 or linea5 == 7:
		if linea6 == 9 or linea6 == 7:
			print "Trigrama superior Sun"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
if linea4 == 9 or linea4 == 7:
	if linea5 == 8 or linea5 == 6:
		if linea6 == 9 or linea6 == 7:
			print "Trigrama superior Li"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
if linea4 == 9 or linea4 == 7:
	if linea5 == 9 or linea5 == 7:
		if linea6 == 8 or linea6 == 6:
			print "Trigrama superior Tui"
			trigramasup = [linea4,linea5,linea6]
			print trigramasup
			print ""
#
if linea6 == 9 :
	print "9 _______"
elif linea6 == 7 :
	print "7 _______"
elif linea6 == 6 :
	print "6 ___ ___"
elif linea6 == 8 :
	print "8 ___ ___"
else :
	print "Valor erroneo"
#
if linea5 == 9 :
	print "9 _______"
elif linea5 == 7 :
	print "7 _______"
elif linea5 == 6 :
	print "6 ___ ___"
elif linea5 == 8 :
	print "8 ___ ___"
else :
	print "Valor erroneo"
#
if linea4 == 9 :
	print "9 _______"
elif linea4 == 7 :
	print "7 _______"
elif linea4 == 6 :
	print "6 ___ ___"
elif linea4 == 8 :
	print "8 ___ ___"
else :
	print "Valor erroneo"
#
if linea3 == 9 :
	print "9 _______"
elif linea3 == 7 :
	print "7 _______"
elif linea3 == 6 :
	print "6 ___ ___"
elif linea3 == 8 :
	print "8 ___ ___"
else :
	print "Valor erroneo"
#
if linea2 == 9 :
	print "9 _______"
elif linea2 == 7 :
	print "7 _______"
elif linea2 == 6 :
	print "6 ___ ___"
elif linea2 == 8 :
	print "8 ___ ___"
else :
	print "Valor erroneo"
#
if linea1 == 9 :
	print "9 _______"
elif linea1 == 7 :
	print "7 _______"
elif linea1 == 6 :
	print "6 ___ ___"
elif linea1 == 8 :
	print "8 ___ ___"
else :
	print "Valor erroneo"
print ""
#hexagrama principal
sign_lineas = '''Las líneas se cuentan desde abajo hacia arriba. El trazo
del comienzo es, pues, el de más abajo. Si el consultante obtiene
un siete, se trata por cierto de un trazo fuerte que se toma
en consideración en cuanto a la estructura del signo en su
totalidad, pero este trazo no se mueve y no tiene, por tanto,
significación individual. Si en cambio, el consultante obtiene 
un nueve, el trazo se mueve, destacándose con ello su significación
peculiar y debiendo tenérselo en cuenta y meditarse sobre él, en
calidad de trazo individual. Lo mismo vale en cuanto a las demás líneas
fuertes en todo el libro. En cada uno de los hexagramas las dos
líneas de abajo significan la tierra, las del medio la región
del mundo humano, las de arriba el cielo.'''
#Ch'ien -Lo Creativo
if linea1 == 9 or linea1 == 7:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 9 or linea3 == 7:
			if linea4 == 9 or linea4 == 7:
				if linea5 == 9 or linea5 == 7:
					if linea6 == 9 or linea6 == 7:
						print "Hexagrama 1. Ch'ien, Lo Creativo\n"
						file1 = open("./db/1.txt", 'r')
						contenido1 = file1.read()
						print (contenido1)
						file1.close()
						print ""
						print (sign_lineas)
						print ""
if linea1 == 9:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 9 or linea3 == 7:
			if linea4 == 9 or linea4 == 7:
				if linea5 == 9 or linea5 == 7:
					if linea6 == 9 or linea6 == 7:
						file1_1 = open("./db/1_1.txt", 'r')
						conlin1 = file1_1.read()
						print "Significado de la primera linea: \n"
						print (conlin1)
						file1_1.close()
if linea1 == 9 or linea1 == 7:
	if linea2 == 9:
		if linea3 == 9 or linea3 == 7:
			if linea4 == 9 or linea4 == 7:
				if linea5 == 9 or linea5 == 7:
					if linea6 == 9 or linea6 == 7:
						file1_2 = open("./db/1_2.txt", 'r')
						conlin2 = file1_2.read()
						print "Significado de la segunda linea: \n"
						print (conlin2)
						file1_2.close()
if linea1 == 9 or linea1 == 7:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 9:
			if linea4 == 9 or linea4 == 7:
				if linea5 == 9 or linea5 == 7:
					if linea6 == 9 or linea6 == 7:
						file1_3 = open("./db/1_3.txt", 'r')
						conlin3 = file1_3.read()
						print "Significado de la tercera linea: \n"
						print (conlin3)
						file1_3.close()
if linea1 == 9 or linea1 == 7:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 9 or linea3 == 7:
			if linea4 == 9:
				if linea5 == 9 or linea5 == 7:
					if linea6 == 9 or linea6 == 7:
						file1_4 = open("./db/1_4.txt", 'r')
						conlin4 = file1_4.read()
						print "Significado de la cuarta linea: \n"
						print (conlin4)
					file1_4.close()
if linea1 == 9 or linea1 == 7:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 9 or linea3 == 7:
			if linea4 == 9 or linea4 == 7:
				if linea5 == 9:
					if linea6 == 9 or linea6 == 7:
						file1_5 = open("./db/1_5.txt", 'r')
						conlin5 = file1_5.read()
						print "Significado de la quinta linea: \n"
						print (conlin5)
					file1_5.close()
if linea1 == 9 or linea1 == 7:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 9 or linea3 == 7:
			if linea4 == 9 or linea4 == 7:
				if linea5 == 9 or linea5 == 7:
					if linea6 == 9:
						file1_6 = open("./db/1_6.txt", 'r')
						conlin6 = file1_6.read()
						print "Significado de la sexta linea: \n"
						print (conlin6)
						file1_6.close()
if linea1 == 9 and linea2 == 9 and linea3 == 9 and linea4 == 9 and linea5 == 9 and linea6 == 9:
	file1_7 = open("./db/1_7.txt", 'r')
	conlin7 = file1_7.read()
	print "Significado si todas las líneas son 9 : \n"
	print (conlin7)
	file1_7.close()	
#K'un -Lo Receptivo
if linea1 == 8 or linea1 == 6:
	if linea2 == 8 or linea2 == 6:
		if linea3 == 8 or linea3 == 6:
			if linea4 == 8 or linea4 == 6:
				if linea5 == 8 or linea5 == 6:
					if linea6 == 8 or linea6 == 6:
						print "Hexagrama 2. K'un, Lo Receptivo"
						file2 = open("./db/2.txt", 'r')
						contenido2 = file2.read()
						print (contenido2)
						file2.close()
						print ""
						print (sign_lineas)
						print ""
#Chun -La dificultad inicial
if linea1 == 9 or linea1 == 7:
	if linea2 == 8 or linea2 == 6:
		if linea3 == 8 or linea3 == 6:
			if linea4 == 8 or linea4 == 6:
				if linea5 == 9 or linea5 == 7:
					if linea6 == 8 or linea6 == 6:
						print "Hexagrama 3. Chun, La Dificultad Inicial"

#Meng - La Necedad Juvenil
if linea1 == 8 or linea1 == 6:
	if linea2 == 9 or linea2 == 7:
		if linea3 == 8 or linea3 == 6:
			if linea4 == 8 or linea4 == 6:
				if linea5 == 8 or linea5 == 6:
					if linea6 == 9 or linea6 == 7:
						print "Hexagrama 4. Meng, La Necedad Juvenil"
						
#Hexagrama mutado
print "Tu hexagrama mutado es : \n"
if linea6 == 9 :
	print " ___ ___"
elif linea6 == 7 :
	print " _______"
elif linea6 == 6 :
	print " _______"
elif linea6 == 8 :
	print " ___ ___"
else :
	print "Valor erroneo"
#
if linea5 == 9 :
	print " ___ ___"
elif linea5 == 7 :
	print " _______"
elif linea5 == 6 :
	print " _______"
elif linea5 == 8 :
	print " ___ ___"
else :
	print "Valor erroneo"
#
if linea4 == 9 :
	print " ___ ___"
elif linea4 == 7 :
	print " _______"
elif linea4 == 6 :
	print " _______"
elif linea4 == 8 :
	print " ___ ___"
else :
	print "Valor erroneo"
#
if linea3 == 9 :
	print " ___ ___"
elif linea3 == 7 :
	print " _______"
elif linea3 == 6 :
	print " _______"
elif linea3 == 8 :
	print " ___ ___"
else :
	print "Valor erroneo"
#
if linea2 == 9 :
	print " ___ ___"
elif linea2 == 7 :
	print " _______"
elif linea2 == 6 :
	print " _______"
elif linea2 == 8 :
	print " ___ ___"
else :
	print "Valor erroneo"
#
if linea1 == 9 :
	print " ___ ___"
elif linea1 == 7 :
	print " _______"
elif linea1 == 6 :
	print " _______"
elif linea1 == 8 :
	print " ___ ___"
else :
	print "Valor erroneo"
print ""

if linea1 == 9:
	linea1 = 8
if linea1 == 6:
	linea1 = 7
if linea2 == 9:
	linea2 = 8
if linea2 == 6:
	linea2 = 7
if linea3 == 9:
	linea3 = 8
if linea3 == 6:
	linea3 = 7
if linea4 == 9:
	linea4 = 8
if linea4 == 6:
	linea4 = 7
if linea5 == 9:
	linea5 = 8
if linea5 == 6:
	linea5 = 7
if linea6 == 9:
	linea6 = 8
if linea6 == 6:
	linea6 = 7
#Ch'ien -Lo Creativo
if linea1 == 7:
	if linea2 == 7:
		if linea3 == 7:
			if linea4 == 7:
				if linea5 == 7:
					if linea6 == 7:
						print "Hexagrama 1. Ch'ien, Lo Creativo\n"
						file1 = open("./db/1.txt", 'r')
						contenido1 = file1.read()
						print (contenido1)
						file1.close()
						print ""
