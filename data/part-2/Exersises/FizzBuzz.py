num = int(input("Number: "))

if num % 3:
    print(num)
    print("Fizz")
elif num % 5:
    print(num)
    print("Buzz")
elif num % 3 and num % 5:
    print("FizzBuzz")
