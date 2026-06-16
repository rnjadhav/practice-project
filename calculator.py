import math

def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100  # bug: should validate inputs
    return price - discount

def divide(a, b):
    return a / b  # bug: no division by zero check

def get_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)  # bug: crashes if list is empty

def find_max(items):
    max_val = 0  # bug: wrong initial value, fails for all-negative lists
    for item in items:
        if item > max_val:
            max_val = item
    return max_val

def is_palindrome(s):
    return s == s[::-1]  # bug: doesn't handle case-insensitive check or spaces

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def count_words(text):
    words = text.split(" ")
    return len(words)  # bug: doesn't handle multiple spaces or empty string

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # bug: no check for negative input (infinite recursion)

def apply_tax(prices, tax_rate):
    result = []
    for i in range(len(prices) + 1):  # bug: off-by-one error (range too large)
        result.append(prices[i] * (1 + tax_rate))
    return result


if __name__ == "__main__":
    print(calculate_discount(100, 20))
    print(divide(10, 0))
    print(get_average([]))
    print(find_max([-5, -3, -1]))
    print(is_palindrome("Racecar"))
    print(count_words("hello  world"))
    print(factorial(-1))
    print(apply_tax([10, 20, 30], 0.1))
