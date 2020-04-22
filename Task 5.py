def sum_of_numbs_in_string(string, curr_sum):
    numb_list = string.split()
    init_sum = curr_sum
    for element in numb_list:
        try:
            temp = float(element)
            curr_sum += temp
        except (TypeError, ValueError):
            print('Строка должна состоять из чисел введённых через пробел')
            return init_sum
    return curr_sum


current_sum = 0
while True:
    print('Введите ваши числа через пробел')
    my_string = input('Помните, что * последним символом - выход из программы\n')
    if my_string[len(my_string)-1] == '*':
        my_string = my_string[0:len(my_string)-1]
        current_sum = sum_of_numbs_in_string(my_string, current_sum)
        print('Итоговая сумма - {0:.3f}'.format(current_sum))
        break
    current_sum = sum_of_numbs_in_string(my_string,current_sum)
    print('Текущая сумма - {0:.3f}\n'.format(current_sum))
