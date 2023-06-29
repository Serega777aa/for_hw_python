MIN = 0
MAX = 1000

while True:
    num = int(input('Введите число от 1 до 1000 '))
    if MIN < num <= MAX:
        break
    print('ввели некорректное число')

if num == 1:
    print('Число является простым')
for i in range(2, int(num ** 0.5) +1):
    if num % i == 0:
        print('Число является составным')
        break
    else:
        print('Число является простым')
        break
