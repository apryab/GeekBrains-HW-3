def my_func(var1, var2, var3):
    sum_of_3 = var1 + var2 + var3
    min_numb = min(var1, var2, var3)
    sum_of_3 = sum_of_3 - min_numb
    return sum_of_3


while True:
    try:
        my_numb1 = float(input('Введите ваше первое число '))
        my_numb2 = float(input('Введите ваше второе число '))
        my_numb3 = float(input('Введите ваше третье число '))
        break
    except (TypeError, ValueError):
        print('Вы ввели не число')
print('Сумма наибольших чиcел равна {0:.3f}'.format(my_func(my_numb1, my_numb2, my_numb3)))
