import time
import random


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False

    return True


test = [i for i in range(2, 1000, random.randint(2, 30))]
start = time.time()

for x in test:
    print(str(x) + ' - ' + str(is_prime(x)))

end = time.time()
print('Time ', end - start)
