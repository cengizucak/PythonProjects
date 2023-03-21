fiyat = 50
indirim = 20

"""

"""

def calculate():
    print(100 - 20)


def calculateWithParams(fiyat, indirim):
    print(fiyat - indirim)


calculate()
calculateWithParams(50, 10)
calculateWithParams(100, 30)

def sayHej(name):
    print(f"Merhaba {name}")

sayHej("Monica")
sayHej("Deniz")
sayHej("Cengiz")

def calculateReturn(price, discount):
    return price-discount

newPrice=calculateReturn(200,40)
print(newPrice)