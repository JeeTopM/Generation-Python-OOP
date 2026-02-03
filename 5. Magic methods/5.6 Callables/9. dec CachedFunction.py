"""
Реализуйте декоратор @CachedFunction, который кэширует вычисленные значения декорируемой функции.
    Кэш должен быть доступен по атрибуту cache и представлять собой словарь,
        ключом в котором является кортеж с аргументами,
            а значением — возвращаемое значение декорируемой функции при вызове с этими аргументами.

Примечание 1. Для однозначного кеширования гарантируется, что декорируемая функция принимает только позиционные аргументы.

Примечание 2. При сдаче решения декоратор @CachedFunction вызывать не нужно.
"""
class CachedFunction:
    pass

if __name__ == '__main__':
    # test 1
    @CachedFunction
    def slow_fibonacci(n):
        if n == 1:
            return 0
        elif n in (2, 3):
            return 1
        return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
    print(slow_fibonacci(100)) # 218922995834555169026

    # test 2
    @CachedFunction
    def slow_fibonacci(n):
        if n == 1:
            return 0
        elif n in (2, 3):
            return 1
        return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
    slow_fibonacci(5)
    for args, value in sorted(slow_fibonacci.cache.items()):
        print(args, value)
    '''
    (2,) 1
    (3,) 1
    (4,) 2
    (5,) 3
    '''
