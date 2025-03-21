# Problem 1: Calculate the Sum of Natural Numbers
print("***Sum of Natural Numbers***")
n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum of natural numbers:", total)

# Problem 2: Check for Prime Number
print("***Prime or Not Prime***")
n = int(input("Enter a number: "))
if n <= 1:
    print("Not Prime")
else:
    i = 2
    is_prime = True
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

# Problem 3: Find the Maximum of Three Numbers
print("***Maximum Number***")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
print("Maximum number:", max_num)

# Problem 4: Factorial Calculation
print("***Factorial of Number***")
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)

# Problem 5: Check if a Number is Even or Odd
print("***Even or Odd***")
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Problem 6: Check if a Number is an Armstrong Number
print("***Armstrong Number or Not***")
n = int(input("Enter a number: "))
num = n
digits = len(str(n))
sum_of_powers = 0
while num > 0:
    digit = num % 10
    sum_of_powers += digit ** digits
    num //= 10
if sum_of_powers == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
