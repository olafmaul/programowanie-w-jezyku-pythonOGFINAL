def greet():
    return (f"Hi,\n"
            f"this is your final price after the discount (of {percentage}%):"
            f"\n")


def calculate_discount(price, percentage):
    return price * (1 - percentage / 100)

price = 207652
percentage = 20

after_discount = calculate_discount(price, percentage)

print(greet(),after_discount)