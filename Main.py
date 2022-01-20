from Processing import identifikasiKolomByTabel, identifikasiTabel, isPerintah
from Preprocessing import pre
from QueryForming import queryForming
from WordList import getDaftarPerintah, getDaftarStopWord

kalimatPerintah = pre(
    "pak bapak ibu tampilkan nama mahasiswa")
print(f'''
    'kalimat': {kalimatPerintah},
    'isPerintah': {isPerintah(kalimatPerintah)},
    'identifikasiTabel': {identifikasiTabel(kalimatPerintah)},
    'identifikasiKolomByTabel': {identifikasiKolomByTabel(kalimatPerintah)},
    'query': {queryForming(kalimatPerintah)}
'''
      )
