MIN = 0
MAX = 1000

while True:
    num = int(input('Введите число от 1 до 1000 '))
    if MIN < num <= MAX:
        break
    else:
        print('ввели некорректное число')

count = 0
for i in range(1, num):
    if num % i == 0:
        count += 1
if count > 1:
    print('Число является составным')
else:
    print('Число является простым')
