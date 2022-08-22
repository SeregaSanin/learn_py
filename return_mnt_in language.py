# объявление функции
def get_month(language, number):
    mnt_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
              'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

    mnt_en = ['january', 'february', 'march', 'april', 'may', 'june',
              'july', 'august', 'september', 'october', 'november', 'december']
    if language=='en':
        return mnt_en[number-1]
    else:
        return mnt_ru[number - 1]

# считываем данные
lan = 'en'
num = 7

# вызываем функцию
print(get_month(lan, num))