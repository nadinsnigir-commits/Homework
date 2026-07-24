# Тема 3
# Урок №9. Множества

# Задача 9.2
n = int(input())
list1 = [int(input()) for _ in range(n)]
m = int(input())
list2 = [int(input()) for _ in range(m)]

list1.sort()
list2.sort()
i = j = 0
count = 0

while i < n and j < m:
    if list1[i] == list2[j]:
        count += 1
        i += 1
        j += 1
    elif list1[i] < list2[j]:
        i += 1
    else:
        j += 1
print(count)

# Задача 9.3

s = input().split()
seen = set()

for num in s:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)