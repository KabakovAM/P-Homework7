import exception
import compl
import controller


def get_type():
    print('\nКалькулятор')
    print('\nВыберите опцию: ')
    print('1 - Рациональное\n2 - Комплексное\n0 - Выйти из программы')
    data = input()
    if exception.type_op(data, 2):
        return int(data)
    print('\nОшибка ввода!')
    return get_type()


def get_operation(typ):
    print('\nВыберете опцию:')
    if typ == 1:
        print('1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n\
5 - Возведение в степень\n6 - Извлечение квадратного корня\n0 - Выйти в предыдущее меню')
        data = input()
        if exception.type_op(data, 6):
            return int(data)
    else:
        print('1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n\
5 - Возведение в степень\n0 - Выйти в главное меню')
        data = input()
        if exception.type_op(data, 5):
            return int(data)
    print('\nОшибка ввода!')
    return get_operation(typ)


def get_number_num_1(typ, op):
    if typ == 1:
        if 0 < op < 5:
            num = input('\nВведите первое число: ')
        if op == 5:
            num = input('\nВведите основание степени: ')
        if op == 6:
            num = input('\nВведите подкоренное выражение: ')
        if not exception.number(num):
            print('\nОшибка ввода!')
            return get_number_num_1(typ, op)
        return exception.number(num)
    if typ == 2:
        if 0 < op < 5:
            print('\nВведите первое число: ')
            return complex(compl.complex_number_num_1(), compl.complex_number_num_2())
        if op == 5:
            print('\nВведите основание степени: ')
            return complex(compl.complex_number_num_1(), compl.complex_number_num_2())


def get_number_num_2(typ, op):
    if op == 6:
        return 1
    if typ == 1:
        if 0 < op < 5:
            num = input('\nВведите второе число: ')
        if op == 5:
            num = input('\nВведите показатель степени: ')
        if not exception.number(num):
            print('\nОшибка ввода!')
            return get_number_num_2(typ, op)
        return exception.number(num)
    if typ == 2:
        if 0 < op < 5:
            print('\nВведите второе число: ')
            return complex(compl.complex_number_num_1(), compl.complex_number_num_2())
        if op == 5:
            print('\nВведите показатель степени: ')
            return complex(compl.complex_number_num_1(), compl.complex_number_num_2())


def view_result(op, num_1, num_2, result):
    dic = {1: '+', 2: '-', 3: '*', 4: '/', 5: '^', 6: '\u221a'}
    if op == 6:
        print(f'\n{dic[op]}{num_1} = {result}')
    else:
        print(f'\n{num_1} {dic[op]} {num_2} = {result}')


def end_programm():
    print('\nВыберите опцию: ')
    print('1 - Продолжить работу с калькулятором\n0 - Выйти из программы')
    data = input()
    if exception.type_op(data, 1):
        if int(data) == 1:
            return controller.button_click()
        if int(data) == 0:
            return
    print('\nОшибка ввода!')
    return end_programm()
