def raise_to_power(number, degree):
    answer1 = number ** degree
    answer2 = 1
    for i in range(degree):
        answer2 *= number
    return answer1, answer2


while True:
    try:
        numb = float(input('Введите ваше число возводимое в степень '))
        my_degree = input('Введите вашу степень ')
        if my_degree.isdigit():
            my_degree = int(my_degree)
            break
        else:
            print('Нужно ввести целую положительную степень')
    except (TypeError, ValueError):
        print('Вы ввели не число')
my_answer1, my_answer2 = raise_to_power(numb, my_degree)
print('Ответ через оператор "**" -', my_answer1)
print('Ответ через цикл -', my_answer2)
