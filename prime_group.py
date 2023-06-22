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

    def inner_product(self, list1, list2):
        sum = 0
        if(len(list1) != len(list2)):
            print("length error!", list1, list2)
        for i  in range(len(list1)):
            sum = self.add(sum, self.multiply(list1[i], list2[i]))
        return sum

    def update_num(self, n, a, left, right):
        result = n
        result = self.add(self.multiply(self.multiply(left, a), a), result)
        result = self.add(self.divide(self.divide(right, a), a), result)
        return result

    def update_list(self, list, a):
        mid_index = len(list) // 2
        left_list = [self.multiply(item, a) for item in list[:mid_index]]
        right_list = [self.divide(item, a) for item in list[mid_index:]]
        return [self.add(item1, item2) for item1, item2 in zip(left_list, right_list)]


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

#如何在python中生成一个大于1 小于p的整数随机数？如何生成这样的随机数的list，需要指定长度l？