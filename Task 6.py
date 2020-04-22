def int_func(string):
    string = string.title()
    return string


latin_check = 0
while latin_check == 0:
    latin_check = 1
    my_string = input('Введите вашу строку: ')
    for elem in my_string:
        if not ((96 < ord(elem) < 123) or (ord(elem) == 32)):
            print('Строка должна состоять из латинских букв ', end='')
            print('в нижнем регистре и пробелов!')
            latin_check = 0
            break
string_list = my_string.split()
answer_list = []
for elem in string_list:
    answer_list.append(int_func(elem))
answer_string = ' '.join(answer_list)
print('Функция отработала:', answer_string)
