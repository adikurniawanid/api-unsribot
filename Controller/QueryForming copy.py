from Controller.Processing import identifikasiKolomByTabel, isPerintah, identifikasiTabel, identifikasiKondisi, identifikasiKolomKondisi, identifikasiOperatorLogika
from Controller.WordList import getDaftarKolomByTabel, getDaftarKondisi, getDaftarTable


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
    if isKalimatPerintah:
        sqlPart.insert(indeksSQL, "SELECT ")
        indeksSQL += 1
    else:
        return("tidak ada kalimat perintah terindentifikasi")

    if len(daftarTabel) == 0:
        return("tidak ada tabel teridentifikasi")

# ?  queryPart Tabel
    indeksKoma = 1
    statusKondisi = False
    for w in token:
        for t in daftarTabel:
            if w in getDaftarKondisi():
                statusKondisi = True
                break
            if statusKondisi == False:
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
        # ! CEK LAGI UNTUK RELASI NANTI
        for w in getDaftarTable():
            if indeksKoma < len(daftarTabel):
                sqlPart.insert(indeksSQL, f"{w}, ")
                indeksKoma += 1
                break
            elif indeksKoma == len(daftarTabel):
                sqlPart.insert(indeksSQL, f"{w} ")
                indeksKoma += 1
            indeksSQL += 1

# ? queryPart Kondisi
    kolomKondisi, atributKondisi = identifikasiKolomKondisi(token)

    banyakKondisi = identifikasiKondisi(token)
    operatorLogika = identifikasiOperatorLogika(token)

    if banyakKondisi is not None and len(kolomKondisi) > 0 and '#None' not in kolomKondisi and '#None' not in atributKondisi and len(operatorLogika) == len(kolomKondisi)-1:
        sqlPart.insert(indeksSQL, f"WHERE ")
        indeksSQL += 1
        for index, k in enumerate(kolomKondisi):
            sqlPart.insert(
                indeksSQL, f"{k} LIKE '%{atributKondisi[index]}%' ")
            indeksSQL += 1
            if len(operatorLogika) > 0 and index < len(operatorLogika):
                sqlPart.insert(
                    indeksSQL, operatorLogika[index])
                indeksSQL += 1


# ? result query
    result = listToString(sqlPart)

    return(result)
