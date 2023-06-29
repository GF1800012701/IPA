import random

class PrimeGroup:
    def __init__(self, order):
        self.p = order  # 素数p作为群的模数

    def add(self, a, b):
        return (a + b) % self.p

    def subtract(self, a, b):
        return (a - b) % self.p

    def multiply(self, a, b):
        return (a * b) % self.p

    def divide(self, a, b):
        inverse_b = self.inverse(b)
        return (a * inverse_b) % self.p

    def inverse(self, a):
        return pow(a, self.p - 2, self.p)  # 使用费马小定理计算模逆元
    
    def generate_random_vector(self, l):
        return [random.randint(2, self.p-1) for _ in range(l)]