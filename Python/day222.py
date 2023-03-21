faiz = 1.59
vade = 36
krediadi = "ihtiyac kredisi"

print(int(vade) + 12)
# print(int(krediadi))

faiz = str(faiz)
print(type(faiz))

#vade = int(input("lutfen istediginiz vade sayisini giriniz : "))
print(type(vade));
#print(vade + 12)
vade = vade + 12

# string interpolation

#print("sectiginiz vade sonucu ortaya cikan vade : " + str(vade))

#print("sectiginiz vade sonucu ortaya cikan vade : {vadeSayisi}".format(vadeSayisi=vade) )


isim="Deniz"
metin= "Merhaba {name}".format(name=isim)
print(metin)


metin= "Merhaba {name}".format(name="MONICA")
print(metin)

metin= "Merhaba {name}".format(name=123.2)
print(metin)

print()

# f-string

metin = f"Hosgeldiniz {isim}"
print(metin)

metin = f"Hosgeldiniz {1 + 1}"
print(metin)


def sayHello():
    return "Hej Monica"

print(sayHello())