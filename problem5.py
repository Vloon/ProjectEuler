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
        power_list.append({i:factors.count(i) for i in factors})
    return power_list


def get_prime_factors_list(lst):
    factors = []
    for n in lst:
        factors.append(get_prime_factors(n))
    return factors

def get_scm(powers_list):
    scm = {}
    for powers in powers_list:
        for b, p in powers.items(): # base^power
            try:
                p_in_l = scm[b]
                scm[b] = max(p_in_l,p)
            except:
                scm[b] = p
    return scm

def defactorize(powers_dict):
    scm = 1
    for b,p in powers_dict.items():
        scm *= b**p
    return scm


def scm(max_nr):
    nrs = list(range(2,max_nr+1))
    factors_list = get_prime_factors_list(nrs)
    powers_list = powerize(factors_list)
    #powers_list = sorted(powers_list, key = lambda x: len(x))
    #print(powers_list)
    scm = get_scm(powers_list)
    scm = defactorize(scm)
    return scm


print(scm(20))
