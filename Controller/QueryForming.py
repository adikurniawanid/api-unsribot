from Controller.Processing import Processing
from Controller.WordList import WordList, getDaftarKolomByTabel


def listToString(list):
    result = ""
    for item in list:
        result += item
    return result


class QueryForming:
    def __init__(self, token):
        self.__wordList = WordList()
        self.__processing = Processing()
        self.__token = token
        self.__sqlPartPerintah = []
        self.__sqlPartKolom = []
        self.__sqlPartTabel = []
        self.__sqlPartKondisi = []
        self.__daftarKondisi = self.__wordList.getDaftarKondisi()
        self.__isKalimatPerintah = self.__processing.isPerintah(token)
        self.__daftarTabelTeridentifikasi = self.__processing.identifikasiTabel(
            token)
        self.__daftarKolom = self.__processing.identifikasiKolomByTabel(token)
        self.__kolomKondisiTeridentifikasi, self.__atributKondisiTeridentifikasi = self.__processing.identifikasiKolomKondisi(
            self.__token)

    def queryForming(self):
        # ? queryPart SELECT
        if self.__isKalimatPerintah:
            self.__sqlPartPerintah.append("SELECT ")
        else:
            return("tidak ada kalimat perintah terindentifikasi")

        if len(self.__daftarTabelTeridentifikasi) == 0:
            return("tidak ada tabel teridentifikasi")

    # ?  queryPart Tabel
        indeks = 0
        indeksKoma = 1
        statusKondisi = False
        for w in self.__token:
            for t in self.__daftarTabelTeridentifikasi:
                if w in self.__daftarKondisi:
                    statusKondisi = True
                    break
                if statusKondisi == False:
                    if w in getDaftarKolomByTabel(t) and indeksKoma < len(self.__daftarKolom):
                        self.__sqlPartKolom.insert(indeks, f"{t}.{w}, ")
                        indeksKoma += 1
                        indeks += 1
                    elif w in getDaftarKolomByTabel(t) and indeksKoma == len(self.__daftarKolom):
                        self.__sqlPartKolom.insert(indeks, f"{t}.{w} ")
                        indeks += 1

    # ? queryPart Kolom
        indeks = 0
        if self.__daftarKolom[0] == '*':
            self.__sqlPartKolom.insert(indeks, f"* ")
            indeks += 1
        if len(self.__daftarTabelTeridentifikasi) > 0:
            self.__sqlPartTabel.insert(indeks, f"FROM ")
            indeks += 1

        indeksKoma = 1
        if len(self.__daftarTabelTeridentifikasi) == 1:
            self.__sqlPartTabel.insert(
                indeks, f"{self.__daftarTabelTeridentifikasi[0]} ")
            indeks += 1

    # ? queryPart Kondisi

        tempOperatorLogika = self.__processing.identifikasiOperatorLogika(
            self.__token)

        operatorLogika = []
        for x in range(len(self.__kolomKondisiTeridentifikasi)-1):
            operatorLogika.append(tempOperatorLogika.pop(0))

        indeks = 0
        if self.__processing.identifikasiKondisi(self.__token) is not None and len(self.__kolomKondisiTeridentifikasi) > 0 and len(operatorLogika) == len(self.__kolomKondisiTeridentifikasi)-1:
            self.__sqlPartKondisi.insert(indeks, f"WHERE ")
            indeks += 1

        for index, k in enumerate(self.__kolomKondisiTeridentifikasi):
            self.__sqlPartKondisi.insert(
                indeks, f"{k} LIKE '%{self.__kolomKondisiTeridentifikasi[index]}%' ")
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
