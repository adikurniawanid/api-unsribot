from Model.Schema import getDaftarTabel, getDaftarKolom, getDaftarRelasi, querySQL
from Config.Settings import WORDLIST_PERINTAH, WORDLIST_STOPWORD, WORDLIST_KONDISI, WORDLIST_SIMBOL, WORDLIST_SINONIM, WORDLIST_PENANGANAN_NAMA_TABEL, WORDLIST_PENANGANAN_NAMA_KOLOM, WORDLIST_OPERATOR_LOGIKA, DATABASE_NAME
from numpy import hstack


class WordList:
    def __init__(self):
        self.__daftarTabel = getDaftarTabel()
        self.__daftarKolom = getDaftarKolom()
        self.__daftarRelasi = getDaftarRelasi()
        self.__daftarPerintah = readTxtToSet(WORDLIST_PERINTAH)
        self.__daftarKondisi = readTxtToSet(WORDLIST_KONDISI)
        self.__daftarStopword = readTxtToSet(WORDLIST_STOPWORD)
        self.__daftarSimbol = readTxtToSet(WORDLIST_SIMBOL)
        self.__daftarOperatorLogika = readTxtToSet(WORDLIST_OPERATOR_LOGIKA)
        self.__daftarPenangananNamaTabel = readTxtToDict(
            WORDLIST_PENANGANAN_NAMA_TABEL)
        self.__daftarPenangananNamaKolom = readTxtToDict(
            WORDLIST_PENANGANAN_NAMA_KOLOM)
        self.__daftarSinonim = readTxtToDict(WORDLIST_SINONIM)

    def getDaftarTable(self):
        return self.__daftarTabel

    def getDaftarKolom(self):
        return self.__daftarKolom

    def getDaftarRelasi(self):
        return self.__daftarRelasi

    def getDaftarPerintah(self):
        return self.__daftarPerintah

    def getDaftarKondisi(self):
        return self.__daftarKondisi

    def getDaftarStopWord(self):
        return self.__daftarStopword

    def getDaftarSimbol(self):
        return self.__daftarSimbol

    def getDaftarOperatorLogika(self):
        return self.__daftarOperatorLogika

    def getDaftarPenangananNamaTabel(self):
        return self.__daftarPenangananNamaTabel

    def getDaftarPenangananNamaKolom(self):
        return self.__daftarPenangananNamaKolom

    def getDaftarSinonim(self):
        return self.__daftarSinonim


def readTxtToSet(txt):
    return set(line.strip() for line in open(txt))


def readTxtToDict(txt):
    return dict((line.strip().split(':')[0], line.strip().split(':')[1]) for line in open(txt))


def getDaftarKolomByTabel(tabel):
    return hstack(querySQL(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{tabel}' AND table_schema='{DATABASE_NAME}'"))
