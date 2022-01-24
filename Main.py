from Controller.Processing import identifikasiKolomByTabel, identifikasiTabel, isPerintah
from Controller.Preprocessing import pre
from Controller.QueryForming import queryForming

kalimatPerintah = pre(
    "tampilkan nama mahasiswa yang memiliki nama adi kurniawan")
print(f'''
    'kalimat': {kalimatPerintah},
    'isPerintah': {isPerintah(kalimatPerintah)},
    'identifikasiTabel': {identifikasiTabel(kalimatPerintah)},
    'identifikasiKolomByTabel': {identifikasiKolomByTabel(kalimatPerintah)},
    'query': {queryForming(kalimatPerintah)}
'''
      )
