# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов, отличной от 0.

# from random import uniform

# def get_real_nums (n, first, last):
#     return [round(uniform(first,last), 2) for i in range(n)]

# def find_the_diff(mynums):
#     nums = [round(x - int(x), 2) for x in (mynums)]
#     return max(nums) - min(nums)

# n = int(input('Введите количество чисел в списке: '))
# first = 1
# last = 10
# mynums = get_real_nums(n, first, last)

# print (mynums)
# print(f"Разница, согласно задания: {find_the_diff(mynums)}")



# Оптимизированный вариант

from random import uniform

n = int(input('Введите размер списка '))
lst = [round(uniform(0,9),2) for i in range(n)]
new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
print(lst)
print('Разница, согласно задания', max(new_lst) - min(new_lst))