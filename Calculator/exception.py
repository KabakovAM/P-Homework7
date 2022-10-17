
def type_op(num, n):
    if num.isdigit() and 0 <= int(num) <= n:
        return True
    return False


def number(num):
    if num.lstrip('-').replace('.','',1).isdigit():
        if '.' in num:
            return float(num)
        return int(num)
    return False