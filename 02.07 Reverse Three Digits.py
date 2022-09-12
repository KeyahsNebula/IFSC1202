number1 = int(input('Enter a a Digit Number: '))
n2 = number1 // 100
n3 = number1 % 100
n4 = n3 // 10
n5 = number1 % 10
n6 = (n2+ n4+n5)
print('Reverse of Digits: {}'.format(n2, n4, n5))


