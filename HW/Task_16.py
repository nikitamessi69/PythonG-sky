#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
#5
#    1 2 3 4 5
#    3
#    -> 1

n = int(input("Введите количество элементов в массиве: "))
a = []
for i in range(n):
    a.append(int(input()))
x = int(input("Введите искомое число: "))
count = 0
for num in a:
    if num == x:
        count += 1
print(f"Число {x} встречается в массиве {count} раз(а)")