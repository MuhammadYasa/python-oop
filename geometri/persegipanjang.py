class PersegiPanjang():

    def __init__(self, p, l):
        # fungsi yang di panggil pertama kali saat object di buat
        self.p = p
        self.l = l

    def info(self):
        return f'ini adalah object dari persegi panjang dengan panjang = {self.p} dan lebar = {self.l}'

    def hitung_luas(self):
        return self.p * self.l
