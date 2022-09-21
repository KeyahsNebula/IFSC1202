print("Winners and Losers - Human is Even, Computer is Odd")
for x in range(1,5):
    print("Round: {}".format(x))
    a = int("Enter your guess: ")
    print("Human Guess: " + a)
    import random
    v = int(random.randint(1,5))
    print("Computers Guess: " + v)
    sum = (a+v) % 2
    if sum > 0:
        print("Sum is Odd")
    else:
        print("Sum is Even")
    print("Human Score: - Computer Score: ")
if Human Score > Computer Score:
    print("Human Wins")
    else:
        print("Computer Wins")