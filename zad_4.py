def sum_checker(x, y, z):
    return x + y >= z


uno = 10
due = 12
tre = 22

czy_wieksze = sum_checker(uno, due, tre)

if czy_wieksze:
    print(f"Suma dwóch pierwszych liczb jest wieksza lub równa trzeciej")
else:
    print(f"Suma dwóch pierwszych liczb nie jest wieksza lub równa trzeciej")
