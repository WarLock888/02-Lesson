# МОДУЛЬ 3

ASPushkin = 1799

year = int(input('В каком году родился Пушкин? '))

if year == ASPushkin:
    date = int(input('Дата рождения Пушкина? '))
    if date == 6:
        print('Верно')
    else:
        print('Неверный день рождения')

else:
    print('Неверный год')
