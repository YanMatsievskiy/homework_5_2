'''Задача 2. Маркировка батончиков'''

n = int(input('Введите кол-во батончиков:'))
print('Введите id и массу батончиков:')

result = {}

for _ in range(n):
    id, mass = input().split()
    id = int(id)
    mass = int(mass)

    if 40 <= mass <= 50:
        status = "GOOD"
    else:
        status = "BAD"

    result[id] = status

print('Вывод данных:')
print(result)
