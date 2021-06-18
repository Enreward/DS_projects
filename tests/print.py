import time
from pathlib import Path
# 1
def rec_revers_string(text):
    if len(text) == 1:
        return text[0]
    revers_text = text[-1] + rec_revers_string(text[:-1])
    return revers_text
# 2
def rec_sum_digit(num):
    length = int(len(str(num)))
    if length == 1:
        return num
    sum = (num // 10 ** (length-1)) + rec_sum_digit(num % 10 ** (length-1))
    return sum
# 3
def infinity_digits(digit=1, step=1):
    while True:
        yield digit
        digit += step
        time.sleep(0.5)
# 4
def loop_generator(data):
    i = 0
    while True:
        if i == len(data):
            i = 0
        yield data[i]
        i += 1
        time.sleep(0.5)
# 5
def cache(func):
   cache_dict = {}
   def wrapper(num):
       print(num)
       nonlocal cache_dict
       if num not in cache_dict:
           cache_dict[num] = func(num)
           print(f"Добавление результата в кэш: {cache_dict[num]}")
       else:
           print(f"Возвращение результата из кэша: {cache_dict[num]}")
       print(f"Кэш {cache_dict}")
       return cache_dict[num]
   return wrapper

@cache
def f(n):
   return n * 123456789
# 6
def count_unique_words(text):
    text = set(text)
    print(text)
    return len(text)
# 7
def not_null(list_digit):
    return  not any(list_digit)
# 8
def multiplication_table():
    table = [[print(f"{i} * {j} = {i*j}") for j in range(1, 11)] for i in range(1, 11)]
    return table
# 9
def parity():
    L = [int(input()) % 2 == 0 for i in range(5)]
    result = any(L) and not all(L)
    return result
# 10
def encod(string):
    string += ' '
    length = len(string)
    result = string[0]
    count_of_char = 1
    char_index = 1
    while char_index <= length-1:
        while string[char_index - 1] == string[char_index]:
            count_of_char += 1
            char_index += 1
        result += str(count_of_char)
        result += string[char_index]
        count_of_char = 1
        char_index += 1
    return result
# 11
def new_encod(string):
    current_char = string[0]
    count_of_char = 1
    result = ""
    for char in string:
        if current_char == char:
            count_of_char += 1
        else:
            result += current_char + str(count_of_char)
            current_char = char
            count_of_char = 1
    result += current_char + str(count_of_char)
    return result
def D(a, b, c):
    return b ** 2 - 4 * a * c

def square_solve(a, b, c):
    import math
    d = D(a, b, c)
    if d > 0:
        x1 = (-b + math.sqrt(d))/2 * a
        x2 = (-b - math.sqrt(d))/2 * a
        return x1, x2
    elif d == 0:
        return -b / (2 * a)
    else:
        return "Нет вещественных корней"


# 1
# print(rec_revers_string('12345'))
# 2
# print(rec_sum_digit(1234758632))
# 3
# for i in infinity_digits():
#     print(i)
# 4
# for i in loop_generator([1,2,3]):
#     print(i)
# 5
# print(f(2))
# 6
# text = """The Zen of Python
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!"""
# print(count_unique_words(text))
# 7
# print(not_null(list(map(int, input().split()))))
# 8
# multiplication_table()
# 9
# print(parity())
# 10
# print(encod(input()))
# 11
# print(new_encod(input()))

# 12
# def mass_index(data):
#     output = {}
#     for i in data:
#         output[i] = i[0] / (i[1]**2)
#     return output
# # (вес, рост)
# data = [
#    (82, 191),
#    (68, 174),
#    (90, 189),
#    (73, 179),
#    (76, 184)
# ]
# list_of_indexes = mass_index(data)
# print(sorted(list_of_indexes.items(), key=lambda x: x[1]))
# sorted_list = sorted(data, key=lambda x: x[0] / (x[1]**2))
# print(sorted_list)
# print(sorted_list[0])
# 13
import numpy as np


def game_core(number):
    '''
    Алгоритм основан на идее бинарного поиска.
    Т.к. алгоритм работает с упорядоченной последовательностью чисел от 1 до 100
    нам не нужно предварительно выполнять сортировку.
    Алгоритм бинарного поиска был взят за основы по причине медленного
    уменьшения скорости поиска при увеличении числа входных данных.
    Так, при 1000 и 1000000 входных данных алгоритм отрабатывает в среднем за 6 попыток.
    Так же, при увеличении диапазона поиска загаданного числа,
    в худшем случае количество попыток увеличивается всего на 3-4 единицы.

    Устанавливаем левую границу head равной 1,
    правую границу tail равной 101 (на единицу больше чем максимально возможное искомое число)
    Устанавливаем проверяемое число как середнее значений head и tail.
    Если проверяемое число больше искомого - устанавливаем tail как искомое,
    если меньше - устанавливаем head как искомое,
    иначе завершаем цикл - искомое число найдено.

    Функция принимает загаданное число и возвращает число попыток
    '''
    
    count = 0
    head = 1
    tail = 101
    for count in range(1, tail // 2 + 1):
        count += 1
        predict = (head + tail) // 2
        if predict > number:
            tail = predict
        elif predict < number:
            head = predict
        else:
            break  # выход из цикла, если угадали
    return count


def score_game(game_core):
    '''
        Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    '''
    
    count_ls = []
    #     np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=100000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    return score


score = score_game(game_core)
print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
