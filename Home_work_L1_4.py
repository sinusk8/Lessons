proceeds = int(input('Укажите выручку фирмы: '))
costs = int(input('Укажите издержки фирмы: '))
if proceeds > costs:
    profit = (proceeds - costs) / proceeds
    print('Фирма работает в прибыль. Ура!')
    print('Рентабельность фирмы: {}'.format(profit))
    peoples = int(input('Введите количество сотрудников фирмы: '))
    person = (proceeds - costs) / peoples
    print('Прибыль фирмы на одного сотрудника: {}'.format(person))
else:
    print('Фирма работает в убыток. Нужно больше продавать.')
