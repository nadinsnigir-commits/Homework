# Тема 3
# Урок 7. Строки

# Задача 7.2

s = input() 
new_s = ""

for i in range(len(s)):
    if s[i] != " ":
        new_s += s[i]
    elif i == 0 or s[i-1] != " ":
        new_s += " "

print(new_s)