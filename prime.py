for number in range(2,15):
    print("number is " + str(number))
    for x in range(2, number):
        print("x is " + str(x))
        if number % x == 0:
            print(number, 'equals', x, '*', number//x)
            break
    else:
        # loop fell through without finding a factor
        print(number, 'is a prime number')

print("That is it")
