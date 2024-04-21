# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib_numbers = [1, 1]
    for i in range(m - 2):
        fib_numbers.append(fib_numbers[i] + fib_numbers[i + 1])

    print(fib_numbers)
    return fib_numbers[n - 1:m + 1]

# print(fibonacci(4, 10))



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    for i in range(len(origin_list) - 1):
        for j in range(i + 1, len(origin_list)):
            if origin_list[i] > origin_list[j]:
                origin_list[i], origin_list[j] = origin_list[j], origin_list[i]

    return origin_list

# print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, collection):
    result_list = []
    for el in collection:
        if func(el):
            result_list.append(el)
    return iter(result_list)


# data = list(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
# print(data)



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# skip