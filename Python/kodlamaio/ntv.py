
#ogrenciler = ["Ali Akçay", "Osman Karakuş", "Ragıp Şenses"]
ogrenciler = []




kacOgrenci = input("Lütfen kaç öğrenci ekleyeceğinizi giriniz: ") #inputtan gelen veriler string veri tipidir for döngüsünde sayaç olarak kullanabilmemiz için önce integer değere çevirmeliyiz aşağıdaki koşulda olduğu gibi.
for i in range(int(kacOgrenci)):
    multiEkle = input("Lütfen eklemek istediğiniz öğrenci isim soyisimini giriniz: ")
    ogrenciler.append(multiEkle)
    print(ogrenciler)
for cc in ogrenciler:
    print(cc)