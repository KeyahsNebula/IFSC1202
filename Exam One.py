print("Winners and Losers - Human is Even, Computer is Odd")
for x in range(1,5):
    print("Round: {}".format(x))
    x = int(input("Human Guess: "))
    import random
    v = int(random.randint(1,5))
    print("Computers Guess: " + v)
    sum = (x+v) // 2
    if sum > 0:
        print("Sum is Odd")
        else:
            print("Sum is Even")
    