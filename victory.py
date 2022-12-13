AUTHORS = {
    'Пушкина': 1799,
    'Толстого': 1828,
    'Лермонтова': 1814,
    'Гоголя': 1807,
    'Достоевского': 1821,
}

again = True

while again:
    answers = []
    for name, year in AUTHORS.items():
        answers += [int(input(f'Введите год рождения {name}: '))]

    score = sum( answers[i] == list(AUTHORS.values())[i] for i in range(len(AUTHORS)) )

    print(f'Количество правильных: {score}')
    print(f'Количество ошибок: {len(AUTHORS) - score}')
    print(f'Процент правильных: {score * 100 / len(AUTHORS)}%')
    print(f'Процент НЕправильных: {100 - (score * 100 / len(AUTHORS))}%')

    again = input('Хотите сыграть еще раз?\n').lower() == 'да'
