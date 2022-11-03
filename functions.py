print('\nfoo1')
def foo1(X,y):
    X[0] =7


A = [1,2,3]
foo1(A,3)
print(A) # result:  [7, 2, 3]


print('\nfoo2')
def foo2(X,y):
    X = [4,5,6]   


A = [1,2,3]
y=foo2(A,3)
print(A) # result:  [1, 2, 3]


print('\nfoo3')
def foo3(x:str, y:int) -> str:
    """ аннотация – это типа комментарий.
        аннотация не обязывает, можно  задать или вернуть и другое значение, но так делать не надо."""
    result = x
    for i in range(y-1):
        result += x
    return result


z=foo3(2, 5)
print(z) # result: 10
z=foo3('MA', 2)
print(z) # result: 'MAMA'


print('\nfoo3')
def foo4(x, y, z=0):
    return 100*x + 10*y + z


print(foo4(1, 2, 3))
print(foo4(z=1, x=2, y=3)) #named parameters
print(foo4(1, 2))


print('\nbar1:')
def bar1(args):
    for arg in args:
        print('bar1 arg =', arg)

bar1([1,2,3])        


print('\nbar2:')
def bar2(*args):                  # произвольное количество параметров
    for arg in args:
        print('bar2 arg =', arg)

bar2()
bar2(1,2,3)
bar2('yelly', 'fish')
bar2(['the', 'list', 'of', 'strings'])


print('\nbar3:')
def bar3(*args, named_parameter='bar'):                  # произвольное количество параметров
    for arg in args:
        print(named_parameter, 'arg =', arg)

bar3()
bar3(4,5,6)
bar3('yelly', 'fish')
bar3('yelly', 'fish', named_parameter='SEPARATOR')
