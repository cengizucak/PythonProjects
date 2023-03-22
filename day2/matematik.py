class Matematik:
    def __init__(self, sayi1, sayi2):  # constructor -yapici block
        self.s1 = sayi1
        self.s2 = sayi2
        print("Referansi olustu. Matematik basladi")

    def topla(self):
        return self.s1 + self.s2

    def cikar(self):
        return self.s1 - self.s2

    def bol(self):
        return self.s1 / self.s2

    def carp(self):
        return self.s1 * self.s2


hesapla = Matematik(4, 8)
sonuc1 = hesapla.topla()
sonuc2 = hesapla.carp()
print("Sonuc : " + str(sonuc1))
print("Sonuc : " + str(sonuc2))


class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)

    def varyansHesapla(self):
        return self.s1 * self.s2


istatistik = Istatistik(5, 7)
