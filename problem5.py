def get_prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
    return factors

def flatten(lst):
    flat_lst = []
    for sublist in lst:
        for e in sublist:
            flat_lst.append(e)
    return flat_lst

def powerize(factors_list):
    power_list = []
    for factors in factors_list:
        ## List of factors
        if len(factors) == 1:
            power_list.append([(factors[0],1)]) ## Hardcody but whatever
            continue ## next iter
        factors.sort()
        for i in range(len(factors)):
            if factors[i] == factors[i+1]

def get_prime_factors_list(lst):
    factors = []
    for n in lst:
        factors.append(get_prime_factors(n))
    return factors

def lcm(max_nr):
    nrs = list(range(2,max_nr+1))
    factors_list = get_prime_factors_list(nrs)
    largest_prime = max(flatten(factors_list))

    print(largest_prime)
    return factors_list


print(lcm(20))
