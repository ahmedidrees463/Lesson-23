number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

largest = number1

if number2 > largest:
    largest = number2

while True:
    if largest % number1 == 0 and largest % number2 == 0:
        lcm = largest
        break
    largest += 1

print("LCM is:", lcm)