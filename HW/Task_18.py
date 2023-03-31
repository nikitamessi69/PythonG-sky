#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
#5
#    1 2 3 4 5
#    6
#    -> 5

n = int(input("Введите количество элементов в массиве: "))
a = []
for i in range(n):
    a.append(int(input()))
x = int(input("Введите число X: "))
min_dist = abs(x - a[0])
min_elem = a[0]
for num in a:
    dist = abs(x - num)
    if dist < min_dist:
        min_dist = dist
        min_elem = num
print(f"Ближайший элемент к числу {x} - это число {min_elem}")