from unittest import result
from WordList import getDaftarKolomByTabel, getDaftarTable, getDaftarPerintah, getDaftarKolom, getDaftarKondisi


def isPerintah(token):
    kalimatPerintah = getDaftarPerintah()
    for w in token:
        if w in kalimatPerintah:
            result = True
            break
        else:
            result = False
    return result


def identifikasiTabel(token):
    daftarTabel = getDaftarTable()

    result = []

    for w in token:
        if w in daftarTabel:
            result.append(w)

    return result


def identifikasiKolom(token):
    daftarKolom = getDaftarKolom()

    result = []

    for w in token:
        if w in daftarKolom:
            result.append(w)

    return result


def identifikasiKolomByTabel(token):

    daftarTabel = identifikasiTabel(token)
    result = []

    for t in token:
        for tabel in daftarTabel:
            if t in getDaftarKolomByTabel(tabel):
                result.append(t)

    if not result:
        result.append("*")

    return result


def identifikasiKondisi(token):
    daftarKondisi = getDaftarKondisi()

    teridentifikasi = []
    indeksTeridentifikasi = []
    banyakKondisi = 0

    indeks = 0
    for w in token:
        if w in daftarKondisi:
            teridentifikasi.append(w)
            indeksTeridentifikasi.append(indeks)
            banyakKondisi += 1
            indeks += 1
        else:
            indeks += 1
    return teridentifikasi, indeksTeridentifikasi, banyakKondisi


def identifikasiOperatorLogika(token):
    teridentifikasi = []
    indeksTeridentifikasi = []
    banyakOperatorLogika = 0

    indeks = 0
    for w in token:
        if w == "atau":
            teridentifikasi.append(w)
            # teridentifikasi.append("or")
            indeksTeridentifikasi.append(indeks)
            indeks += 1
            banyakOperatorLogika += 1
        elif w == "dan":
            teridentifikasi.append(w)
            # teridentifikasi.append("and")
            indeksTeridentifikasi.append(indeks)
            indeks += 1
            banyakOperatorLogika += 1
        else:
            indeks += 1
    return teridentifikasi, indeksTeridentifikasi, banyakOperatorLogika
