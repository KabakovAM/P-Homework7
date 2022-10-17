import exception


def complex_number_num_1():
    num_1 = input('Введите вещественную часть: ')
    if not exception.number(num_1):      
        print('\nОшибка ввода!')
        return complex_number_num_1()
    return exception.number(num_1)

def complex_number_num_2():
    num_2 = input('Введите мнимую часть: ')
    if not exception.number(num_2):
        print('\nОшибка ввода!')
        return complex_number_num_2()
    return exception.number(num_2)
