a = input("Enter Classroom A: ")
z = int(a)
b = input("Enter Classroom B: ")
y = int(b)
c = input("Enter Classroom C: ")
x = int(c)
fulldeska = z // 2
partialdeska = z % 2
fulldeskb = y // 2
partialdeskb = y % 2
fulldeskc = x // 2
partialdeskc = x % 2
d = fulldeska+partialdeska+fulldeskb+partialdeskb+fulldeskc+partialdeskc
print(d)
