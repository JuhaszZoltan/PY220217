import modul as m

# e = m.Ember(1, 'Para Zita', 1994)
# print(f'Az emberemet úgy hívják, hogy {e.nev}')

osztaly = [
    m.Ember(1, 'Kiss Ádám', 1982),
    m.Ember(2, 'Gajdos Gábor', 1970),
    m.Ember(3, 'Varga Viktória', 1988),
    m.Ember(5, 'Dömök Dávid', 2001),
    m.Ember(6, 'Bartha Imola', 1992),
    m.Ember(10, 'Borza Barnabás', 2000),
    m.Ember(4, 'Kalász Nándor', 1977)]

avg = m.atlageletkor(osztaly)
print(f'az osztály átlagéletkora {avg} év')

lf_nev = m.legfiatalabb_ember_neve(osztaly)
print(f'a legfiatalabb az osztályban {lf_nev}')

k = int(input('melyik id-ú osztálytársafat keresed? '))
nev = m.adott_idhoz_tartozo_nev(k, osztaly)
if len(nev) != 0: print(f'{k} id-hoz {nev} nevű ember tartozik')
else: print('nincs ilyen ID az osztályban')

db = m.db_elmult_25(osztaly)
print(f'összesen {db} db hallgató múlt el 25 éves')