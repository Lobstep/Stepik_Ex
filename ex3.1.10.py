# Написать программу ввода двух слов (через пробел в одну строчку).
# Определить булевы значения для оператора in проверки вхождения первого слова во второе.
# А также для операторов ==, >, <. Все булевы значения объединить в одну строку через пробел и вывести на экран.
a, b = (input().split())
print(a in b, a == b, a > b, a < b)