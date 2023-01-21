# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран,
# а так же сумму элементов списка.

# n = int(input('Введите количество чисел в последовательности: '))
# lst = []
# i = 1
# while i <= n:
#     lst.append((1+1/i)**i)
#     i+=1
# print(lst)
# sum = 0
# for item in lst:
#     sum += item
# print(f'Сумма элементов списка {sum}')



# Оптимизированный вариант

n = int(input('Введите количество чисел в последовательности: ')) 

lst = [round((1+1/i)**i,3) for i in range(1, n+1)]
print(lst)
print(f"Сумма элементов списка {round(sum(lst),2)}")