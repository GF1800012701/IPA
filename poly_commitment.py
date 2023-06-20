# coding=utf-8

from prime_group import PrimeGroup

class Verifier:
    def __init__(self, group):
        self.group = group

    

class Prover:
    def __init__(self, group, u):
        self.group = group
        self.u = u



if __name__ == "__main__":
    group = PrimeGroup(101)
    u = group.generate_random_vector(8)


    g = group.generate_random_vector(8)
    y = group.generate_random_vector(8)


