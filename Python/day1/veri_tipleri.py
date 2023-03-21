# Pythonda veri tipler

# text icin = str

# tamsayilar icin = int , ondalikli sayilar icin = float

# diziler icin = list , tuple, range

# true ya da false icin = bool

# ******************************************

name = "Deniz"  # veri tipi = str   , print(type(name))

sayi = 10       # veri tipi = int

pris =20.5      # veri tipi = float

takimlar = ["GS", "BJK","FB", 10, True]    # veri tipi = list

meyveler = ("elma", "kiraz", "mandalina")  # veri tipi = tuple

arabalar = {"ford", "fiat", "ferrari"}     # veri tipi = set

dogru= True           # veri tipi = bool

randomm= range(7)     # veri tipi = range

dene = b"selam"       # veri tipi = bytes

print(type(dene))


# *******************************************

baslik= "Kurs Programi"

tarih= "  1. Gün - 8 Mart 2023"

durum="uygun"

kategori= ["Tumu","Programlama"]

programlama=["Yazılım Geliştirici Yetiştirme Kampı (JavaScript)",""
            "(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium","vb.."]


# *******************************************


email = "abccom"
sifre = "123"
usermail = input("Email adresini Yaziniz = ")
usersifre = input("Sifrenizi yaziniz = ")

#if email == usermail and sifre == usersifre:
if "abc@com" == usermail and "123" == usersifre:
    print("Giriş baraşılı!")
else:
    print("Giriş başarısız!")
