sec = int(input('Введите количество секунд: '))
h = sec // 3600
minutes = sec - h * 3600
m = minutes // 60
s = minutes - m * 60
if h < 10:
    h = '0' + str(h)
if m < 10:
    m = '0' + str(m)
if s < 10:
    s = '0' + str(s)
print('{}:{}:{}'.format(h, m, s))