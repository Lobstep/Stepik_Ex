# В список: a = [5.4, 6.7, 10.4]
# добавить в конец вложенный список со значениями, вводимыми в программу (целые числа вводятся в строчку через пробел).
# Результирующий список lst вывести на экран командой: print(lst)
a = [5.4, 6.7, 10.4]
a.append(list(map(int, input().split())))
lst = a[:]
print(lst)