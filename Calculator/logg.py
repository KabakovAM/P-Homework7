import datetime
from encodings import utf_8


def opertion_logger(op, num_1, num_2, result):
    dic = {1: '+', 2: '-', 3: '*', 4: '/', 5: '^', 6: '\u221a'}
    time = datetime.datetime.now().strftime('%d.%m.%y || %H:%M')
    with open('Homework7\Calculator\log.txt', 'a', encoding='utf_8') as file:
        if op == 6:
            file.write(f'{time}; {dic[op]}{num_1} = {result}\n')
        else:
            file.write(f'{time}; {num_1} {dic[op]} {num_2} = {result}\n')
