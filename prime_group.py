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
    
    def generate_random_vector(self, len):
        pass

if __name__ == "__main__":
    # 创建一个 101 阶素数群的实例
    prime_Group = PrimeGroup(101)

    # 测试加法
    result = prime_Group.add(200, 300)
    print("200 + 300 =", result)

    # 测试减法
    result = prime_Group.subtract(80, 90)
    print("80 - 90 =", result)

    # 测试乘法
    result = prime_Group.multiply(5, 70)
    print("5 * 70 =", result)

    # 测试除法
    result = prime_Group.divide(80, 4)
    print("80 / 4 =", result)
