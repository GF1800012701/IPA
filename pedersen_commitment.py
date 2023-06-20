import random

class PedersenCommitment:
    def __init__(self, p, g, h):
        self.p = p  # 素数p作为群的模数
        self.g = g  # 生成元g
        self.h = h  # 另一个生成元h

    def commit(self, value, randomness):
        r = random.randint(1, self.p - 1)  # 选择一个随机数r
        commitment = (self.g**value * self.h**randomness) % self.p  # 计算承诺
        return commitment, r

    def verify(self, value, randomness, commitment):
        result = (self.g**value * self.h**randomness) % self.p
        return commitment == result

# 定义群的参数
p = 101  # 101是一个质数
g = 2  # 使用2作为生成元
h = 3  # 使用3作为另一个生成元

# 创建Pedersen承诺实例
commitment_scheme = PedersenCommitment(p, g, h)

# 假设我们要承诺的值是10，随机数是5
value = 10
randomness = 5

# 承诺阶段
commitment, r = commitment_scheme.commit(value, randomness)
print("Commitment:", commitment)

# 验证阶段
is_valid = commitment_scheme.verify(value, randomness, commitment)
print("Is Valid:", is_valid)
