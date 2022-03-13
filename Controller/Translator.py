from Controller.Parser import Parser
from Controller.WordList import WordList, getDaftarKolomByTabel


class Translator:
    def __init__(self, token):
        self.__token = token
        self.__wordList = WordList()
        self.__parser = Parser(self.__token)

        self.__daftarKondisi = self.__wordList.getDaftarKondisi()

        self.__kalimatPerintah = self.__parser.getPerintahTeridentifikasi()
        self.__daftarTabelTeridentifikasi = self.__parser.getTabelTeridentifikasi()
        self.__daftarKolom = self.__parser.getKolomTeridentifikasiByTabel()
        self.__kondisiTeridentifikasi = self.__parser.getKondisiTeridentifikasi()
        self.__kolomKondisiTeridentifikasi = self.__parser.getKolomKondisiTeridentifikasi()
        self.__atributKondisiTeridentifikasi = self.__parser.getAtributKondisiTeridentifikasi()
        self.__OperatorLogikaTeridentifikasi = self.__parser.getOperatorLogikaTeridentifikasi()

        self.__sqlPartPerintah = []
        self.__sqlPartKolom = []
        self.__sqlPartTabel = []
        self.__sqlPartKondisi = []
        self.__sqlPartOperatorLogika = []

    def queryPartPerintah(self):
        self.__sqlPartPerintah.append("SELECT ")

    def queryPartKolom(self):
        indeksKoma = 1
        for w in self.__token:
            if w in self.__daftarKondisi:
                break
            for t in self.__daftarTabelTeridentifikasi:
                if w in getDaftarKolomByTabel(t) and indeksKoma < len(self.__daftarKolom):
                    self.__sqlPartKolom.append(f"{t}.{w}, ")
                    indeksKoma += 1
                elif w in getDaftarKolomByTabel(t) and indeksKoma == len(self.__daftarKolom):
                    self.__sqlPartKolom.append(f"{t}.{w} ")

        if self.__daftarKolom[0] == '*':
            self.__sqlPartKolom.append(f"* ")

    def queryPartTabel(self):
        if len(self.__daftarTabelTeridentifikasi) > 0:
            self.__sqlPartTabel.append(f"FROM ")

        if len(self.__daftarTabelTeridentifikasi) == 1:
            self.__sqlPartTabel.append(
                f"{self.__daftarTabelTeridentifikasi[0]} ")

    def queryPartOperator(self):
        for x in range(len(self.__kolomKondisiTeridentifikasi)-1):
            self.__sqlPartOperatorLogika.append(
                self.__OperatorLogikaTeridentifikasi.pop(0))

    def queryPartKondisi(self):
        if self.__kondisiTeridentifikasi is not None and len(self.__kolomKondisiTeridentifikasi) > 0 and len(self.__sqlPartOperatorLogika) == len(self.__kolomKondisiTeridentifikasi)-1:
            self.__sqlPartKondisi.append(f"WHERE ")

        if len(self.__daftarTabelTeridentifikasi) == 1:
            for index, k in enumerate(self.__kolomKondisiTeridentifikasi):
                self.__sqlPartKondisi.append(
                    f"{self.__daftarTabelTeridentifikasi[0]}.{k} LIKE '%{self.__atributKondisiTeridentifikasi[index]}%' ")
                if len(self.__sqlPartOperatorLogika) > 0 and index < len(self.__sqlPartOperatorLogika):
                    self.__sqlPartKondisi.append(
                        self.__sqlPartOperatorLogika[index] + ' ')

    def run(self):
        if self.__kalimatPerintah:
            self.queryPartPerintah()
        else:
            return("tidak ada kalimat perintah terindentifikasi")

        if len(self.__daftarTabelTeridentifikasi) == 0:
            return("tidak ada tabel teridentifikasi")

        self.queryPartKolom()
        self.queryPartTabel()
        self.queryPartOperator()
        self.queryPartKondisi()

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
