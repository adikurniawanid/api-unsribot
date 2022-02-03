from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Controller.WordList import WordList


class Preprocessing:
    def __init__(self):
        __wordlist = WordList()
        __factory = StemmerFactory()
        self.__stemmer = __factory.create_stemmer()

        self.__daftarPenangananNamaKolom = __wordlist.getDaftarPenangananNamaKolom()
        self.__daftarSinonim = __wordlist.getDaftarSinonim()
        self.__daftarPenangananNamaTabel = __wordlist.getDaftarPenangananNamaTabel()
        self.__daftarSimbol = __wordlist.getDaftarSimbol()
        self.__daftarKolom = __wordlist.getDaftarKolom()
        self.__daftarTable = __wordlist.getDaftarTable()
        self.__daftarStopWord = __wordlist.getDaftarStopWord()

    def __sinonim(self, text):
        for i, j in self.__daftarSinonim.items():
            text = text.replace(i, j)
        return text

    def __penangananNamaKolom(self, text):
        for i, j in self.__daftarPenangananNamaKolom.items():
            text = text.replace(i, j)
        return text

    def __penangananNamaTabel(self, text):
        for i, j in self.__daftarPenangananNamaTabel.items():
            text = text.replace(i, j)
        return text

    def __simbolToKarakter(self, text):
        return text.replace("&", "dan").replace("/", "atau")

    def __doubleToSingleTick(self, text):
        return text.replace("\"", "'")

    def __tokenizing(self, kalimat):
        return self.__doubleToSingleTick(self.__simbolToKarakter(kalimat)).split()

    def __hapusSimbol(self, token):
        return [w for w in token if w not in self.__daftarSimbol]

    def __stemming(self, token):

        tokenStem = []
        for t in token:
            if(t.find("'") != False):
                if(t not in self.__daftarKolom and t not in self.__daftarTable):
                    if(self.__stemmer.stem(t) != ""):
                        tokenStem.append(
                            self.__penangananNamaKolom(
                                self.__penangananNamaTabel(self.__stemmer.stem(t))))
                else:
                    tokenStem.append(
                        self.__penangananNamaKolom(
                            self.__penangananNamaTabel(t)))
            else:
                tokenStem.append(
                    self.__penangananNamaKolom(
                        self.__penangananNamaTabel(t)))
        return tokenStem

    def __stopwordFiltering(self, token):
        return [w for w in token if w not in self.__daftarStopWord]

    def run(self, kalimat):
        result = self.__stopwordFiltering(
            self.__stemming(
                self.__hapusSimbol(
                    self.__tokenizing(
                        self.__doubleToSingleTick(
                            self.__simbolToKarakter(
                                self.__penangananNamaTabel(
                                    self.__penangananNamaKolom(
                                        self.__sinonim(
                                            kalimat.lower())))))))))
        return result
