#Switch w python nie dostepna ale mozna ja zaprogramowac o tak

def WeekDayinPoland(dayNumber) :

    names ={
        0: "poniedzialek",
        1: "wtorek",
        2: "sroda",
        3: "czwartek",
        4: "piatek",
        5: "sobota",
        6: "niedziela"
    }
    return names.get(dayNumber, "error")
print(WeekDayinPoland(4))
print(WeekDayinPoland(8))