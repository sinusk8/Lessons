first_day = float(input('Введите, сколько километров пробежит спортсмен в первый день: '))
last_day = float(input('Введите желаемый результат, в километрах: '))
day = 1
print('{}-й день: {} км'.format(day, first_day))
while first_day < last_day:
    first_day = first_day + first_day * 0.1
    day += 1
    print('{}-й день: {:.2f} км'.format(day, first_day))
print('Ответ: на {}-й день спортсмен достиг результата — не менее {} км.'.format(day, last_day))
