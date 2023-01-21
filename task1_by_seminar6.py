# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# number = float(input("Введите вещественное число: "))

# lst = list(str(number).split('.'))
# summ = 0
# for i in lst:
#     for j in i:
#         summ += int(j)
# print(f"Сумма цифр в этом числе равна {summ}")


# Оптимизированный вариант

def sum_digits(num):
    return sum(map(int, num.replace('.','').replace('-','')))

num = input('Введите любое вещественное число: ')
print(f'Сумма цифр в этом числе равна {sum_digits(num)}')