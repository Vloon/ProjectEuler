def is_palindrome(nr):
    string = str(nr)
    i = 0
    j = len(string)-1
    while i < j:
        if not string[i] == string[j]:
            return False
        i += 1
        j -= 1
    return True

def find_largest_palindrome():
    palindromes = []
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            prod = i*j
            if is_palindrome(prod):
                palindromes.append(prod)
    return max(palindromes)
print(find_largest_palindrome())
