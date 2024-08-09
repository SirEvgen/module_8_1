def add_everything_up(a, b):
    try:
        a + b
    except TypeError:
        print(f'Так делать вообще нельзя, но что нас остановит?')
        return f'{a} {b}'
    else:
        return round(a + b, 3)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

