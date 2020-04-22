def division(var1, var2):
    if var2 != 0:
        return var1 / var2
    else:
        return 'Деление на ноль'


while True:
    try:
        my_var1 = float(input('Введите ваше делимое '))
        my_var2 = float(input('Введите ваш делитель '))
        break
    except (TypeError, ValueError):
        print('Вы ввели не числа')
answer = division(my_var1, my_var2)
try:
    answer = float(answer)
    print('Мы получили: {0:.3f}'.format(answer))
except (TypeError, ValueError):
    print('Мы получили: {0}'.format(answer))
