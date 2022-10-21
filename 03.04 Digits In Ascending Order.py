a = int(input('Enter a Number: '))
b = a//100
c = a % 100
d = c //10
e = a % 10
if b <= d <= e:
    print('Yes')
else:
    print('No')
