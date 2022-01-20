from Processing import identifikasiKolomByTabel, isPerintah, identifikasiTabel, identifikasiKondisi
from WordList import getDaftarKolomByTabel, getDaftarTable


def listToString(list):
    result = ""
    for item in list:
        result += item
    return result


def queryForming(token):
    sqlPart = []
    indeksSQL = 0

    isKalimatPerintah = isPerintah(token)
    daftarTabel = identifikasiTabel(token)
    daftarKolom = identifikasiKolomByTabel(token)

# ? queryPart SELECT
    if isKalimatPerintah == False:
        return("tidak ada perintah SELECT")
    else:
        sqlPart.insert(indeksSQL, "SELECT ")
        indeksSQL += 1
    if len(daftarTabel) == 0:
        return("tidak ada tabel teridentifikasi")

# ?  queryPart Tabel
    indeksKoma = 1
    for w in token:
        for t in daftarTabel:
            if w in getDaftarKolomByTabel(t) and indeksKoma < len(daftarKolom):
                sqlPart.insert(indeksSQL, f"{t}.{w}, ")
                indeksKoma += 1
                indeksSQL += 1
            elif w in getDaftarKolomByTabel(t) and indeksKoma == len(daftarKolom):
                sqlPart.insert(indeksSQL, f"{t}.{w} ")
                indeksSQL += 1

# ? queryPart Kolom
    if daftarKolom[0] == '*':
        sqlPart.insert(indeksSQL, f"* ")
        indeksSQL += 1
    if len(daftarTabel) > 0:
        sqlPart.insert(indeksSQL, f"FROM ")
        indeksSQL += 1
    indeksKoma = 1
    if len(daftarTabel) == 1:
        sqlPart.insert(indeksSQL, f"{daftarTabel[0]} ")
        indeksSQL += 1
    else:
        for w in getDaftarTable():
            if indeksKoma < len(daftarTabel):
                sqlPart.insert(indeksSQL, f"{w}, ")
                indeksKoma += 1
                break
            elif indeksKoma == len(daftarTabel):
                sqlPart.insert(indeksSQL, f"{w} ")
                indeksKoma += 1
            indeksSQL += 1

# ? result query
    result = listToString(sqlPart)

    return(result)
