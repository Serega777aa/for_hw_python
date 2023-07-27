# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

balance = 0.0
COMMISSION = 0.015
CASH_BACK = 0.03
TAX = 0.1
count = 0
history = []


def get_choice():
    while True:
        choice = input('Выберите действие \n' \
                       '1 - поплнить \n' \
                       '2 - снять \n' \
                       '3 - история баланса\n' \
                       '4 - выход \n')
        if choice >= '1' and choice <= '4':
            return choice
        else:
            print('некорректный ввод, повторите попытку')


def input_amount():
    while True:
        amount = float(input('Введите сумму кратную 50: '))
        if (amount <= 0 or amount % 50 != 0):
            print('Некорректный ввод')
        else:
            return amount


def show_balance(balance):
    print(f'На счете = {balance:.2f}')


def up_balance(balance, count):
    balance -= get_tax(balance, TAX)
    show_balance(balance)
    amount = input_amount()
    count += 1
    balance += amount
    balance = get_cashback(count, CASH_BACK, balance) + balance
    show_balance(balance)
    return balance, count


def down_balance(balance, count):
    balance -= get_tax(balance, TAX)
    show_balance(balance)
    amount = input_amount()
    amount = get_commission(amount, COMMISSION) + amount
    if balance < amount:
        print('Недостаточно средств', amount)
    else:
        count += 1
        balance -= amount
        balance += get_cashback(count, CASH_BACK, balance)
        show_balance(balance)
    return balance, count


def get_commission(amount, commission):
    if amount * commission < 30:
        return 30
    elif amount * commission > 600:
        return 600
    return commission * amount


def get_tax(balance, tax):
    if balance > 5000000:
        return balance * tax
    return 0


def get_cashback(count, cashback, balance):
    if count % 3 == 0:
        return balance * cashback
    return 0


def get_history(balance, lst):
    lst.append(balance)
    return lst


def bankomat(balance, count, history):
    while True:
        choice = get_choice()
        match choice:
            case '1':
                balance, count = up_balance(balance, count)
                history = get_history(balance, history)
            case '2':
                balance, count = down_balance(balance, count)
                history = get_history(balance, history)
            case '3':
                print(history)
            case '4':
                print('Всего доброго!')
                quit()


bankomat(balance, count, history)


