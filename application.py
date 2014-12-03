#-*- coding: utf-8-*-
import random # el import random para que me elija numero al azar.
import time # el import time para que tome un cierto tiempo de espera.
import sys # el import sys para que pueda acceder a funciones y objetos que tenga.
import os # el import os para limpiar la consola.

#***************************Instrucciones**************************************#
def Instrucciones():
	print"     ██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ "
	print"     ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗"
	print"     ██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝"
	print"     ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ "
	print"     ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     "
	print"     ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝ "
	print""
	print""" 	- A Cada jugador se le colocara sus barcos en las casillas del tablero 
	- Cada jugador tiene su propio tablero).
	- El tablero de un jugador no puede ser visto por el otro jugador.
	- Al inicio el jugador dice las coordenadas a la cual desea atacar 
	- Si en las coordenadas se encuentra un barco o parte de él, 
	- entonces el barco recibe el daño y el jugador da una nueva coordenada.
	- Si en las coordenadas no se encuentra un barco, 
	- entonces sera el turno del otro jugador y habrá fallado el tiro.
	- Cuando un barco ha recibido un daño en cada casilla que ocupa, 
	- entonces el barco se habrá hundido.
	- Todas las coordenadas se marcan en el tablero, para que no se repitan.
	- Saldra un mensaje diciendo Ya dijiste esa y perdera el turno
	- Cuando un jugador dice sus coordenadas termina su turno.
	- Gana el jugador que hunda primero los barcos de su enemigo."""
#**************************************Termina Instrucciones****************************************#

def Ganador():
	print" 	 _   _              ____                       _          ____                                        "
	print" 	| | | | __ _ ___   / ___| __ _ _ __   __ _  __| | ___    / ___|__ _ _ __ ___  _ __   ___  ___  _ __   "
	print" 	| |_| |/ _` / __| | |  _ / _` | '_ \ / _` |/ _` |/ _ \  | |   / _` | '_ ` _ \| '_ \ / _ \/ _ \| '_ \  "
	print" 	|  _  | (_| \__ \ | |_| | (_| | | | | (_| | (_| | (_) | | |__| (_| | | | | | | |_) |  __/ (_) | | | | "
	print" 	|_| |_|\__,_|___/  \____|\__,_|_| |_|\__,_|\__,_|\___/   \____\__,_|_| |_| |_| .__/ \___|\___/|_| |_| "
	print"                                                                              |_|                     "

def perdedor():
	print"""
\t\t\t███▀▀▀██ ███▀▀▀███ ███▀█▄█▀███ ██▀▀▀
\t\t\t██    ██ ██     ██ ██   █   ██ ██   
\t\t\t██   ▄▄▄ ██▄▄▄▄▄██ ██   ▀   ██ ██▀▀▀
\t\t\t██    ██ ██     ██ ██       ██ ██   
\t\t\t███▄▄▄██ ██     ██ ██       ██ ██▄▄▄

\t\t\t███▀▀▀███ ▀███  ██▀ ██▀▀▀ ██▀▀▀▀██▄
\t\t\t██     ██   ██  ██  ██    ██     ██
\t\t\t██     ██   ██  ██  ██▀▀▀ ██▄▄▄▄▄▀▀
\t\t\t██     ██   ██  █▀  ██    ██     ██
\t\t\t███▄▄▄███    ▀█▀    ██▄▄▄ ██     ██▄
\t\t\t
\t\t\t        ██               ██         
\t\t\t      ████▄   ▄▄▄▄▄▄▄   ▄████       
\t\t\t         ▀▀█▄█████████▄█▀▀          
\t\t\t           █████████████            
\t\t\t           ██▀▀▀███▀▀▀██            
\t\t\t           ██   ███   ██            
\t\t\t           █████▀▄▀█████            
\t\t\t            ███████████             
\t\t\t        ▄▄▄██  █▀█▀█  ██▄▄▄         
\t\t\t        ▀▀██           ██▀▀         
\t\t\t          ▀▀           ▀▀           """

#**************************************Tableros********************************************#
tablero_pc = []
tablero_Usuario_1 = []
tablero_Usuario_2 = []

