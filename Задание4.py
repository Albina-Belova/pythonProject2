"Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму."

n = int(input())
lst = [round((1+1/n)**n, 2) for n in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')
