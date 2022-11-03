print('\n---------------------------')
print('numeral system - система счисления ')
print('\n---------------------------')
print('binary numeral system - двоичная система счисления ')
print()
b = 0b00011010 #10 system
o = 0o32       #8  system
h = 0x1A       #16 system
print('b#2=', bin(b), 'b#10=', int('11010', base=2))
print('o#2=', oct(o), 'o#10=', int('32', base=8))
print('h#2=', hex(h), 'h#10=', int('1A', base=16))

print('b#10=', int(b))
print('o#10=', int(o))
print('h#10=', int(h))
print()
print('', end='\n\n')

print('---- СХЕМА ГОРНЕРА ----', end='\n')

print('перевод десятичного числа в число заданной системы счисления.')
# перевод на бумаге десятичного 23 в двоичное
# делим в столбик 23 на 2:
# 23|2
# 2 |=11
# 03
#  2
# =1                      (0, нулевой разряд)
#     11|2
#     10|=5
#     =1                  (1, первый разряд)
#         5|2
#         4|=2 
#        =1               (2)
#            2|2
#            2|=1         (4, старший разряд)
#           =0            (3)
# результат: 10111
number = int(input('введите десятичное число:'))
base = int(input('введите основание системы счисления до 10:'))
res = ''
while number>0:
    digit = number % base  # выделяем последнюю цифру числа
    res = str(digit) + res # добавляем цифру вперед результирующего числаб т.к. цифры высчитываются от младшей к старшей
    number //= base        # получаем 
print('res=', res, end='\n\n')

print('перевод числа заданной системы счисления в десятичное (начиная со старших разрядов). ')
# перевод на бумаге двоичного числа 10111
# 1     = 1                             = 1 
# 10    = 1*2+0                         = 1*2+0  = 2
# 101   = (1*2+0)*2 + 1                 = 2*2+1  = 5
# 1011  = ((1*2+0)*2 + 1)*2 + 1         = 5*2+1  = 11
# 10111 = (((1*2+0)*2 + 1)*2 + 1)*2 + 1 = 11*2+1 = 23
# результат: 23
base = int(input('введите основание системы счисления до 10:'))
number_txt = input('введите число заданной системы счисления:')
l = len(number_txt)  # количество цифр в веденном числе

"""
print('перебор числа по цифрам, начиная со старшего разряда:', end='')
x = int(number_txt)
for i in range(l-1,-1,-1):
    digit = x//(10**i) # получаем первую цифру слева, делением на вес разряда в десятичной системе счисл, если система счисление превысит 10, то надо использовать строку или массив символов, т.к. в системе старше десятичной используются уже символы A B C D ...  
    x -= digit * (10**i)
    print(' ', digit, end='')
print('')
"""
# calculate result:
number = int(number_txt)
res = 0
for i in range(l-1,-1,-1):
    # выделяем цифру старшего разряда и сдвигаем число влево
    digit = number//(10**i)   # получаем первую цифру слева, делением на вес разряда в десятичной системе счисл, если система счисление превысит 10, то надо использовать строку или массив символов, т.к. в системе старше десятичной используются уже символы A B C D ...  
    number -= digit * (10**i) # сдвигаем число влево
    # собираем результат
    res = res * base + digit
print('результат расчета, когда перебор цифр идет от старшей к младшей: res=', res)
    
number = int(number_txt)
res = 0
for i in range(l):
    #если система счисление превысит 10, то надо использовать строку или массив символов, т.к. в системе старше десятичной используются уже символы A B C D ...  
    digit = number%base # получаем цифру нулевого разряда
    number //= 10       # number = (number - digit)/10 сдвигаем число вправо на один десятичный разряд
    # собираем результат
    res += digit * (base**i)
    #print('i=', i)
    #print('digit=', digit)
    #print('number=', number)
    #print('res=', res)
print('результат расчета, когда перебор цифр идет от младшей к старшей: res=', res, end='\n\n\n')