#**************Tablero_pc**************# 
for a in range(0,10):
	tablero_pc.append(["●"] * 10)

def print_1(tablero_pc):
	for fila in tablero_pc:
		print "\t\t",
		print "   ".join(fila)
#****************************************# 

#**************Tablero_Usuario_1**************# 
for b in range(0,10):
	tablero_Usuario_1.append(["●"] * 10)

def print_2(tablero_Usuario_1):
	for fila1 in tablero_Usuario_1:
		print "\t\t",
		print "   ".join(fila1)
#*********************************************#

#**************Tablero_Usuario_2**************# 
for c in range(0,10):
	tablero_Usuario_2.append(["●"] * 10)

def print_3(tablero_Usuario_2):
	for fila2 in tablero_Usuario_2:
		print "\t\t",
		print "   ".join(fila2)
#*********************************************# 

#**********Barcos y su asignacion*************#
#Haciendo Barcos 
def fila_aleatoria_1(tablero_pc):
	return random.randint(0,len(tablero_pc)-1)

#def fila_aleatoria_1(tablero_pc):
#	fila_barco1 = random.randint(0,8)
#	columna_barco1 = random.randint(0,8)
#	tablero_pc[fila_barco1+1][columna_barco1]=u"⚓"
#	tablero_pc[fila_barco1+2][columna_barco1]=u"⚓"


def columna_aleatoria_1(tablero_pc):
	return random.randint(0,len(tablero_pc[0])-1)

#def columna_aleatoria_1(tablero_pc):
#	fila_barco3 = random.randint(0,5)
#	columna_barco3 = random.randint(0,5)
#	tablero_pc[fila_barco3][columna_barco3+1]=u"⚓"
#	tablero_pc[fila_barco3][columna_barco3+2]=u"⚓"
#	tablero_pc[fila_barco3][columna_barco3+3]=u"⚓"
#	tablero_pc[fila_barco3][columna_barco3+4]=u"⚓"

def fila_aleatoria_2(tablero_pc):
	return random.randint(0,len(tablero_pc[0])-1)

#def fila_aleatoria_2(tablero_pc):
#	fila_barco2 = random.randint(0,7)
#	columna_barco2 = random.randint(0,7)
#	tablero_pc[fila_barco2+1][columna_barco2]=u"⚓"
#	tablero_pc[fila_barco2+2][columna_barco2]=u"⚓"
#	tablero_pc[fila_barco2+3][columna_barco2]=u"⚓"

def columna_aleatoria_2(tablero_pc):
	return random.randint(0,len(tablero_pc[0])-1)

#def columna_aleatoria_2(tablero_pc):
#	fila_barco4 = random.randint(0,7)
#	columna_barco4 = random.randint(0,7)
#	tablero_pc[fila_barco4][columna_barco4+1]=u"⚓"
#	tablero_pc[fila_barco4][columna_barco4+2]=u"⚓"


def fila_aleatoria_3(tablero_pc):
	return random.randint(0,len(tablero_pc[0])-1)

#def fila_aleatoria_3(tablero_Usuario_1):
#	fila_barco5 = random.randint(0,7)
#	columna_barco5 = random.randint(0,7)
#	tablero_Usuario_1[fila_barco5+1][columna_barco5]=u"⚓"
#	tablero_Usuario_1[fila_barco5+2][columna_barco5]=u"⚓"


def columna_aleatoria_3(tablero_pc):
	return random.randint(0,len(tablero_pc[0])-1)

#def columna_aleatoria_3(tablero_Usuario_1):
#	fila_barco7 = random.randint(0,5)
#	columna_barco7 = random.randint(0,5)
#	tablero_Usuario_1[fila_barco7][columna_barco7+1]=u"⚓"
#	tablero_Usuario_1[fila_barco7][columna_barco7+2]=u"⚓"
#	tablero_Usuario_1[fila_barco7][columna_barco7+3]=u"⚓"
#	tablero_Usuario_1[fila_barco7][columna_barco7+4]=u"⚓"


def fila_aleatoria_4(tablero_pc):
	return random.randint(0,len(tablero_pc[0])-1)

