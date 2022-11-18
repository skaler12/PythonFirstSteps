#petle

i = 1
imax = 10
while  i<=imax:
    print(i)
    i=i+1
#mozemy dodac blok else
else:
    print("i jest równe = ", i)

lista = ['maciek', 'amelia', 'weronika']

email = []
for osoba in lista:
    email_osoba= ''
    email_osoba = osoba + '@gmail.com'
    if len(email_osoba) < 13:
        break
    if len(email_osoba) > 17:
        continue
    email.append(email_osoba)
print(email)


