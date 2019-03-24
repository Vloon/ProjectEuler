def sum_of_squares(max_nr):
    s = 0
    for n in range(1,max_nr+1):
        s += n**2
    return s

def square_of_sum(max_nr):
    s = 0
    for n in range(1,max_nr+1):
        s += n
    return s**2

n = 100
print(square_of_sum(n) - sum_of_squares(n))