#def fila_aleatoria_4(tablero_Usuario_1):
#	fila_barco6 = random.randint(0,7)
#	columna_barco6 = random.randint(0,7)
#	tablero_Usuario_1[fila_barco6+1][columna_barco6]=u"⚓"
#	tablero_Usuario_1[fila_barco6+2][columna_barco6]=u"⚓"
#	tablero_Usuario_1[fila_barco6+3][columna_barco6]=u"⚓"

def columna_aleatoria_4(tablero_pc):
	return random.randint(0,len(tablero_pc[0])-1)

#def columna_aleatoria_4(tablero_Usuario_1):
#	fila_barco8 = random.randint(0,7)
#	columna_barco8 = random.randint(0,7)
#	tablero_Usuario_1[fila_barco8][columna_barco8+1]=u"⚓"
#	tablero_Usuario_1[fila_barco8][columna_barco8+2]=u"⚓"

#asignando los barcos
barco_fila_1 = fila_aleatoria_1(tablero_pc)

barco_columna_1 = columna_aleatoria_1(tablero_pc)

barco_fila_2 = fila_aleatoria_2(tablero_pc)

barco_columna_2 = columna_aleatoria_2(tablero_pc)

barco_fila_3 = fila_aleatoria_3(tablero_pc)

barco_columna_3 = columna_aleatoria_3(tablero_pc)

barco_fila_4 = fila_aleatoria_4(tablero_pc)

barco_columna_4 = columna_aleatoria_4(tablero_pc)

def un_jugador():
	print"   ██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ "
	print"   ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗"
	print"   ██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝"
	print"   ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ "
	print"   ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     "
	print"   ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝ "

	print "\t\t\tProcesando Juego....."
	print ""

	time.sleep(1)
	os.system("clear")

	def letras():
		print"   ██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ "
		print"   ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗"
		print"   ██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝"
		print"   ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ "
		print"   ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     "
		print"   ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝ "

	letras()
	print""
	print"\t\tTablero Al que se Atacara"
	print""
	print_1(tablero_pc)
	turno = 0
	for turno in range(5):
		while True:
			try:
				print""
				adivina_fila = int(raw_input ("\t\tAdivina Coordenada de Fila: "))
				adivina_columna = int(raw_input ("\t\tAdivina Coordenada de Columna: "))
				break
			except (ValueError, NameError):
				print "\t\tSolo Se pueden Ingresar Numero Enteros y dentro de las Coordenadas."
		if (adivina_fila == barco_fila_1 and adivina_columna == barco_columna_1):
			print "\t\t¡Felicitaciones! ¡Hundiste mi barco!"
			turno += 1
			print "\t\tEste Es Tu Turno: ", turno
			tablero_pc[adivina_fila][adivina_columna] = "☠"
					
		elif (adivina_fila == barco_fila_2 and adivina_columna == barco_columna_2):
			print "\t\t¡Felicitaciones! ¡Hundiste mi barco!"
			turno += 1
			print "\t\tEste Es Tu Turno: ", turno
			tablero_pc[adivina_fila][adivina_columna] = "☠"	
			
		elif (adivina_fila == barco_fila_3 and adivina_columna == barco_columna_3):
			print "\t\t¡Felicitaciones! ¡Hundiste mi barco!"
			turno += 1
			print "\t\tEste Es Tu Turno: ", turno
			tablero_pc[adivina_fila][adivina_columna] = "☠"

		elif (adivina_fila == barco_fila_4 and adivina_columna == barco_columna_4):
			print "\t\t¡Felicitaciones! ¡Hundiste mi barco!"
			turno += 1
			print "\t\tEste Es Tu Turno: ", turno
			tablero_pc[adivina_fila][adivina_columna] = "☠"
			if  barcos == 1:
				print "\t\tHas Hundido Todos Mis Barcos"
				undidos = 0
				undidos >= 1
				Ganador()
				time.sleep(3)
				os.system('clear')
				break
				print""
				print_1(tablero_pc)

		else:
			if (adivina_fila < 0 or adivina_fila > 10) or (adivina_columna < 0  or adivina_columna > 10):
				print "\t\tVaya, esto ni siquiera esta en el oceano."
			elif(tablero_pc[adivina_fila][adivina_columna] == "☣" or tablero_pc[adivina_fila][adivina_columna] == "☠"):
				print "\t\tYa dijiste esa."
			else:
				print ""
			while True : 
				try :
					print"\t\tNo Has impactado nada"
					turno += 1
					print "\t\tEste Es Tu Turno: ", turno
					tablero_pc[adivina_fila][adivina_columna] = "☣"
					break
				except (IndexError):
					print "\t\tTu Disparo No Fue dentro del Oceano"
					break
			if turno == 5:
				game = 0
				game == 0
				perdedor()
		time.sleep(2)
		os.system("clear")
		letras()
		print""
		print"\t\t\tTablero Al que se Atacara"
		print""
		print_1(tablero_pc)

