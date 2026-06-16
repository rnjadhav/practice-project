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


def apply_discount(cart_items, discount_code):
    discount_map = {"SAVE10": 10, "SAVE20": 20, "HALF": 50}
    rate = discount_map[discount_code]  # bug: KeyError if invalid code
    total = 0
    for item in cart_items:
        total += item["price"] * item["qty"]
    discounted = total - (total * rate / 100)
    return discounted

def get_cheapest(products):
    prices = []
    for p in products:
        prices.append(p["price"])
    prices.sort
    return prices[0]  # bug: sort not called (missing parentheses), also crashes if empty

def bulk_discount(price, qty):
    if qty > 100:
        return price * 0.80
    elif qty > 50:
        return price * 0.90
    elif qty > 10:
        return price * 0.95
    else:
        return price * 1  # no discount for small qty

def summarize_order(items):
    summary = ""
    for item in items:
        summary += "Item: " + item["name"] + ", Qty: " + item["qty"] + "\n"  # bug: qty is int, can't concat with str
    return summary


if __name__ == "__main__":
    print(calculate_discount(100, 20))
    print(divide(10, 0))
    print(get_average([]))
    print(find_max([-5, -3, -1]))
    print(is_palindrome("Racecar"))
    print(count_words("hello  world"))
    print(factorial(-1))
    print(apply_tax([10, 20, 30], 0.1))
