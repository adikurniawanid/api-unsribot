from ast import For, operator
from Controller.Processing import identifikasiKolomByTabel, isPerintah, identifikasiTabel, identifikasiKondisi, identifikasiKolomKondisi, identifikasiOperatorLogika
from Controller.WordList import getDaftarKolomByTabel, getDaftarKondisi


def listToString(list):
    result = ""
    for item in list:
        result += item
    return result


def queryForming(token):
    _sqlPerintah = []
    _sqlKolom = []
    _sqlTabel = []
    _sqlKondisi = []

    isKalimatPerintah = isPerintah(token)
    daftarTabel = identifikasiTabel(token)
    daftarKolom = identifikasiKolomByTabel(token)

# ? queryPart SELECT
    if isKalimatPerintah:
        _sqlPerintah.insert(0, "SELECT ")
    else:
        return("tidak ada kalimat perintah terindentifikasi")

    if len(daftarTabel) == 0:
        return("tidak ada tabel teridentifikasi")

# ?  queryPart Tabel
    indeks = 0
    indeksKoma = 1
    statusKondisi = False
    for w in token:
        for t in daftarTabel:
            if w in getDaftarKondisi():
                statusKondisi = True
                break
            if statusKondisi == False:
                if w in getDaftarKolomByTabel(t) and indeksKoma < len(daftarKolom):
                    _sqlKolom.insert(indeks, f"{t}.{w}, ")
                    indeksKoma += 1
                    indeks += 1
                elif w in getDaftarKolomByTabel(t) and indeksKoma == len(daftarKolom):
                    _sqlKolom.insert(indeks, f"{t}.{w} ")
                    indeks += 1

# ? queryPart Kolom
    indeks = 0
    if daftarKolom[0] == '*':
        _sqlKolom.insert(indeks, f"* ")
        indeks += 1
    if len(daftarTabel) > 0:
        _sqlTabel.insert(indeks, f"FROM ")
        indeks += 1

    indeksKoma = 1
    if len(daftarTabel) == 1:
        _sqlTabel.insert(indeks, f"{daftarTabel[0]} ")
        indeks += 1
    # else:
    #     # ! CEK LAGI UNTUK RELASI NANTI
    #     for w in getDaftarTable():
    #         if indeksKoma < len(daftarTabel):
    #             sqlPart.insert(indeksSQL, f"{w}, ")
    #             indeksKoma += 1
    #             break
    #         elif indeksKoma == len(daftarTabel):
    #             sqlPart.insert(indeksSQL, f"{w} ")
    #             indeksKoma += 1
    #         indeksSQL += 1

# ? queryPart Kondisi
    kolomKondisi, atributKondisi = identifikasiKolomKondisi(token)
    tempOperatorLogika = identifikasiOperatorLogika(token)

    operatorLogika = []
    for x in range(len(kolomKondisi)-1):
        operatorLogika.append(tempOperatorLogika.pop(0))

    indeks = 0
    if identifikasiKondisi(token) is not None and len(kolomKondisi) > 0 and len(operatorLogika) == len(kolomKondisi)-1:
        _sqlKondisi.insert(indeks, f"WHERE ")
        indeks += 1

    for index, k in enumerate(kolomKondisi):
        _sqlKondisi.insert(
            indeks, f"{k} LIKE '%{atributKondisi[index]}%' ")
        indeks += 1
        if len(operatorLogika) > 0 and index < len(operatorLogika):
            _sqlKondisi.insert(
                indeks, operatorLogika[index] + ' ')
            indeks += 1


# ? result query
    result = listToString(_sqlPerintah) + \
        listToString(_sqlKolom) + \
        listToString(_sqlTabel) + \
        listToString(_sqlKondisi)

    return(result)
