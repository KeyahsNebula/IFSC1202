a = int(input('Enter a Four Digit Number: '))
b = a // 1000
c = a //100
d = c % 10
e = a //10
f = e % 10
h = a % 1000
i = h % 100
j = i % 10
if b==j and d==f:
    print('YES')
else:
    print('NO')