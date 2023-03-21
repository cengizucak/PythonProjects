""" for i in range(10):
    print("xx")
    print(i)
print('**********')
for i in range(5,15):
    print(i)
print('*********')

for i in range(0,50+1,10):
    print(i)
     """

krediler = ["ihtiyac kredisi", "Tasit kredisi", "Konut kredisi"]

for kredi in krediler:
    print(kredi)

for i in range(len(krediler)):
    print(krediler[i])

print("\n")

i = 0
while i < 10:
    print("X")
    i+=1
print("y")

print("\n")


i=0
while i< len(krediler):
    if krediler[i]=="Konut kredisi":
        break
    print(krediler[i])
    i+=1
