import random 

# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
# Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
def zadcha1():
    num = [random.randint(1,10) for i in range (random.randint(1,10))]
    print(num)
    x = filter(lambda x:x > 5, num)
    x = list (x)
    print(f'список чисел больше 5: {x}')


# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

def zadacha2():
    nums = [1, 5, 2, 3, 4, 6, 1, 7]
    index = random.randint(1,6)
    new_spisok = [nums[index]]
    for i in nums:
        if i > max(new_spisok):
            new_spisok.append(i)
    print(index)
    print(new_spisok)



# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадаютСписок уникальных элементов
# [1, 4, 2, 3, 6, 7]

def zadacha3():
    num1 = list(random.randint(1,10) for i in range (10))
    print(num1)
    new_num = len(num1)
    num2=list(set(num1))
    print(num2)
    print('совпадающие элементов было в списке:', new_num - len(num2))
