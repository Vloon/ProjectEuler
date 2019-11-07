import math
def get_triplet(n,m):
    """
    Returns the tuple (a,b,c) for input n and m based on Euclids formula.
    """
    return (m**2 - n**2, 2*m*n, m**2 + n**2)

def get_pythagorean_triplet(number):
    for n in range(0, number):
        for m in range(n+1,number):
            a,b,c = get_triplet(n,m)
            if a + b + c == number:
                return(a,b,c)

a,b,c = get_pythagorean_triplet(1000)
print(a*b*c)
