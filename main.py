from geometri.bangunruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('menerapkan metode OOP pada python')

p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(14, 4)
print(s1.info())
print(s1.hitung_luas())

print('\nmencoba membuat object dari class bangun ruang')
b1 = BangunRuang()
print(b1.info())

# polymorphism : kemampuan object untuk merespon berbeda, terhadap pemanggilan method yg sama

daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\npolymorphism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())
