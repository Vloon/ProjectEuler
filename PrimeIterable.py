import sys, math
class PrimeIterable:
    def __init__(self, max = 1000, key = "max"):
        self.max = max
        self.key = key

    def __iter__(self):
        self.previous_primes = [2,3] ## Add three because then we can go over only odd numbers.
        return self

    def __next__(self):
        for i in range(self.previous_primes[-1]+2,sys.maxsize**10,2):
            if self.key == "max":
                if i >= self.max:
                    raise StopIteration
            elif self.key == "index":
                if len(self.previous_primes) >= self.max:
                    raise StopIteration

            if self.is_prime(i):
                self.previous_primes.append(i)
                return i

    def is_prime(self, number):
        return len([x for x in self.get_sqrt_prime_list(number) if number%x == 0]) == 0

    def get_sqrt_prime_list(self, number):
        return [x for x in self.previous_primes if x < int(math.sqrt(number)+1)]
