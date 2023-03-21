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

