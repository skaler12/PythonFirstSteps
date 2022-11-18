age = 19
isTrzezwy = True

if age<18 and isTrzezwy:
    print('za mlody')
elif age>=18 and not isTrzezwy:
    print('nie kupuj alko jestes pijany')
elif age<18 and not isTrzezwy:
    print('za mlody i pijany')
else:
    print('kupuj alko!')