number = int(input('Введите любое число: '))
n = 0
if number < 10:
    n = number
while number > 10:
    a = number % 10
    number //= 10
    if a > n:
        n = a
print('Наибольшая цифра в числе {}'.format(n))
