import osmnx as ox

lugar = "Maputo"

# numero de agregado familiar publicado em 2020
agreFamiliar = 4.8 

# pegar casas
casas = ox.geometries_from_place(lugar, tags={"building": True})

# nr total de casas
totalCasas = len(casas)

# instrucao para o calculo da populacao 
popTotal = totalCasas*agreFamiliar

print("Casas: ", totalCasas)
print("Populacao: ", popTotal)