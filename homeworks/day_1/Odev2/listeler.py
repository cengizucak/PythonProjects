krediler=["ihtiyac kredisi","Tasit kredisi","Konut kredisi"]

print(type(krediler))
print(krediler[2])

print(len(krediler))

dizi=["Ihtiyac Kredisi", 1, 2,True]
print(dizi)

krediler.append("Özel Kredi")
print(krediler)

krediler.append("x Kredisi")
print(krediler)

print()
#krediler.pop(1)
print(krediler)

krediler.append("Tasit kredisi")
krediler.remove("Tasit kredisi")
print(krediler)

krediler.extend(["Y kredisi", "Z kredisi"])
print(krediler)


