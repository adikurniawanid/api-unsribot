from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Controller.WordList import getDaftarStopWord, getDaftarKolom, getDaftarTable, getDaftarSimbol, getDaftarPenangananNamaTabel, getDaftarPenangananNamaKolom, getDaftarSinonim


def penangananNamaKolom(text):
    daftarPenangananNamaKolom = getDaftarPenangananNamaKolom()
    for i, j in daftarPenangananNamaKolom.items():
        text = text.replace(i, j)
    return text


def penangananNamaTabel(text):
    daftarPenangananNamaTabel = getDaftarPenangananNamaTabel()
    for i, j in daftarPenangananNamaTabel.items():
        text = text.replace(i, j)
    return text


def sinonim(text):
    daftarSinonim = getDaftarSinonim()
    for i, j in daftarSinonim.items():
        text = text.replace(i, j)
    return text


def simbolToKarakter(simbol):
    return simbol.replace("&", "dan").replace("/", "atau")


def doubleToSingleTick(kata):
    return kata.replace("\"", "'")


def tokenizing(kalimat):
    kalimat = doubleToSingleTick(simbolToKarakter(kalimat))
    return kalimat.split()


def hapusSimbol(token):
    specialCharacter = getDaftarSimbol()
    return [w for w in token if w not in specialCharacter]


def stopwordFiltering(token):
    return [w for w in token if w not in getDaftarStopWord()]


def stemming(token):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    tokenStem = []
    for w in token:
        if(w.find("'") != False):
            if(w not in getDaftarKolom() and w not in getDaftarTable()):
                if(stemmer.stem(w) != ""):
                    tokenStem.append(stemmer.stem(w))
            else:
                tokenStem.append(w)
        else:
            tokenStem.append(w)
    return tokenStem


def pre(kalimatPerintah):
    result = stopwordFiltering(
        stemming(
            hapusSimbol(
                tokenizing(
                    doubleToSingleTick(
                        simbolToKarakter(
                            penangananNamaTabel(
                                penangananNamaKolom(
                                    sinonim(
                                        kalimatPerintah.lower())))))))))

    return result
