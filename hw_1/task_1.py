MIN = 2
MAX = 10
COLUMN = 4

print(" " * 18, "ТАБЛИЦА УМНОЖЕНИЯ")
for i in range(MIN, MAX, COLUMN):
    for j in range(MIN, MAX):
        for k in range(i, i + COLUMN):
            print(f'{k} x {j:>2} = {j * k:>2}', end='    ')
        print()
    print()
