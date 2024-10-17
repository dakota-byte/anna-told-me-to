from collections import defaultdict

def xor_product_slow(integer_a: int, integer_b: int) -> int:
    a = str(bin(integer_a))[2:]
    b = str(bin(integer_b))[2:]

    # "manually" create intermediate step of long multiplication
    intermediate = []
    for i in range(len(b)):
        bit = b[i]
        if bit == "1":
            # if the bit is 1 in b, then we add another a
            # but we need to indent it depending on the pos
            # which is len(b) - 1 - i

            intermediate.append(a + "0"*(len(b)-1-i))

    xor_product = 0
    for step in intermediate:
        xor_product = xor_product ^ int(step, 2)

    return xor_product
# test case from wikipedia:
# print(xor_product_slow(int("10010110", 2), int("10100010", 2)))
# print(int("101100011101100",2))

# multiplication of polynomials
# definetly NOT faster
def xor_polynomial(integer_a, integer_b):
    a, b = str(bin(integer_a))[2:], str(bin(integer_b))[2:]
    polynomial_a, polynomial_b = [], []

    for bit in range(len(a)-1, -1, -1):
        if a[bit] == "1":
            polynomial_a.append(len(a)-bit-1)

    for bit in range(len(b)-1, -1, -1):
        if b[bit] == "1":
            polynomial_b.append(len(b)-bit-1)

    mult = []
    for i in polynomial_a:
        for j in polynomial_b:
            ij = i+j
            if ij in mult:
                mult.remove(ij)
            else:
                mult.append(ij)

    ans = 0
    for bit_rep in mult:
        ans += 2**bit_rep

    return ans
# wikipedia example: x^7+x^4+x^2+x^1 * x^7+x^5+x^1
# print(xor_polynomial(int("10010110", 2), int("10100010", 2)))
# print(int("101100011101100",2))

# no more space complexity! begone!!!
# CREDIT: to chatgpt, as I was looking for possible optimizations :(
def xor_product_bitwise(a, b):
    indent = 0
    product = 0

    while b > 0:
        if b & 1:
            product ^= a << indent
        indent += 1
        b = b >> 1

    return product

# oh dear lord
def is_xor_prime(n):
    count_n = 0  # track how many times n appears instead of hashmap lolll

    for i in range(1, n+1):
        for j in range(1, n+1):
            xor_prod = xor_product(i, j)
            if xor_prod == n:
                count_n += 1
                if count_n > 2:  # Early exit if count exceeds 2
                    return False

    return count_n == 2
# print(is_xor_prime(41))

# first attempt grrrr
# modifications made: 3rd attempts
def attempt_1(n):
    # starting at 3, because i know 2 is an xor_prime and
    # i dont want an extra edge case for the even check
    xor_primes = 1
    current_try = 3
    while xor_primes < n:
        if current_try % 2 == 0:
            current_try += 1
            continue # they never seem to be even so we half the search space

        if is_xor_prime(current_try):
            xor_primes += 1
            print("xor_prime #" + str(xor_primes) + " = " + str(current_try))
        current_try += 1

attempt_1(5000000)

def xor_prime_table(n):
    counts = defaultdict(int) # hashmap
    
    for i in range(1, n+1):
        print(str((i/n * 100)) + "%")
        for j in range(1, n+1):
            xor_prod = xor_product(i, j)
            counts[xor_prod] += 1
    return counts

# not in order but faster
# a lot faster
# but not fast enough
# and not in order
def attempt_2(n):
    t = xor_prime_table(n)
    count = 0
    print(t)
    for key, val in t.items():
        if val == 2:
            count += 1
            print(key)
        if count == n:
            break
    print(str(count) + " found")