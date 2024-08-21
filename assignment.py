name = input("Enter your name: ")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))
print(f" Hello, {name}! Let's explore your favorite numbers:")

numbers=[first, second, third]
even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
for num, info in even_odd_info:
    print(f"The number {num} is {info}.")

for num in numbers:
    square=num**2
    print(f"The number {num} and its square: ({num} ,{square})")
totalsum=sum(numbers)
print(f"Amazing! The sum of your favorite numbers is: {totalsum}")
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n <= 3:
        return True   # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False  # Exclude multiples of 2 and 3
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
if is_prime(totalsum):
    print(f"Wow, {totalsum} is a prime number! That's awesome!")
else:
    print(f"{totalsum} is not a prime number, but it's still a cool number!")