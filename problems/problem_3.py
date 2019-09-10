
def problem():
    """What is the largest prime factor of the number 600851475143 ?"""
    number = 600_851_475_143
    i = 2
    for i in range(2, number):
        if i >= number:
            break
        if number % i == 0:
            number /= i
            i -= 1
    result = i
    return result
    
    
if __name__ == "__main__":
    value = problem()
    print(value)
