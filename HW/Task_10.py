#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть.

n = int(input())  # количество монеток
s = input()  # строка с описанием, как лежат монетки вначале
heads = s.count('H')  # количество монеток гербом вначале
tails = n - heads  # количество монеток решкой вначале
flips = 0  # количество переворотов, которые нужно сделать

# случай 1: все монетки лежат гербом вначале
if heads == 0:
    flips = tails
# случай 2: все монетки лежат решкой вначале
elif tails == 0:
    flips = heads
# случай 3: можно перевернуть монетки гербом
elif heads <= tails:
    flips = heads
# случай 4: можно перевернуть монетки решкой
else:
    flips = tails

print(flips)