class Ember:
    def __init__ (self, id, nev, szul):
        self.id = int(id)
        self.nev = nev
        self.szul = int(szul)


def atlageletkor(emberek):
    ossz_eletkor = 0
    for e in emberek:
        ossz_eletkor += (2022 - e.szul)
    return round(ossz_eletkor / len(emberek), 2)


def legfiatalabb_ember_neve(emberek):
    maxi = 0
    for i in range(1, len(emberek)):
        if emberek[i].szul > emberek[maxi].szul:
            maxi = i
    return emberek[maxi].nev


def adott_idhoz_tartozo_nev(keresett_id, emberek):
    i = 0
    while i < len(emberek) and emberek[i].id != keresett_id:
        i += 1
    if i < len(emberek): return emberek[i].nev
    else: return ''


def db_elmult_25(emberek):
    db = 0
    for e in emberek:
        if (2022 - e.szul) > 25: db += 1
    return db