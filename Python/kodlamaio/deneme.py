students = ["Emirhan Küçükmorkoç","Halit Kalaycı","Sefa Dilmeç"]

def add(name):
    students.append(name)
add("Engin Demirog")
print(students)


def deleteByNameAndSurname(name):
    students.remove(name)
deleteByNameAndSurname("Engin Demirog")
print(students)

print("oooooooooooooooo")

def addMore(names = []):
    students.extend(names)
addMore(["Engin Demiroğ", "Murat Peker","EEEE","AAAAA,","XXXX"])
print(students)



def getAll():
    for student in students:
        print(student)
getAll()

def learnNumberOfStudent(name):
    print(f"{name} adlı öğrencinin numarasi :  {students.index(name)} ")

learnNumberOfStudent("Emirhan Küçükmorkoç")



def deleteMoreThan(name):
    students.remove(name)
message = int(input("How many students do u want to delete "))
i =0
while i<message:
    nameAndSurname = input("Please enter the student's name do you want to delete : ")
    deleteMoreThan(nameAndSurname)
    i +=1

print(students)