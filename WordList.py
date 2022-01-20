from Model import querySQL
from numpy import hstack

from Settings import DATABASE_NAME, WORDLIST_PERINTAH, WORDLIST_STOPWORD, WORDLIST_KONDISI, WORDLIST_SIMBOL


class wordList:
    def readTxt(txt):
        myFile = open(txt, "r")
        content = myFile.read()
        result = content.split(",")
        myFile.close()
        return result

    _daftarTabel = hstack(querySQL(
        f"SELECT TABLE_NAME FROM information_schema.`TABLES` WHERE TABLE_TYPE LIKE 'VIEW' AND TABLE_SCHEMA LIKE '{DATABASE_NAME}'"))
    _daftarKolom = hstack(querySQL(
        f"SELECT col.column_name FROM information_schema.columns col JOIN information_schema.views vie ON vie.table_schema=col.table_schema AND vie.table_name=col.table_name where col.table_schema not in ('sys', 'information_schema','mysql', 'performance_schema') AND vie.table_schema='{DATABASE_NAME}'"))
    _daftarRelasi = querySQL(
        "SELECT `TABLE_NAME`, `COLUMN_NAME`, `REFERENCED_TABLE_SCHEMA`,`REFERENCED_TABLE_NAME`,`REFERENCED_COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`KEY_COLUMN_USAGE` WHERE`TABLE_SCHEMA`=SCHEMA() AND `REFERENCED_TABLE_NAME` IS NOT NULL")

    _daftarPerintah = readTxt(WORDLIST_PERINTAH)
    _daftarKondisi = readTxt(WORDLIST_KONDISI)
    _daftarStopword = readTxt(WORDLIST_STOPWORD)
    _daftarSimbol = readTxt(WORDLIST_SIMBOL)
    _daftarPenangananNamaTabel = {
        "kode mata kuliah": "kode_mata_kuliah",
        "kode matakuliah": "kode_mata_kuliah",
        "mata kuliah": "mata_kuliah",
        "matakuliah": "mata_kuliah"}
    _daftarSinonim = {
        "perempuan":  "wanita",
        "laki laki": "pria",
        "laki-laki": "pria",
        "lelaki": "pria",
    }


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


def getDaftarSinonim():
    return wordList._daftarSinonim


def getDaftarKolomByTabel(tabel):
    return hstack(querySQL(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{tabel}' AND table_schema='{DATABASE_NAME}'"))
