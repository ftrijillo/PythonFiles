num = 100

def print_primes():
    for i in range(1, num):
        for j in range(2, i):
            #This will not run when i is 1 or 2 because of the range command, so both
            #1 and 2 will be counted as prime numbers automatically.
            if (i % j) == 0:
                break
        else:
            print(i, "is a prime number")

print_primes()