#********************************Usuario 1 vs Usuario 2*******************************************************
#**********Barcos y su asignacion*************#
#Haciendo Barcos 
def fila_aleatoria_5(tablero_Usuario_1):
	return random.randint(0,len(tablero_Usuario_1)-1)

def columna_aleatoria_5(tablero_Usuario_1):
	return random.randint(0,len(tablero_Usuario_1[0])-1)

def fila_aleatoria_6(tablero_Usuario_1):
	return random.randint(0,len(tablero_Usuario_1)-1)

def columna_aleatoria_6(tablero_Usuario_1):
	return random.randint(0,len(tablero_Usuario_1[0])-1)

def fila_aleatoria_7(tablero_Usuario_1):
	return random.randint(0,len(tablero_Usuario_1)-1)

def columna_aleatoria_7(tablero_Usuario_1):
	return random.randint(0,len(tablero_Usuario_1[0])-1)

def fila_aleatoria_8(tablero_Usuario_1):
	return random.randint(0,len(tablero_Usuario_1)-1)

def columna_aleatoria_8(tablero_Usuario_1):
	return random.randint(0,len(tablero_Usuario_1[0])-1)

barco_fila_5 = fila_aleatoria_5(tablero_Usuario_1)

barco_columna_5 = columna_aleatoria_5(tablero_Usuario_1)

barco_fila_6 = fila_aleatoria_6(tablero_Usuario_1)

barco_columna_6 = columna_aleatoria_6(tablero_Usuario_1)

barco_fila_7 = fila_aleatoria_7(tablero_Usuario_1)

barco_columna_7 = columna_aleatoria_7(tablero_Usuario_1)

barco_fila_8 = fila_aleatoria_8(tablero_Usuario_1)

barco_columna_8 = columna_aleatoria_8(tablero_Usuario_1)

def fila_aleatoria_9(tablero_Usuario_2):
	return random.randint(0,len(tablero_Usuario_2)-1)

def columna_aleatoria_9(tablero_Usuario_2):
	return random.randint(0,len(tablero_Usuario_2[0])-1)

def fila_aleatoria_10(tablero_Usuario_2):
	return random.randint(0,len(tablero_Usuario_2)-1)

def columna_aleatoria_10(tablero_Usuario_2):
	return random.randint(0,len(tablero_Usuario_2[0])-1)

def fila_aleatoria_11(tablero_Usuario_2):
	return random.randint(0,len(tablero_Usuario_2)-1)

def columna_aleatoria_11(tablero_Usuario_2):
	return random.randint(0,len(tablero_Usuario_2[0])-1)

def fila_aleatoria_12(tablero_Usuario_2):
	return random.randint(0,len(tablero_Usuario_2)-1)

def columna_aleatoria_12(tablero_Usuario_2):
	return random.randint(0,len(tablero_Usuario_2[0])-1)

barco_fila_9 = fila_aleatoria_9(tablero_Usuario_2)

barco_columna_9 = columna_aleatoria_9(tablero_Usuario_2)

barco_fila_10 = fila_aleatoria_10(tablero_Usuario_2)

barco_columna_10 = columna_aleatoria_10(tablero_Usuario_2)

