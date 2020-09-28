a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)


class CountDown:
    def __init__(self, start):
        self._start = start
    
    def __iter__(self):
        n = self._start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self._start:
            yield n
            n += 1
