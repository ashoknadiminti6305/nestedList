# Sum of digits
num1 = 15
sum_digits = 0
temp = num1

while temp > 0:
    d = temp % 10
    sum_digits += d
    temp //= 10

print("Sum of digits:", sum_digits)


# Reverse a number
num2 = 15
rev = 0
temp = num2

while temp > 0:
    d = temp % 10
    rev = rev * 10 + d
    temp //= 10

print("Reverse:", rev)


# Count digits
num3 = 15
count = 0
temp = num3

while temp > 0:
    count += 1
    temp //= 10

print("Digit count:", count)


# Check even or odd
num4 = 15
if num4 % 2 == 0:
    print("Even")
else:
    print("Odd")


# Check prime number
num5 = 10

if num5 <= 1:
    print("Not Prime")
else:
    for i in range(2, int(num5 ** 0.5) + 1):
        if num5 % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


# Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(4))


# Factors of a number
num6 = 12
factors = []

for i in range(1, num6 + 1):
    if num6 % i == 0:
        factors.append(i)

print("Factors:", factors)


# Palindrome
num7 = 121
temp = num7
rev = 0

while temp > 0:
    d = temp % 10
    rev = rev * 10 + d
    temp //= 10

if rev == num7:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")


# Armstrong number
num8 = 153
temp = num8
armstrong_sum = 0

while temp > 0:
    d = temp % 10
    armstrong_sum += d ** 3
    temp //= 10

if armstrong_sum == num8:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


# GCD / HCF
a = 12
b = 18

x, y = a, b

while y:
    x, y = y, x % y

print("GCD:", x)