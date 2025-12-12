def parzysta_checker(x):
    return x % 2 == 0

x = 10

parzysta_check = parzysta_checker(x)

if parzysta_check:
   print('Jest parzysta')
else:
    print('Nie jest parzysta')