# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#     3. Валюту пользователя определите сами.

import time

def convert(byn):

    rez = float(byn) * 2.58

    print('Ты ввел', byn, 'BYN')

    print('конвертируемая сумма в USD =', rez)

while True:

    inputValue = input('Введите число BYN обмена валюты в USDT. BYN : ')

    if inputValue.isdigit():

        convert(inputValue)

        time.sleep(2)

        break

    else:

        print('Введен неверный формат, введите число BYN для конвертации')