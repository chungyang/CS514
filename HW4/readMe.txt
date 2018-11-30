Heavy Hitter Algorithm is implemented as follow

1. keep a count on total element N

2. get frequency f of incoming data from count min sketch

3. if f >=  N / k, insert the data into heap and delete the previous occurrence

4, delete all element from heap that has f < N / k

5. scan the heap at the end, return all elements that have f >= N / k