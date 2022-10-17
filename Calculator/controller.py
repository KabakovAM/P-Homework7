import model_sub
import model_div
import model_mult
import model_sum
import user_interface
import logg


def button_click():
    typ = user_interface.get_type()
    if typ == 0:
        return
    op = user_interface.get_operation(typ)
    if op == 0:
        return button_click()
    num_1 = user_interface.get_number_num_1(typ, op)
    num_2 = user_interface.get_number_num_2(typ, op)
    if op == 1:
        result = model_sum.init(num_1, num_2)
    if op == 2:
        result = model_sub.init(num_1, num_2)
    if op == 3 or op == 5:
        result = model_mult.init(num_1, num_2, op, typ)
    if op == 4 or op == 6:
        result = model_div.init(num_1, num_2, op, typ)
    logg.opertion_logger(op, num_1, num_2, result)
    user_interface.view_result(op, num_1, num_2, result)
    user_interface.end_programm()
