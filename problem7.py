import PrimeIterable as pi

y = 0
for x in pi.PrimeIterable(10001, key = "index"):
    y = x

print(y)
