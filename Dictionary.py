#dictionary - slowniki - takie mapy
Country_Leaders = {'PL':'Duda', 'USA':'Trump'}
print(Country_Leaders)

Country_Leaders ['DE'] = 'Merkel'
print(Country_Leaders)

#wywietlanie klcuzy , wartosci oraz kluczy i wartosci
print(Country_Leaders.keys())
print(Country_Leaders.values())
print(Country_Leaders.items())

#ustawnienie wartosci domyslych
print(Country_Leaders.setdefault('FR','Macron'))

