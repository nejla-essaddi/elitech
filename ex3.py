n=int(input("donnez n"))
ListeC=[]
for i in range(n):
	d=dict()
	nom=input("donnez nom")
	d["nom"]=nom

	age=int(input("donnez age"))
	d["age"]=age
	taille=float(input("donnez taille"))
	d["taille"]=taille
	ListeC.append(d)
	print(d)
print(ListeC)
no=input("nom à chercher")
ageno=0
tailleno=0
for i in range(n):
	if no == ListeC[i]["nom"]:
		ageno=ListeC[i]["age"]
		tailleno=ListeC[i]["taille"]
if ageno!=0 :
	print("Nom :", no," - age : ", ageno," ans - taille :", tailleno, "m")
else :
	print(no,"non trouvé")
		