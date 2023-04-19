carros = ['corola', 'gol', 'ferrari', 'ethos', 'mustang', 'ford']

#fatiar a lista :
# print(carros[2:5])

#carros[primeiro elemento : ultimo elemento] // vai se comportar igual o range()

#copiar listas:

alimentos = ['carne','frango','tomate','alface','melancia','feijao','arroz']
alimentos2 = alimentos

# se eu fizer assim ^ eu estarei copiando todos os elementos e quaisquer alterações que fizer daqui pra frente
#se eu quiser só copiar ela nesse exato ponto, eu fatio ela:

alimentos_copiados = alimentos[:] #esse ':' é para copiar toda a lista

#vou fazer uma mudança na lista principal 'alimentos' e vamos ver a diferença

alimentos.append('hamburger')
alimentos.sort()

print(alimentos)
print(alimentos2)
print(alimentos_copiados)