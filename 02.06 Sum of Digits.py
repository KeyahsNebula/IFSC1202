a = int(input('Enter a 3 Digit Number: '))
b = a // 100
c = a // 10
d = c % 10
e = a % 10
f = b+d+e
print('Sum of Digits: {}'.format(f))
