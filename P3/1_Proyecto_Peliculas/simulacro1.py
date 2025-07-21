lista=[]
if len(lista)==0:
    resp="si"
    while resp=="si":
        lista.append(input("Dame la frase: ").upper())
        resp=input("¿Desea solicitar otra frase? (si/no)").lower().strip()

print(lista)
       