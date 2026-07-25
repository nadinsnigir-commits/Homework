# Тема 3
# Урок 11. Функции

# Задача 11.1

def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

n = int(input("Введите натуральное число: "))
fact_n = factorial(n)
result_list = []

for i in range(fact_n, 0, -1):
    result_list.append(factorial(i))

print(result_list)