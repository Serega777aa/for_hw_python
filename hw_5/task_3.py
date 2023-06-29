# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def gen_fib(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(gen_fib(15)))
