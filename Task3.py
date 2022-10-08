#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

#list = [i for i in range(1,10)]
#print(list)
#new_list = list[:: - 1] 
#print(new_list)

import random

list = []
for i in range(5):
    list.append(random.randint(1,10))
print(list)
new_list = []
for i in list:
    if list.cunt(i)<2:
        new_list.append(i)
print(new_list)
