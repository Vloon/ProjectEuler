def get_primes(nr_primes):
    primes = []
    for n in range(2,nr_primes):
        is_divisible = False
        for p in primes:
            if n%p == 0:
                is_divisible = True
        if not is_divisible:
            primes.append(n)
    return primes

def main():
    primes = get_primes(10000)
    target = 600851475143
    i = 0
    while target >= primes[i]:
        if target%primes[i] == 0:
            print(primes[i],target)
            target = target/primes[i]
        i += 1
# main()
### This code is fugly
