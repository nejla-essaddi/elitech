
try:
	a = input("Entrer un nombre: ")
	b = input("Entrer un nombre: ")
	S=float(a)/float(b)
	print (S)
except  ZeroDivisionError:
	print ("Division par 0 interdite...")	
	b=2
	S=float(a)/float(b)
	print (S)
except  ValueError:
	print ("Type non convertible")	
except  :
	print ("Erreur inconnue")
	
print("reste du programme")
