class Human:
    # name = "Halit"

    # "Built-in"
    # "initialize"

    def __init__(self, name):
        self.name = name
        print("Bir human instance uretildi")

    def __str__(self) -> str:
        return f"STR fonksiyonundan dönen deger : {self.name}"

    def talk(self, sentence):
        print(f"{self.name} : {sentence} ")

    def walk(self):
        print(f"{self.name} is walking..")


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