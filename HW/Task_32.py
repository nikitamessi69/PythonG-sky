# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def indices_in_range(lst, min_value, max_value):
    indices = []
    for i in range(len(lst)):
        if min_value <= lst[i] <= max_value:
            indices.append(i)
    return indices

lst = [2, 4, 5, 7, 8, 1, 3, 6]
min_value = 3
max_value = 6
result = indices_in_range(lst, min_value, max_value)
print(f"Индексы элементов списка, значения которых находятся в диапазоне [{min_value}, {max_value}]: {result}")