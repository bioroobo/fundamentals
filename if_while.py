#целые числа от -4 до 4 кроме нуля
s = 0; i=-5
while i < 4:
    i = i + 1
    if i == 0:
        continue
    else:
        print(i)
        s += 1/i
    if (i==3):
        break;
else:
    print('s=', s)
