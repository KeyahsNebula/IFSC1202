print("First Timestamp")
h1 = int(input("Enter Hour: "))
m1 = int(input("Enter Minute: "))
s1 = int(input("Enter Seconds: "))
t1 = h1 * 3600 + m1 * 60 + s1
print("Second Timestamp")
h2 = int(input("Enter Hour: "))
m2 = int(input("Enter Minute: "))
s2 =int(input("Enter Seconds: "))
t2 = h2 * 3600 + m2 * 60 + s2
print(t2 - t1)


