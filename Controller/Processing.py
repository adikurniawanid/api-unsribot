from Controller.WordList import getDaftarKolomByTabel, getDaftarTable, getDaftarPerintah,  getDaftarKondisi


def isPerintah(token):
    kalimatPerintah = getDaftarPerintah()
    for w in token:
        if w in kalimatPerintah:
            return w
        else:
            return False


def identifikasiTabel(token):
    daftarTabel = getDaftarTable()

    result = []

    for w in token:
        if w in daftarTabel:
            result.append(w)

    return result


def identifikasiKolomByTabel(token):
    daftarTabel = identifikasiTabel(token)
    result = []

    daftarKondisi = getDaftarKondisi()
    statusKondisi = False

    for t in token:
        if t in daftarKondisi:
            statusKondisi = True
        if statusKondisi != True:
            for tabel in daftarTabel:
                if t in getDaftarKolomByTabel(tabel):
                    result.append(t)

    if not result:
        result.append("*")

    return result


def identifikasiKondisi(token):
    daftarKondisi = getDaftarKondisi()

    for w in token:
        if w in daftarKondisi:
            return w


def identifikasiKolomKondisi(token):
    daftarTabel = identifikasiTabel(token)
    kolomKondisi = []
    atributKondisi = []

    daftarKondisi = getDaftarKondisi()
    statusKolomKondisi = False

    for index, t in enumerate(token):
        if t in daftarKondisi:
            statusKolomKondisi = True
        if statusKolomKondisi == True:
            for tabel in daftarTabel:
                if t in getDaftarKolomByTabel(tabel):
                    try:
                        kolomKondisi.append(t)
                    except:
                        kolomKondisi.append('#None')
                    try:
                        atributKondisi.append(token[index+1])
                    except:
                        kolomKondisi.pop()
    return kolomKondisi, atributKondisi


def identifikasiOperatorLogika(token):
    result = []
    daftarKondisi = getDaftarKondisi()
    operatorStatus = False

    for w in token:
        if w in daftarKondisi:
            operatorStatus = True
        if operatorStatus == True:
            if w == "atau":
                result.append("or")
            elif w == "dan":
                result.append("and")
    return result
