import numpy as np
import math


class hash_function:

    def __init__(self, w):

        self.w = w
        self.a, self.b = np.random.randint(0, w, 2)

    def hash(self, n):
        """
        :param n: value to hash
        :return: a hash_value
        """

        hash_value = (self.a * n + self.b) % self.w

        return hash_value


class count_min_sketch:

    def __init__(self, epislon, delta):

        # Error parameters. Count min sketch guarantees that the estimate a' <= a + epislon * N with probability 1 - delta
        # a': estimate frequency
        # a: true frequency
        # N: stream size
        self.epislon = epislon
        self.delta = delta

        # Number of hash function, or the row number of count min sketch table
        self.d = math.ceil(math.log(1 / self.delta))

        # hash function that does following h: {1,2,....m} ----> {1,2,.....w}, or column number of count min sketch table
        self.w = math.ceil(math.exp(1) / self.epislon)

        self.count_table = np.zeros((self.d, self.w))

        self.hash_functions = []

        self.__generateHashFuntions()


    def __generateHashFuntions(self):

        # Get hash functions
        for i in range(self.d):
            self.hash_functions.append(hash_function(self.w))

    def listen(self, x):
        """
        This function listens to the stream data and perform count min sketch on the stream data
        :param x: Stream data
        """

        for i in range(len(self.hash_functions)):

            hash_value = self.hash_functions[i].hash(x)

            self.count_table[i][hash_value] += 1

    def queryFrequency(self, x):
        """
        This function returns the estimated frequency of stream data x
        :param x: stream data
        :return: estimated frequency of stream data
        """
        counts = []

        for i in range(len(self.hash_functions)):

            hash_value = self.hash_functions[i].hash(x)

            count = self.count_table[i][hash_value]

            counts.append(count)

        return min(counts)


import heapq
h = []
# Minimum frequency to be considered as a heavy hitter
k = 30
c = count_min_sketch(epislon = 0.1, delta = 0.1)
total_count = 0

for i in range(10000):

    data = np.random.randint(0, 499)

    c.listen(data)

    total_count += 1

    f = c.queryFrequency(data)

    if f > total_count / k:

        # Delete previous occurrence of data
        for j in range(len(h)):

            if h[j][1] == data:
                h.pop(j)
                break

        heapq.heappush(h, (f, data))

    # Delete elements that has count less than total_count / k
    while h:
        element = h.pop(0)

        # Min element is bigger than total_count / k, stop deleting and put it back to the heap
        if element[0] >= total_count / k:
            heapq.heappush(h, element)
            break

print("list of heavy hitters")
for element in h:

    print("value: ", element[1], "count: ", element[0])











