t = 1,2,3,4,5
type(t)#<class 'tuple'>
a = t[0]
print(a)#1
a,b,*rest = t
print(rest)#[3, 4, 5]
type(rest)#<class 'list'>
type(t)#class 'tuple'>
print(t)#(1, 2, 3, 4, 5)
print(*t)#1 2 3 4 5
print(*rest)#3 4 5
print(*rest, sep=':', end='!\n') #3:4:5!

def hello_n(name:str,
            n : int):
    for i in range(n):
        print(name)

vas = 'Vasia', 3
hello_n(*vas)
hello_n(3,4) # нет ошибки
#hello_n(3,'4') ошибка
l = [1,'dd',5.0]
print(l)
print(type(l))
t2 = (1,'dd',5.0)
print(t2)
print(type(t2))
