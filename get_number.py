'''
добавить счетчик попыток, возможность задать границы диапазона
GUI??
'''

import random
a=random.randrange(1,100)
print('Добро пожаловать в числовую угадайку!')

def is_valid(str):
    if str.isdigit():
        return True if 0<int(str)<100 else False
    else:return False

while True:
    s=input('Введите число: ')
    if not is_valid(s):
        print('введите правильно:')
    else:
        if int(s)<a:
            print('пока меньше')
            continue
        elif int(s)>a:
            print('пока больше')
            continue
        else:
            print('You Win!!!')
            break
