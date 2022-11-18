# pierwsze kroki
country = 'usa'
print(country,' ','state')
pi = 3.14
print(pi)
print(pi*2)
print(1,2,3, sep="\n")

#zmienne
text = 'napis to jest'
print(text)
print(text.find('a'))
text_podzielony = text.split(' ')
print(text_podzielony)
print('\n')

#Konkantyncaj stringow
text1 = 'imie'
text2 = 'weronika'
podaj_imie = text1 + ' ' + text2
print(podaj_imie)

#Konwertowanie typow
#na int
liczba1 = '1000'
liczba2 = 2
suma = int(liczba1) - liczba2
print(suma)

#Operatory logiczne
liczba3 = 5
liczba4 = 4
if(liczba3==liczba4):
    print("równe")
else:
    print("różne")
print(float(liczba3/liczba4))

#operacaj na true i false
rowne = True
rowne = liczba3==liczba4
print(rowne)

#sprawdzanie typu
print(type(liczba3))

#potegowanie
print(3**2)

