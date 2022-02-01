from Controller.WordList import WordList, getDaftarKolomByTabel


class Processing:
    def __init__(self):
        wordlist = WordList()
        self.__daftarPerintah = wordlist.getDaftarPerintah()
        self.__daftarTabel = wordlist.getDaftarTable()
        self.__daftarKondisi = wordlist.getDaftarKondisi()
        self.__daftarTabelTeridentifikasi = []

    def isPerintah(self, token):
        for t in token:
            if t in self.__daftarPerintah:
                return t
            else:
                return False

    def identifikasiTabel(self, token):
        result = []
        for t in token:
            if t in self.__daftarTabel:
                result.append(t)
        return result

    def identifikasiKolomByTabel(self, token):
        result = []
        statusKondisi = False
        for t in token:
            if t in self.__daftarKondisi:
                statusKondisi = True
            if statusKondisi != True:
                for tabel in self.__daftarTabel:
                    if t in getDaftarKolomByTabel(tabel):
                        result.append(t)
        if not result:
            result.append("*")
        return result

    def identifikasiKondisi(self, token):
        for t in token:
            if t in self.__daftarKondisi:
                return t

    def identifikasiKolomKondisi(self, token):
        self.__daftarTabelTeridentifikasi = self.identifikasiTabel(token)
        kolomKondisi = []
        atributKondisi = []
        statusKolomKondisi = False

        for index, t in enumerate(token):
            if t in self.__daftarKondisi:
                statusKolomKondisi = True
            if statusKolomKondisi == True:
                for tabel in self.__daftarTabelTeridentifikasi:
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

    def identifikasiOperatorLogika(self, token):
        result = []
        operatorStatus = False

        for w in token:
            if w in self.__daftarKondisi:
                operatorStatus = True
            if operatorStatus == True:
                if w == "atau":
                    result.append("or")
                elif w == "dan":
                    result.append("and")
        return result
