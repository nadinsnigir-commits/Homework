# Тема 2
# Урок 5 "Логические и условные операторы"

# Задача 5.1

Namber = int(input ("Введите число: "))

if Namber % 2 == 0:

    if Namber == 0:
        print("Нулевое число")

    elif Namber / 1 < 0:
        print("Отрицательное четное число")

    else:
        print("Положительное четное число")

else:
    print("Число не является четным")



# Задача 5.2


word = input("Введите слово: ").lower()

vowel_count = 0
consonant_count = 0

for letter in word:
    if letter in 'aeiou':
        vowel_count += 1
    elif not vowel_count:
        print("False")
    elif letter:
        consonant_count += 1

print("Количество гласных:", vowel_count)
print("Количество согласных:", consonant_count)

# Задача 5.3

if (a >= x) and (b < x):
    print("Mike") 
elif (b >= x) and (a < x):
    print("Ivan")
elif ((a + b) >= x):
    # print(2) 
    print(1) 
elif a >= x and b >= x:
    print("2") 
else:
    print("0")