barco_fila_11 = fila_aleatoria_11(tablero_Usuario_2)

barco_columna_11 = columna_aleatoria_11(tablero_Usuario_2)

barco_fila_12 = fila_aleatoria_12(tablero_Usuario_2)

barco_columna_12 = columna_aleatoria_12(tablero_Usuario_2)
#********************************Usuario 1 vs Usuario 2*******************************************************
def multijugador():
	print"\t\t████████ ██    ██ ██████  ███    ██  ██████           ██ ██    ██  ██████   █████  ██████   ██████  ██████       ██ "
	print"\t\t   ██    ██    ██ ██   ██ ████   ██ ██    ██          ██ ██    ██ ██       ██   ██ ██   ██ ██    ██ ██   ██     ███ "
	print"\t\t   ██    ██    ██ ██████  ██ ██  ██ ██    ██          ██ ██    ██ ██   ███ ███████ ██   ██ ██    ██ ██████       ██ "
	print"\t\t   ██    ██    ██ ██   ██ ██  ██ ██ ██    ██     ██   ██ ██    ██ ██    ██ ██   ██ ██   ██ ██    ██ ██   ██      ██ "
	print"\t\t   ██     ██████  ██   ██ ██   ████  ██████       █████   ██████   ██████  ██   ██ ██████   ██████  ██   ██      ██ "
	print"\t\t                                                                                                                    "

	print""
	Nombre_Jugador = raw_input("Nombre De Jugador No.1: ")
	print"\t\tTablero" , Nombre_Jugador
	print_2(tablero_Usuario_1)
	print""
	Nombre_Jugador_2 = raw_input("Nombre De Jugador No.2: ")
	print"\t\tTablero" ,Nombre_Jugador_2
	print_3(tablero_Usuario_2)
	turno = 0
	for turno in range(5):
		while True:
			try:
				print""
				adivina_fila = int(raw_input ("\t\tAdivina Coordenada de Fila: "))
				adivina_columna = int(raw_input ("\t\tAdivina Coordenada de Columna: "))
				break
			except (ValueError, NameError):
				print "\t\tSolo Se pueden Ingresar Numero Enteros y dentro de las Coordenadas."
		if (adivina_fila == barco_fila_5 and adivina_columna == barco_columna_5):
			print "\t\t¡Felicitaciones! ¡Hundiste mi barco!"
			turno += 1
			print "\t\tEste Es Tu Turno: ", turno
			tablero_Usuario_2[adivina_fila][adivina_columna] = "☠"
					
		elif (adivina_fila == barco_fila_6 and adivina_columna == barco_columna_6):
			print "\t\t¡Felicitaciones! ¡Hundiste mi barco!"
			turno += 1
			print "\t\tEste Es Tu Turno: ", turno
			tablero_Usuario_2[adivina_fila][adivina_columna] = "☠"	
			
		elif (adivina_fila == barco_fila_7 and adivina_columna == barco_columna_7):
			print "\t\t¡Felicitaciones! ¡Hundiste mi barco!"
			turno += 1
			print "\t\tEste Es Tu Turno: ", turno
			tablero_Usuario_2[adivina_fila][adivina_columna] = "☠"

		elif (adivina_fila == barco_fila_8 and adivina_columna == barco_columna_8):
			print "\t\t¡Felicitaciones! ¡Hundiste mi barco!"
			turno += 1
			print "\t\tEste Es Tu Turno: ", turno
			tablero_Usuario_2[adivina_fila][adivina_columna] = "☠"
			if  barcos == 1:
				print "\t\tHas Hundido Todos Mis Barcos"
				time.sleep(3)
				os.system('clear')
				break
				print""
				print_3(tablero_Usuario_2)

		else:
			if (adivina_fila < 0 or adivina_fila > 10) or (adivina_columna < 0  or adivina_columna > 10):
				print "\t\tVaya, esto ni siquiera esta en el oceano."
			elif(tablero_Usuario_2[adivina_fila][adivina_columna] == "☣" or tablero_Usuario_2[adivina_fila][adivina_columna] == "☠"):
				print "\t\tYa dijiste esa."
			else:
				print ""
			while True : 
				try :
					print"\t\tNo Has impactado nada"
					turno += 1
					print "\t\tEste Es Tu Turno: ", turno
					tablero_Usuario_2[adivina_fila][adivina_columna] = "☣"
					break
				except (IndexError):
					print "\t\tTu Disparo No Fue dentro del Oceano"
					break
			if turno == 5:
				time.sleep(2)
				os.system("clear")
				print""
				print"	Tablero" , Nombre_Jugador
				print_2(tablero_Usuario_1)
				print""
				print"	Tablero" ,Nombre_Jugador_2
				print_3(tablero_Usuario_2)


	print"\t\t████████ ██    ██ ██████  ███    ██  ██████           ██ ██    ██  ██████   █████  ██████   ██████  ██████      ██████  "
	print"\t\t   ██    ██    ██ ██   ██ ████   ██ ██    ██          ██ ██    ██ ██       ██   ██ ██   ██ ██    ██ ██   ██          ██ "
	print"\t\t   ██    ██    ██ ██████  ██ ██  ██ ██    ██          ██ ██    ██ ██   ███ ███████ ██   ██ ██    ██ ██████       █████  "
	print"\t\t   ██    ██    ██ ██   ██ ██  ██ ██ ██    ██     ██   ██ ██    ██ ██    ██ ██   ██ ██   ██ ██    ██ ██   ██     ██      "
	print"\t\t   ██     ██████  ██   ██ ██   ████  ██████       █████   ██████   ██████  ██   ██ ██████   ██████  ██   ██     ███████ "
	

	print""
	print"	Tablero" ,Nombre_Jugador_2
	print_3(tablero_Usuario_2)	
	print""
	print"	Tablero" , Nombre_Jugador
	print_2(tablero_Usuario_1)
	print""
	turno = 0
	for turno in range(5):
		while True:
			try:
				print""
				adivina_fila = int(raw_input ("\t\tAdivina Coordenada de Fila: "))
				adivina_columna = int(raw_input ("\t\tAdivina Coordenada de Columna: "))
				break
			except (ValueError, NameError):
				print "\t\tSolo Se pueden Ingresar Numero Enteros y dentro de las Coordenadas."
		if (adivina_fila == barco_fila_9 and adivina_columna == barco_columna_9):
			print "\t\t¡Felicitaciones! ¡Hundiste mi barco!"
			turno += 1
			print "\t\tEste Es Tu Turno: ", turno
			tablero_Usuario_1[adivina_fila][adivina_columna] = "☠"
					
		elif (adivina_fila == barco_fila_10 and adivina_columna == barco_columna_10):
			print "\t\t¡Felicitaciones! ¡Hundiste mi barco!"
			turno += 1
			print "\t\tEste Es Tu Turno: ", turno
			tablero_Usuario_1[adivina_fila][adivina_columna] = "☠"	
			
		elif (adivina_fila == barco_fila_11 and adivina_columna == barco_columna_11):
			print "\t\t¡Felicitaciones! ¡Hundiste mi barco!"
			turno += 1
			print "\t\tEste Es Tu Turno: ", turno
			tablero_Usuario_1[adivina_fila][adivina_columna] = "☠"

		elif (adivina_fila == barco_fila_12 and adivina_columna == barco_columna_12):
			print "\t\t¡Felicitaciones! ¡Hundiste mi barco!"
			turno += 1
			print "\t\tEste Es Tu Turno: ", turno
			tablero_Usuario_1[adivina_fila][adivina_columna] = "☠"
			if  barcos == 1:
				print "\t\tHas Hundido Todos Mis Barcos"
				time.sleep(3)
				os.system('clear')
				break
				print""
				print_2(tablero_Usuario_1)

		else:
			if (adivina_fila < 0 or adivina_fila > 10) or (adivina_columna < 0  or adivina_columna > 10):
				print "\t\tVaya, esto ni siquiera esta en el oceano."
			elif(tablero_Usuario_1[adivina_fila][adivina_columna] == "☣" or tablero_Usuario_1[adivina_fila][adivina_columna] == "☠"):
				print "\t\tYa dijiste esa."
			else:
				print ""
			while True : 
				try :
					print"\t\tNo Has impactado nada"
					turno += 1
					print "\t\tEste Es Tu Turno: ", turno
					tablero_Usuario_1[adivina_fila][adivina_columna] = "☣"
					break
				except (IndexError):
					print "\t\tTu Disparo No Fue dentro del Oceano"
					break
			if turno == 5:
				time.sleep(2)
				os.system("clear")
				print"	Tablero" ,Nombre_Jugador_2
				print_3(tablero_Usuario_2)
				print""
				print"	Tablero" , Nombre_Jugador
				print_2(tablero_Usuario_1)

