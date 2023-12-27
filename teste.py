C = int(input()) 

for i in range (C): 
    refrigerantes_comprados = int(input("Quantidade de refrigerantes comprados:"))
    garrafas_vazias = int(input("Quantidade de garrafas vazias:"))
    if garrafas_vazias > refrigerantes_comprados:
        saida = refrigerantes_comprados
    else:
        quociente = refrigerantes_comprados//garrafas_vazias
        resto = refrigerantes_comprados % garrafas_vazias
        saida = quociente + resto
    print(saida)