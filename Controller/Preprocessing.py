from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Controller.WordList import WordList


class Preprocessing:
    def __init__(self):
        wordlist = WordList()
        self.__daftarPenangananNamaKolom = wordlist.getDaftarPenangananNamaKolom()
        self.__daftarSinonim = wordlist.getDaftarSinonim()
        self.__daftarPenangananNamaTabel = wordlist.getDaftarPenangananNamaTabel()
        self.__daftarSimbol = wordlist.getDaftarSimbol()
        self.__daftarKolom = wordlist.getDaftarKolom()
        self.__daftarTable = wordlist.getDaftarTable()
        self.__daftarStopWord = wordlist.getDaftarStopWord()

    def sinonim(self, text):
        for i, j in self.__daftarSinonim.items():
            text = text.replace(i, j)
        return text

    def penangananNamaKolom(self, text):
        for i, j in self.__daftarPenangananNamaKolom.items():
            text = text.replace(i, j)
        return text

    def penangananNamaTabel(self, text):
        for i, j in self.__daftarPenangananNamaTabel.items():
            text = text.replace(i, j)
        return text

    def simbolToKarakter(self, text):
        return text.replace("&", "dan").replace("/", "atau")

    def doubleToSingleTick(self, text):
        return text.replace("\"", "'")

    def tokenizing(self, kalimat):
        kalimat = self.doubleToSingleTick(self.simbolToKarakter(kalimat))
        return kalimat.split()

    def hapusSimbol(self, token):
        return [w for w in token if w not in self.__daftarSimbol]

    def stemming(self, token):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        tokenStem = []
        for t in token:
            if(t.find("'") != False):
                if(t not in self.__daftarKolom and t not in self.__daftarTable):
                    if(stemmer.stem(t) != ""):
                        tokenStem.append(
                            self.penangananNamaKolom(
                                self.penangananNamaTabel(stemmer.stem(t))))
                else:
                    tokenStem.append(
                        self.penangananNamaKolom(
                            self.penangananNamaTabel(t)))
            else:
                tokenStem.append(
                    self.penangananNamaKolom(
                        self.penangananNamaTabel(t)))
        return tokenStem

    def stopwordFiltering(self, token):
        return [w for w in token if w not in self.__daftarStopWord]

    def pre(self, kalimat):
        result = self.stopwordFiltering(
            self.stemming(
                self.hapusSimbol(
                    self.tokenizing(
                        self.doubleToSingleTick(
                            self.simbolToKarakter(
                                self.penangananNamaTabel(
                                    self.penangananNamaKolom(
                                        self.sinonim(
                                            kalimat.lower())))))))))
        return result
