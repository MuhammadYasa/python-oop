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
