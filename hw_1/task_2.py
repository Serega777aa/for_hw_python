a = int(input('Введите сторону треугольника '))
b = int(input('Введите сторону треугольника '))
c = int(input('Введите сторону треугольника '))

if (a + b < c or a + c < b or b + c < a) or (a < 1 or b < 1 or c < 1):
    print('треугольника с такими сторонами не существует')
elif a == b == c:
    print('треугольник равносторонний')
elif a == b or a == c  or b == c:
    print('треугольник равнобедренный')
else:
    print('треугольник разносторонний')
