def info(name, surname, birth_year, city, email, phone):
    print('Имя - {}, Фамилия - {}, Год рождения - {}'.format(name, surname, birth_year), end = ', ')
    print('Город - {}, Эл. адрес - {}, Телефон - {}'.format(city, email, phone))


user_name = input('Введите ваше имя ')
user_surname = input('Введите вашу фамилию ')
user_birth_year = input('Введите ваш год рождения ')
user_city = input('Введите ваш город ')
user_email = input('Введите ваш эл. адрес ')
user_phone = input('Введите ваш телефон ')
info(name=user_name, surname=user_surname, birth_year=user_birth_year,
     city=user_city, email=user_email,  phone=user_phone)
