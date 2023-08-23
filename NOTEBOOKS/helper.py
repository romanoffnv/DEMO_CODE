flag = True
def main_func(callback_function):
    trigger = callback_function()
    print(trigger)

def callback_func():
    return 'button 1'
def callback_func_1():
    return 'button 2'

if flag:
    main_func = main_func(callback_func) 
else:
    main_func = main_func(callback_func_1) 
