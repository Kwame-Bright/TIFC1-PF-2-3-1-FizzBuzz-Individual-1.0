for i in range(1, 1001):
    if i % 5 == 0 and i % 3 == 0:
        print("Fizzbuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
