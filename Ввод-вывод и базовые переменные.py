# Тема 2
# Урок 3

# Задача 3.1

Pet = str(input("Введите вид питомца: "))
Age = int(input("Возраст питомца: "))
Name = str(input("Кличка питомца: "))
print("Это" , Pet, "по кличке", Name ,"." , "Возраст: ",Age)


# Задача 3.2

print(' Australopithecus ', ' Homo habilis ', ' Homo erectus ', ' Homo heidelbergensis ', ' Homo neanderthalensis ', ' Homo sapiens ', ' Homo sapiens sapiens ' sep="=>")
# или
print(' Australopithecus ', end="=>")
print(' Homo habilis ', end="=>")
print(' Homo erectus ',  end="=>")
print(' Homo heidelbergensis ', end="=>")
print(' Homo neanderthalensis ', end="=>")
print(' Homo sapiens ', end="=>")
print(' Homo sapiens sapiens ', end=".")
