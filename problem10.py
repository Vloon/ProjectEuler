import PrimeIterable as pi

max = 2000000
pl = []
for x in pi.PrimeIterable(max):
    pl.append(x)

print(sum(pl))
