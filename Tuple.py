#tuple , krotka
#tuple jest niezmienne, stale, aby zmienaic trzeba konwertowac na liste

tax = (12,3,4)
print(tax)
print(tax[1])
#ostatnia pozycja na tuple
print(tax[-1])
#wartosc max
print(max(tax))

#konwertowanie taple na liste - po to bo w taple nie mozemy nic edytowac
taxList = list(tax)
print(taxList)
taxList.append(20)

Newtax = tuple(taxList)
print(Newtax)


