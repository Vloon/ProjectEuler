def get_nrs(max_nr):
    lst = list(range(max_nr,1,-1))
    i = 0
    while i < len(lst):
        j = i+1
        while j < len(lst):
            if lst[i]%lst[j]==0:
                lst.pop(j)
                j -= 1
            j += 1
        i +=1
    return list(reversed(lst))



def problem5(max_nr):
    lst = get_nrs(max_nr)
    print(lst) ## Check if sorted
    i = lst[-1] ## Start at max in the list
    while True:
        for n in lst:
            if i%n == 0:
                continue
            else:
                 break
            return n
        i += 2 ## only check even numbers

problem5(20)
