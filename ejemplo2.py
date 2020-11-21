print("Ejercicio en python")
def medir(frase):
	dir={}
	frase=frase.split()
	for i in frase:
		dic[i]=len(i)
	print(dic)

texto=input("Ingresa una frase")
medir(texto)
print("Fin")
