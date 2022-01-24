from Model.Schema import getDaftarTabel, getDaftarKolom, getDaftarRelasi, querySQL
from numpy import hstack

from Config.Settings import DATABASE_NAME, WORDLIST_PERINTAH, WORDLIST_STOPWORD, WORDLIST_KONDISI, WORDLIST_SIMBOL, WORDLIST_SINONIM, WORDLIST_PENANGANAN_NAMA_TABEL, WORDLIST_PENANGANAN_NAMA_KOLOM


class wordList:
    def readTxtToSet(txt):
        return set(line.strip() for line in open(txt))

    def readTxtToDict(txt):
        return dict((line.strip().split(':')[0], line.strip().split(':')[1]) for line in open(txt))

    _daftarTabel = getDaftarTabel()
    _daftarKolom = getDaftarKolom()
    _daftarRelasi = getDaftarRelasi()

    _daftarPerintah = readTxtToSet(WORDLIST_PERINTAH)
    _daftarKondisi = readTxtToSet(WORDLIST_KONDISI)
    _daftarStopword = readTxtToSet(WORDLIST_STOPWORD)
    _daftarSimbol = readTxtToSet(WORDLIST_SIMBOL)
    _daftarPenangananNamaTabel = readTxtToDict(WORDLIST_PENANGANAN_NAMA_TABEL)
    _daftarPenangananNamaKolom = readTxtToDict(WORDLIST_PENANGANAN_NAMA_KOLOM)
    _daftarSinonim = readTxtToDict(WORDLIST_SINONIM)


def getDaftarPerintah():
    return wordList._daftarPerintah


def getDaftarTable():
    return wordList._daftarTabel


def getDaftarKolom():
    return wordList._daftarKolom


def getDaftarKondisi():
    return wordList._daftarKondisi


def getDaftarStopWord():
    return wordList._daftarStopword


def getDaftarSimbol():
    return wordList._daftarSimbol


def getDaftarRelasi():
    return wordList._daftarRelasi


def getDaftarPenangananNamaTabel():
    return wordList._daftarPenangananNamaTabel


def getDaftarPenangananNamaKolom():
    return wordList._daftarPenangananNamaKolom


def getDaftarSinonim():
    return wordList._daftarSinonim


def getDaftarKolomByTabel(tabel):
    return hstack(querySQL(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{tabel}' AND table_schema='{DATABASE_NAME}'"))
