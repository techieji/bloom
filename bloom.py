from math import log, ceil

class bloom:
    def __init__(self, b, k=3):
        self.ba = bytearray(b)
        self.bitlen = b * 8
        self.k = k

    def _set_bit(self, n, v):
        n = n % self.bitlen
        print(n)
        self.ba[n // 8] ^= v << (n % 8)

    def _get_bit(self, n):
        n = n % self.bitlen
        print('get', n)
        return (self.ba[n // 8] >> (n % 8)) % 2

    @staticmethod
    def _split_hash(h, k):
        l = ceil(log(h, 2))         # Python numbers are variable length?
        step = l // k
        prev = 0
        for i in range(k):
            mv = i * step
            prev = h - (h >> mv << mv) - prev
            yield prev

    def __contains__(self, k):
        return all(map(self._get_bit, bloom._split_hash(hash(k), self.k)))

    def add(self, item):
        for x in bloom._split_hash(hash(item), self.k):
            self._set_bit(x, 1)

b = bloom(10)
b.add(10)
print(10 in b)