#************************************Menu**********************************************************#
class menu():
	op_menu=True
	while op_menu==True:
		print"  	  ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄   ███    █▄  "
		print"  	▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄ ███    ███ "
		print"  	███   ███   ███   ███    █▀  ███   ███ ███    ███ "
		print"  	███   ███   ███  ▄███▄▄▄     ███   ███ ███    ███ "
		print"  	███   ███   ███ ▀▀███▀▀▀     ███   ███ ███    ███ "
		print"  	███   ███   ███   ███    █▄  ███   ███ ███    ███ "
		print"  	███   ███   ███   ███    ███ ███   ███ ███    ███ "
		print"  	 ▀█   ███   █▀    ██████████  ▀█   █▀  ████████▀ "
		print"  	                                                  "
		print"                                                    "
		print"		1) Instucciones"
		print"		2) Hundiendo Barcos: "
		print"		3) Multiplayer: "
		print"		4) Jugador 1 vs PC:"
		print""
		opcion_menu=raw_input("		Que opcion Desea Realizar: ")
		print ""
		print ""
		try:
			if opcion_menu.isalpha()==False:
				os.system("clear")
				if opcion_menu.lower()=="1":
					Instrucciones()
					validar=True
					while validar==True:
						print""
						volver=raw_input("		Desea volver al Menu Si/No: ")
						print""
						try:
							if volver.isalpha()==True:
								if volver.lower()=="si":
									validar=False
								elif volver.lower()=="no":
									op_menu=False
									print "Adios"
									break
							else:
								print "		Dato No valido."
						except:
							print "No se Aceptan Datos Numericos."
		except:
			print "Adios"
		os.system("clear")
		try:
			if opcion_menu.isalpha()==False:
				if opcion_menu.lower()=="2":
					un_jugador()
					validar=True
					while validar==True:
						print""
						volver=raw_input("\t\tDesea volver al Menu Si/No: ")
						print ""
						try:
							if volver.isalpha()==True:
								if volver.lower()=="si":
									validar=False
								elif volver.lower()=="no":
									op_menu=False
									print "Adios"
									break
							else:
								print "Dato No Valido."
						except:
							print "No se Aceptan Datos Numericos."
		except:
			print"Adios"
		os.system("clear")
		try:
			if opcion_menu.isalpha()==False:
				if opcion_menu.lower()=="3":
					multijugador()
					validar=True
					while validar==True:
						print""
						volver=raw_input("Desea volver al Menu Si/No: ")
						print""
						try:
							if volver.isalpha()==True:
								if volver.lower()=="si":
									validar=False
								elif volver.lower()=="no":
									op_menu=False
									print "Adios"
									break
							else:
								print "Dato No Valido."
						except:
							print "No se Aceptan Datos Numericos."
		except:
			print "Adios."
		os.system("clear")
		try:
			if opcion_menu.isalpha()==False:
				if opcion_menu.lower()=="4":
					vs_pc()
					validar=True
					while validar==True:
						print"" 
						volver=raw_input("Desea volver al Menu Si/No: ")
						print""
						try:
							if volver.isalpha()==True:
								if volver.lower()=="si":
									validar=False
								elif volver.lower()=="no":
									op_menu=False
									print "Adios"
									break
							else:
								print "Dato No Valido."
						except:
							print "No se Aceptan Datos Numericos."
		except:
			print "Adios."
menu()
#*****************************Termina Menu***********************************#