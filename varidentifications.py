# Variable identifications and Constants
# Переменные - это ссылки на объект?
a = 5
b = 5
print('a=b=5')
# Test one.
if a == b:
    print('Yes: a == b')

# Test two.
if a is b:
    print('Yes: a is b')

# Test two.
if not id(a) is id(b):
    print('NOT: id(a) is id(b)')
