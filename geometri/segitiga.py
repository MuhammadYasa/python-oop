class Segitiga():
    def __init__(self, alas, tinggi):
        # fungsi yang di panggil pertama kali saat object di buat
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'ini adalah object dari segitiga dengan alas = {self.alas} dan tinggi = {self.tinggi}'

    def hitung_luas(self):
        return self.alas * self.tinggi / 2