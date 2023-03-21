

# modules
# paket yönetimi
# self => this



from human import Human


human1 = Human("MONICA")
human1.name = "Enes"
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Malik")

human2.talk("Selam")
human2.walk()
print(human2)

Human("Melike").talk("Merhaba")


def sayHello():
    return "Hej Monica"

print(sayHello())

