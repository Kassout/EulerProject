
def problem():
    """Find the largest palindrome made from the product of two 3-digit numbers."""
    n_digits = 3
    i = j = int((n_digits*1000)/n_digits) - 1
    list = []
    while i >= 0:
        if str(i * j) == str(i*j)[:3] + str(i * j)[::-1][3:6]:
            list.append(i * j)
        if j > 0:
            j -= 1
        else:
            i -= 1
            j = i
    result = max(list)
    return result

    
if __name__ == "__main__":
    value = problem()
    print(value)
