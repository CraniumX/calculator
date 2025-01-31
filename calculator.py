def calculator(numb_one, numb_two):
    try:
        operation = int(input(f"Какую операцию будем выполнять ? Выберите номер нужной операции (1-Сложение, 2-Вычитание, 3-Умножение, 4-Деление): "))
        if operation == 1:
            res = numb_one + numb_two
            return res
        if operation == 2:
            res = numb_one - numb_two
            return res
        if operation == 3:
            res = numb_one * numb_two
            return res
        if operation == 4:
            res = numb_one / numb_two
            return res
    except: ValueError
    print("Нужно выбрать один из вариантов. Попробуйте еще раз...")

numb_one = float(input("Введите первое число: "))
numb_two = float(input("Введите второе число: "))

print(calculator(numb_one, numb_two))