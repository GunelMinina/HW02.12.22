# Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

print('Введите количество элементов: ')
num = int(input())
list = []
for _ in range(num):
    list.append(int(input('Введите элемент: ')))
print(list)

result_list = []
for i in list:
    if list.count(i) == 1:
        result_list.append(i)
print(result_list)
