import timeit


# 1) Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності,
# закон якої задається за допомогою функції користувача.
# Крім цього параметром генераторної функції повинні бути значення першого члена прогресії
# та кількість членів, що видаються послідовностю. Генератор повинен зупинити свою роботу
# або по досягненню n-го члена, або при передачі команди на завершення.
def user_function(first_value, len_list):
    return first_value * len_list * 10


PROGRESSION_LIMIT = 1000


def outer_func(first_value, user_func):
    _list = [first_value]

    def inner_func():
        answer = ""
        res = user_func(_list[0], len(_list))
        while res < PROGRESSION_LIMIT and not answer:
            answer = yield res
            _list.append(res)
            res = user_func(_list[0], len(_list))
        return res

    return inner_func


first_value_of_progression = 1
x = outer_func(first_value_of_progression, user_function)
for i in x():
    if input("Press ENTER to continue or 'N' to stop"):
        x().close()
        break
    print(i)


# 2) Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація
# #  - https://en.wikipedia.org/wiki/Memoization .
# #  Використовуйте отриманий механізм для прискорення функції рекурсивного
# #  обчислення n - го члена ряду Фібоначчі. Порівняйте швидкість виконання із просто рекурсивним підходом.

FIBONACCI_LIMIT = 25


s1 = """def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(25)
"""
print(timeit.timeit(s1, number=100))
# print(f"2.1){fibonacci(FIBONACCI_LIMIT)}")

s2 = """def f_fibonacci():
    buff = [0, 1]

    def get_next(n):
        if n <= len(buff):
            return buff[n]
        for i in range(len(buff), n + 1):
            res = buff[-1] + buff[-2]
            buff.append(res)
        return res

    return get_next


fib = f_fibonacci()
fib(25)
"""
print(timeit.timeit(s2, number=100))
# print(f"2.2){fib(FIBONACCI_LIMIT)}")


# 3) Напишіть функцію, яка застосує до списку чисел довільну функцію користувача
#  і поверне суми елементів отриманого списку.


def my_function(num_list, func):
    return sum((func(j) for j in num_list))


def user_function_2(n):
    return n + 1000


print(f"3){my_function(range(10), user_function_2)}")
