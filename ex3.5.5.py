# Вводятся (каждое с новой строки): курс доллара (вещественное значение) и число рублей (целое число) для обмена рублей на доллары.
# Вычислить целое количество получаемых долларов (с отбрасыванием дробной части) и сформировать строку, используя F-строку:
# "Вы можете получить <долларов>$ за <число рублей> рублей по курсу <курс доллара>".
# Вывести результат на экран (без кавычек).
dol = float(input())
rub = int(input())
exchange = rub // int(dol)
print(f'Вы можете получить {exchange}$ за {rub} рублей по курсу {dol}')