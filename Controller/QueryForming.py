from Controller.Processing import Processing
from Controller.WordList import WordList


class QueryForming:
    def __init__(self):
        wordList = WordList()
        self.__isKalimatPerintah = False
        self.__daftarTabelTeridentifikasi = []
        self.__daftarKolomTeridentifikasi = []
        self.__kolomKondisiTeridentifikasi = []
        self.__atributKondisiTeridentifikasi = []
        self.__OperatorLogikaTeridentifikasi = []
        self.__daftarKondisi = wordList.getDaftarKondisi()

        self.__sqlPartPerintah = []
        self.__sqlPartKolom = []
        self.__sqlPartTabel = []
        self.__sqlPartKondisi = []

    def queryForming(self, token):
        processing = Processing()
        self.__isKalimatPerintah = processing.isPerintah(token)
        self.__daftarTabelTeridentifikasi = processing.identifikasiTabel(token)
        self.__daftarKolomTeridentifikasi = processing.identifikasiKolomByTabel(
            token)
        self.__kolomKondisiTeridentifikasi, self.__atributKondisiTeridentifikasi = processing.identifikasiKolomKondisi(
            token)
        self.__OperatorLogikaTeridentifikasi = processing.identifikasiOperatorLogika(
            token)

    # ? queryPart SELECT
        if self.__isKalimatPerintah:
            self.__sqlPartPerintah.insert(0, "SELECT ")
        else:
            return("tidak ada kalimat perintah terindentifikasi")

        if len(self.__daftarTabelTeridentifikasi) == 0:
            return("tidak ada tabel teridentifikasi")

    # ?  queryPart Tabel
        indeks = 0
        indeksKoma = 1
        statusKondisi = False

        wordList2 = WordList()
        for t in token:
            for tb in self.__daftarTabelTeridentifikasi:
                if t in self.__daftarKondisi:
                    statusKondisi = True
                    break
                if statusKondisi == False:
                    if t in wordList2.getDaftarKolomByTabel(tb) and indeksKoma < len(self.__daftarKolomTeridentifikasi):
                        self.__sqlPartKolom.insert(indeks, f"{tb}.{t}, ")
                        indeksKoma += 1
                        indeks += 1
                    elif t in wordList2.getDaftarKolomByTabel(tb) and indeksKoma == len(self.__daftarKolomTeridentifikasi):
                        self.__sqlPartKolom.insert(indeks, f"{tb}.{t} ")
                        indeks += 1

    # ? queryPart Kolom
        indeks = 0
        if self.__daftarKolomTeridentifikasi[0] == '*':
            self.__sqlPartKolom.insert(indeks, f"* ")
            indeks += 1
        if len(self.__daftarTabelTeridentifikasi) > 0:
            self.__sqlPartKolom.insert(indeks, f"FROM ")
            indeks += 1

        indeksKoma = 1
        if len(self.__daftarTabelTeridentifikasi) == 1:
            self.__sqlPartTabel.insert(
                indeks, f"{self.__daftarTabelTeridentifikasi[0]} ")
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

        operatorLogika = []
        for x in range(len(self.__kolomKondisiTeridentifikasi)-1):
            operatorLogika.append(self.__OperatorLogikaTeridentifikasi.pop(0))

        indeks = 0
        if processing.identifikasiKondisi(token) is not None and len(self.__kolomKondisiTeridentifikasi) > 0 and len(operatorLogika) == len(self.__kolomKondisiTeridentifikasi)-1:
            self.__sqlPartKondisi.insert(indeks, f"WHERE ")
            indeks += 1

        for index, k in enumerate(self.__kolomKondisiTeridentifikasi):
            self.__sqlPartKondisi.insert(
                indeks, f"{k} LIKE '%{self.__atributKondisiTeridentifikasi[index]}%' ")
            indeks += 1
            if len(operatorLogika) > 0 and index < len(operatorLogika):
                self.__sqlPartKondisi.insert(
                    indeks, operatorLogika[index] + ' ')
                indeks += 1

    # ? result query
        result = listToString(self.__sqlPartPerintah) + \
            listToString(self.__sqlPartKolom) + \
            listToString(self.__sqlPartTabel) + \
            listToString(self.__sqlPartKondisi)

        return(result)


def listToString(list):
    result = ""
    for item in list:
        result += item
    return result
