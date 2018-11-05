
import math
import numpy as np

class FM:

    def __init__(self, range):
        """
        :param range: a tuple that represents the range of the uniformly distributed set of integers
        :
        """

        # for hash function h(x) = ax + b mod m, pick a,b from {0,1,2,... m -1} and store a and b
        self.range = range
        self.m = self.getAPrime(range[1], 2 * range[1])
        print(self.m)
        self.a,self.b = np.random.randint(0, self.m - 1, 2)
        self.min_hash = math.inf

    def listen(self, data):
        """
        take in stream data and process it
        :param data: stream data
        """
        hash_value = self.hash(data)

        if self.min_hash > hash_value:
            self.min_hash = hash_value


    def approximate(self):

        if self.min_hash == 0:
            return self.range[1] + 1
        else:
            return math.ceil((self.range[1] + 1) / self.min_hash)




    def hash(self, n):
        """

        :param n: number to hash
        :return: hash value
        """
        hash_value = (self.a * n + self.b) % self.m

        return hash_value


    def trailing_zeros(self, i):
        """
        :param i: binary number in a string
        :return: number of trailing zeros in its binary form
        """
        str_i = str(i)
        return len(str_i) - len(str_i.rstrip('0'))


    def getAPrime(self, lower, upper):
        """
        Get a prime number that's randomly picked from a list of primes between the specified range

        :param lower: lower range
        :param upper: upper range
        :return: list of primes within range
        """
        primes = []

        for num in range(lower, upper + 1):

            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    primes.append(num)

        index = np.random.randint(0, len(primes))
        return primes[index]

# Use python built-in data structure set to calculate number of unique integer
def count_distinct(data):
    """

    :param data: stream data
    :return: number of unique values in data
    """
    s = set()

    for d in data:
        s.add(d)

    return len(s)

# Put data in a list so count_distinct can compute true number of distinct values
data = np.random.randint(0,9999, 10000)

# Stream data with a loop and use flajolet-martin algorithm to approximate number of distinct value
fm = FM((0,9999))

for d in data:
    fm.listen(d)

print("approximate of distinct values: " , fm.approximate())
print("real number of distinct values ", count_distinct(data))
