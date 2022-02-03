from Controller.WordList import WordList, getDaftarKolomByTabel


class Parser:
    def __init__(self, token):
        self.__token = token
        __wordlist = WordList()
        self.__daftarPerintah = __wordlist.getDaftarPerintah()
        self.__daftarTabel = __wordlist.getDaftarTable()
        self.__daftarKondisi = __wordlist.getDaftarKondisi()
        self.__perintahTeridentifikasi = False
        self.__daftarTabelTeridentifikasi = []
        self.__daftarKolomTeridentifikasiByTabelTeridentifikasi = []
        self.__kondisiTeridentifikasi = False
        self.__operatorLogikaTeridentifikasi = []
        self.__kolomKondisiTeridentifikasi = []
        self.__atributKondisiTeridentifikasi = []
        self.run()

    def run(self):
        self.identifikasiPerintah()
        self.identifikasiTabel()
        self.identifikasiKolomByTabel()
        self.identifikasiKondisi()
        self.identifikasiOperatorLogika()
        self.identifikasiKolomKondisi()

    def identifikasiPerintah(self):
        for t in self.__token:
            if t in self.__daftarPerintah:
                self.__perintahTeridentifikasi = t

    def identifikasiTabel(self):
        for t in self.__token:
            if t in self.__daftarTabel:
                self.__daftarTabelTeridentifikasi.append(t)

    def identifikasiKolomByTabel(self):
        statusKondisi = False
        for t in self.__token:
            if t in self.__daftarKondisi:
                statusKondisi = True
            if statusKondisi != True:
                for tabel in self.__daftarTabelTeridentifikasi:
                    if t in getDaftarKolomByTabel(tabel):
                        self.__daftarKolomTeridentifikasiByTabelTeridentifikasi.append(
                            t)
        if not self.__daftarKolomTeridentifikasiByTabelTeridentifikasi:
            self.__daftarKolomTeridentifikasiByTabelTeridentifikasi.append("*")

    def identifikasiKondisi(self):
        for t in self.__token:
            if t in self.__daftarKondisi:
                self.__kondisiTeridentifikasi = t

    def identifikasiKolomKondisi(self):
        statusKolomKondisi = False

        for index, t in enumerate(self.__token):
            if t in self.__daftarKondisi:
                statusKolomKondisi = True
            if statusKolomKondisi == True:
                for tabel in self.__daftarTabelTeridentifikasi:
                    if t in getDaftarKolomByTabel(tabel):
                        try:
                            self.__kolomKondisiTeridentifikasi.append(t)
                        except:
                            self.__kolomKondisiTeridentifikasi.append('#None')
                        try:
                            self.__atributKondisiTeridentifikasi.append(
                                self.__token[index+1])
                        except:
                            self.__kolomKondisiTeridentifikasi.pop()

    def identifikasiOperatorLogika(self):
        __operatorStatus = False

        for w in self.__token:
            if w in self.__daftarKondisi:
                __operatorStatus = True
            if __operatorStatus == True:
                if w == "atau" or w == "dan":
                    self.__operatorLogikaTeridentifikasi.append(w)
                # if w == "atau":
                #     self.__operatorLogikaTeridentifikasi.append("or")
                # elif w == "dan":
                #     self.__operatorLogikaTeridentifikasi.append("and")

    def getPerintahTeridentifikasi(self):
        return self.__perintahTeridentifikasi

    def getTabelTeridentifikasi(self):
        return self.__daftarTabelTeridentifikasi

    def getKolomTeridentifikasiByTabel(self):
        return self.__daftarKolomTeridentifikasiByTabelTeridentifikasi

    def getKondisiTeridentifikasi(self):
        return self.__kondisiTeridentifikasi

    def getOperatorLogikaTeridentifikasi(self):
        return self.__operatorLogikaTeridentifikasi

    def getKolomKondisiTeridentifikasi(self):
        return self.__kolomKondisiTeridentifikasi

    def getAtributKondisiTeridentifikasi(self):
        return self.__atributKondisiTeridentifikasi
