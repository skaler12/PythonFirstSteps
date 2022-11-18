#lista
lista = ['jablko','gruszka','pomarancza']
print(lista)

#wyswietlanie elementow listy
print(lista[0])

#dodawanie elementow
lista.append('cytryna')
print(lista)
#dodawnie na konkretne pozycje
lista.insert(2,'wisnia')
print(lista)

#usuwanie elementow
lista.remove(lista[1])
print(lista)

#sortownia
lista.sort()
print(lista)

#sprawdzanie indeksu
print(lista.index('wisnia'))

#kopiownie listy
lista2 = lista.copy()
print(lista2)

#czyszczenie listy
lista2.clear()
print(lista2)
print(lista)