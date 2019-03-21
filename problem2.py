max = 4000000
fib = [1,2]
while fib[-1] < max:
    fib.append(fib[-2]+fib[-1])
fib.pop() ## Last element > max, so remove it.

even_fib = [x for x in fib if x%2==0]
print(sum(even_fib))
