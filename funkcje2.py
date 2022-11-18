# sztuczki z funkcjami
# *-oznacza ze jest to kolekcja ktora moze byc kilku wersjowa, ** - odwpanie do dictionary czylk mapy
def DoAction (action, *parameter):
    print("action: ", action)
    print("parameter: ", parameter)
    return

DoAction('buy','shoes','socks')