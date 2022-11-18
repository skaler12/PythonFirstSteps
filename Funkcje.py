def PrintHello():
    print("hello")
    return
PrintHello()

#funkcja z wartoscia domyslna 1
def GiveWarkingDay(year, month, day=1):
    from datetime import date
    from datetime import timedelta

    #day = date(2017,9,30)
    day = date(year,month,day)
    if day.weekday() == 5 :
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6 :
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    return workingday

GiveWarkingDay(2017,9,30)
#jak podam nazwy parametrow to moge je pisac w innej kolejnosci niz w funkcji domyslnie
nextWorkingDay = GiveWarkingDay(day=30, month=9, year=2017)
GiveWarkingDay(2017,9)
print(nextWorkingDay)