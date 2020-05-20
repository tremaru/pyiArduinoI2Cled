#!/usr/bin/python3
# ПРИМЕР ВЫВОДА ДАННЫХ С РАЗНЫМИ ПАРАМЕТРАМИ:

from time import sleep
# Подключаем библиотеку для работы с индикатором I2C-flash.
from pyiArduinoI2Cled import *

# Объявляем объект библиотеки pyiArduinoI2Cled, указывая адрес модуля на шине I2C.
disp = pyiArduinoI2Cled(0x09)

# Если объявить объект без указания адреса, то адрес будет найден автоматически.
#disp = pyiArduinoI2Cled()

# Объявляем список из 4 целых положительных чисел.
a = [0,3,6,9]

# Объявляем переменную с указанием интервала
delay = .5

# NB! Комментарии справа, выражения через запятую и пробелы
# при вызове функций исключительно для показательных целей
# в производственном коде такие вещи не приветствуются

try:

    while True:

        disp.print(    1                  ),    sleep(delay)  # Вывод целого   числа    1.
        disp.print(   -1                  ),    sleep(delay)  # Вывод целого   числа   -1.
        disp.print(  0.1                  ),    sleep(delay)  # Вывод дробного числа  0.1.
        disp.print( -0.1                  ),    sleep(delay)  # Вывод дробного числа -0.1.

        disp.print(    1   , TEMP         ),    sleep(delay)  # Вывод целого   числа    1 в качестве температуры.
        disp.print(   -1   , TEMP         ),    sleep(delay)  # Вывод целого   числа   -1 в качестве температуры.
        disp.print(  0.1   , TEMP         ),    sleep(delay)  # Вывод дробного числа  0.1 в качестве температуры.
        disp.print( -0.1   , TEMP         ),    sleep(delay)  # Вывод дробного числа -0.1 в качестве температуры.

        disp.print(    a                  ),    sleep(delay)  # Вывод массива «а» состоящего из 4 положительный целых чисел.

        disp.print(    1, 2, TIME         ),    sleep(delay)  # Вывод двух чисел 1,2   в качестве времени (01 минута : 02 секунды).
        disp.print(   34,56, TIME         ),    sleep(delay)  # Вывод двух чисел 34,56 в качестве времени (34 минуты : 56 секунд ).

        disp.print(  250   , HEX          ),    sleep(delay)  # Вывод целого числа 250 в шестнадцатиричной системе счисления (FA).
        disp.print(   31   , HEX          ),    sleep(delay)  # Вывод целого числа  31 в шестнадцатиричной системе счисления (1F).

        disp.print("test"                 ),    sleep(delay)  # Вывод текста.

        disp.point(    0, 1               ),    sleep(delay)  # Установка двоеточия.
        disp.point(    0, 0               ),    sleep(delay)  # Сброс     двоеточия.
        disp.point(    5, 1               ),    sleep(delay)  # Установка всех точек и двоеточия.
        disp.point(    5, 0               ),    sleep(delay)  # Сброс     всех точек и двоеточия.

        disp.light(    4                  ),    sleep(delay)  # Установка яркости 4.
        disp.light(    1                  ),    sleep(delay)  # Установка яркости 1.
        disp.light(    0                  ),    sleep(delay)  # Установка яркости 0.
        disp.light(    6                  ),                  # Установка яркости 6.

        disp.turn (    1                  ),    sleep(delay)  # Переворот изображения на 180°.
        disp.turn (    0                  ),    sleep(delay)  # Возврат изображения к углу 0°.

        disp.print(    1                  ),    sleep(delay)  # Вывод целого числа    1.
        disp.print(   12                  ),    sleep(delay)  # Вывод целого числа   12.
        disp.print(  123                  ),    sleep(delay)  # Вывод целого числа  123.
        disp.print( 1234                  ),    sleep(delay)  # Вывод целого числа 1234.
        disp.print(  234   , RIGHT        ),    sleep(delay)  # Вывод целого числа 234    со сдвигом вправо от старшего разряда.
        disp.print(   34   , RIGHT        ),    sleep(delay)  # Вывод целого числа 34     со сдвигом вправо от старшего разряда.
        disp.print(    4   , RIGHT        ),    sleep(delay)  # Вывод целого числа 4      со сдвигом вправо от старшего разряда.

        disp.print(   45   , POS1, RIGHT  ),    sleep(delay)  # Вывод целого числа 45     со сдвигом вправо от 1 позиции.
        disp.print(   45   , POS2, RIGHT  ),    sleep(delay)  # Вывод целого числа  45    со сдвигом вправо от 2 позиции.
        disp.print(   45   , POS3, RIGHT  ),    sleep(delay)  # Вывод целого числа   45   со сдвигом вправо от 3 позиции.
        disp.print(   45   , POS4, RIGHT  ),    sleep(delay)  # Вывод целого числа    45  со сдвигом вправо от 4 позиции.
        disp.print(   45   , POS4         ),    sleep(delay)  # Вывод целого числа    45  со сдвигом влево  от 4 позиции.
        disp.print(   45   , POS3         ),    sleep(delay)  # Вывод целого числа   45   со сдвигом влево  от 3 позиции.
        disp.print(   45   , POS2         ),    sleep(delay)  # Вывод целого числа  45    со сдвигом влево  от 2 позиции.
        disp.print(   45   , POS1         ),    sleep(delay)  # Вывод целого числа 45     со сдвигом влево  от 1 позиции.

        disp.print(    6, 1               ),    sleep(delay)  # Вывод целого числа 6 с 1 знаком  после запятой.
        disp.print(    6, 2               ),    sleep(delay)  # Вывод целого числа 6 с 2 знаками после запятой.
        disp.print(    6, 3               ),    sleep(delay)  # Вывод целого числа 6 с 3 знаками после запятой.
        disp.print(    6, 2, RIGHT        ),    sleep(delay)  # Вывод целого числа 6 с 2 знаками после запятой и сдвигом вправо от старшего разряда.
        disp.print(    6, 1, RIGHT        ),    sleep(delay)  # Вывод целого числа 6 с 1 знаком  после запятой и сдвигом вправо от старшего разряда.
        disp.print(    6,    RIGHT        ),    sleep(delay)  # Вывод целого числа 6                           и сдвигом вправо от старшего разряда.

        disp.print(7.89 , 0, RIGHT        ),    sleep(delay)  # Вывод дробного числа 7.89 без знаков  после запятой и сдвигом вправо от старшего разряда.
        disp.print(7.89 , 1, RIGHT        ),    sleep(delay)  # Вывод дробного числа 7.89 с 1 знаком  после запятой и сдвигом вправо от старшего разряда.
        disp.print(7.89 , 2, RIGHT        ),    sleep(delay)  # Вывод дробного числа 7.89 с 2 знаками после запятой и сдвигом вправо от старшего разряда.
        disp.print(7.89 , 3, RIGHT        ),    sleep(delay)  # Вывод дробного числа 7.89 с 3 знаками после запятой и сдвигом вправо от старшего разряда.
        disp.print(7.89 , 2               ),    sleep(delay)  # Вывод дробного числа 7.89 с 2 знаками после запятой.
        disp.print(7.89 , 1               ),    sleep(delay)  # Вывод дробного числа 7.89 с 1 знаком  после запятой.
        disp.print(7.89 , 0               ),    sleep(delay)  # Вывод дробного числа 7.89 без знаков  после запятой.

        disp.print(    8   , LEN1         ),    sleep(delay)  # Вывод целого числа 8 в 1 разряде.
        disp.print(    8   , LEN2         ),    sleep(delay)  # Вывод целого числа 8 в 2 разрядах (впереди добавляется 1 нуль).
        disp.print(    8   , LEN3         ),    sleep(delay)  # Вывод целого числа 8 в 3 разрядах (впереди добавляется 2 нуля).
        disp.print(    8   , LEN4         ),    sleep(delay)  # Вывод целого числа 8 в 4 разрядах (впереди добавляется 3 нуля).
        disp.print(    8   , LEN4, '_'    ),    sleep(delay)  # Вывод целого числа 8 в 4 разрядах (впереди добавляется 3 знака '_').
        disp.print(    8   , LEN3, '_'    ),    sleep(delay)  # Вывод целого числа 8 в 3 разрядах (впереди добавляется 2 знака '_').
        disp.print(    8   , LEN2, '_'    ),    sleep(delay)  # Вывод целого числа 8 в 2 разрядах (впереди добавляется 1 знак  '_').
        disp.print(    8   , LEN1, '_'    ),    sleep(delay)  # Вывод целого числа 8 в 1 разряде.

        disp.print( 6789   , LEN1         ),    sleep(delay)  # Вывод целого числа 6789 в 1 разряде  (срезаются 3 первых разряда).
        disp.print( 6789   , LEN2         ),    sleep(delay)  # Вывод целого числа 6789 в 2 разрядах (срезаются 2 первых разряда).
        disp.print( 6789   , LEN3         ),    sleep(delay)  # Вывод целого числа 6789 в 3 разрядах (срезается 1 первый разряд ).
        disp.print( 6789   , LEN4         ),    sleep(delay)  # Вывод целого числа 6789 в 4 разрядах (выводится всё число целиком).
        disp.print( 6789   , LEN3, RIGHT  ),    sleep(delay)  # Вывод целого числа 6789 в 3 разрядах (срезается 1 первый разряд ).
        disp.print( 6789   , LEN2, RIGHT  ),    sleep(delay)  # Вывод целого числа 6789 в 2 разрядах (срезаются 2 первых разряда).
        disp.print( 6789   , LEN1, RIGHT  ),    sleep(delay)  # Вывод целого числа 6789 в 1 разряде  (срезаются 3 первых разряда).

        disp.print("88.:8.8."             ),    sleep(delay)  # Включение всех сегментов кроме точки в 1 позиции.

        disp.blink(    1, 1               ),    sleep(delay)  # Включение  мигания знака в 1 позиции.
        disp.blink(    2, 1               ),    sleep(delay)  # Включение  мигания знака в 2 позиции.
        disp.blink(    3, 1               ),    sleep(delay)  # Включение  мигания знака в 3 позиции.
        disp.blink(    4, 1               ),    sleep(delay)  # Включение  мигания знака в 4 позиции.
        disp.blink(    1, 0               ),    sleep(delay)  # Отключение мигания знака в 1 позиции.
        disp.blink(    2, 0               ),    sleep(delay)  # Отключение мигания знака в 2 позиции.
        disp.blink(    3, 0               ),    sleep(delay)  # Отключение мигания знака в 3 позиции.
        disp.blink(    4, 0               ),    sleep(delay)  # Отключение мигания знака в 4 позиции.
        disp.blink(    0, 1               ),    sleep(delay)  # Включение  мигания двоеточия.
        disp.blink(    0, 0               ),    sleep(delay)  # Отключение мигания двоеточия.
        disp.blink(    5, 1               ),    sleep(delay)  # Включение  мигания всех светящихся сегментов дисплея.
        disp.blink(    5, 0               ),    sleep(delay)  # Отключение мигания всех светящихся сегментов дисплея.

        disp.blink(    5, 1               )                   # Включение  мигания всех светящихся сегментов дисплея.
        disp.frequ(    4                  )                   # Устанавливаем частоту миганий в 4 Гц.
        disp.print( 4444                  ),    sleep(delay)  # Вывод целого  числа 4444.
        disp.frequ(    3                  )                   # Устанавливаем частоту миганий в 3 Гц.
        disp.print( 3333                  ),    sleep(delay)  # Вывод целого  числа 3333.
        disp.frequ(    2                  )                   # Устанавливаем частоту миганий в 2 Гц.
        disp.print( 2222                  ),    sleep(delay)  # Вывод целого  числа 2222.
        disp.frequ(    1                  )                   # Устанавливаем частоту миганий в 1 Гц.
        disp.print( 1111                  ),    sleep(delay)  # Вывод целого  числа 1111.
        disp.blink(    5, 0               )                   # Отключение мигания всех светящихся сегментов дисплея.

except:

    # Очистка экрана.
    disp.clear()
