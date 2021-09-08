def divisors(n):
    l = [x for x in range(2, n) if n % x == 0]
    if len(l) == 0:
        return str(n) + " is prime"
    return l
