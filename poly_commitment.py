# coding=utf-8

from prime_group import PrimeGroup

from EllipticCurves import EllipticPoint,BitcoinEllipticPoint
from FieldElement import FieldElemet,BitcoinFieldElement

A = 0
B = 7
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
G = BitcoinEllipticPoint(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
                         0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
O=N*G
P = 2 ** 256 - 2 ** 32 - 977

def inner_product(list1, list2):
    sum = O
    if(len(list1) != len(list2)):
        print("length error!", list1, list2)
    if type(list2[0])==int:
        return inner_product(list2,list1)
    for i  in range(len(list1)):
        #print(list1[i]*list2[i])
        sum = sum+(list1[i]*list2[i])
    return sum

def update_num(group, n, a, left, right):
    result = n
    result = group.multiply(a, a)*left+ result
    result = group.multiply(group.divide(1, a), group.divide(1, a))*right+ result
    return result

def update_list(group, list, a):
    mid_index = len(list) // 2
    left_list = [group.divide(1, a)*item for item in list[:mid_index]]
    right_list = [a*item for item in list[mid_index:]]
    return [ item1+item2 for item1, item2 in zip(left_list, right_list)]

def update_ulist(group, list, a):
    mid_index = len(list) // 2
    left_list = [a*item for item in list[:mid_index]]
    right_list = [group.divide(1, a)*item for item in list[mid_index:]]
    return [ item1+item2 for item1, item2 in zip(left_list, right_list)]        



class Verifier:
    def __init__(self, group, g, c, y, v):
        self.group = group
        self.g = g
        self.c = c
        self.y = y
        self.v = v

    def challenge(self, cv_tuple):
        a = self.group.generate_random_vector(1)[0]
        self.c = update_num(self.group,self.c, a, cv_tuple[0], cv_tuple[1])
        self.v = update_num(self.group,self.v, a, cv_tuple[2], cv_tuple[3])

        self.g = update_list(self.group,self.g, a)
        self.y = update_list(self.group,self.y, a)

        #self.print_status("challenge: " + str(a))
        return (a, self.c, self.v, self.g, self.y)

    def final_verify(self, final_tuple):
        u = final_tuple[0]
        #self.print_status("final_verify: " + str(u))
        if self.g[0]*u == self.c and self.y[0]*u == self.v :
            print("True!")
            return True
        else:
            print("False!")
            return False

    def print_status(self, str):
        print(str, self.g, self.c, self.y, self.v)
    

class Prover:
    def __init__(self, group, u):
        self.group = group
        self.u = u

    def init_g(self, g):
        self.g = g
        self.c = inner_product(g, self.u)
        return self.c

    def init_y(self, y):
        self.y = y
        self.v = inner_product(y, self.u)
        return self.v
    
    def one_prove(self):
        length = len(self.u)
        #print("length", length)
        
        if length == 1:
            return (self.u)
        else:
            ul = self.u[ : length//2]
            ur = self.u[length//2 : ]
            gl = self.g[ : length//2]
            gr = self.g[length//2 : ]
            yl = self.y[ : length//2]
            yr = self.y[length//2 : ]

            cl = inner_product(ul, gr)
            cr = inner_product(ur, gl)
            vl = inner_product(ul, yr)
            vr = inner_product(ur, yl)

            #self.print_status("one_prove")
            return (cl, cr, vl, vr)

    def update(self, update_tuple):
        (a, c, v, g, y) = update_tuple
        self.c = c
        self.v = v
        self.g = g
        self.y = y
        self.u = update_ulist(self.group,self.u, a)
        #self.print_status("update")
        return

    def print_status(self, str):
        print(str, self.u, self.g, self.c, self.y, self.v)

def test_poly_commitment(hack):
    group = PrimeGroup(N)
    u = group.generate_random_vector(8)
    prover = Prover(group, [item*G for item in u])

    g = group.generate_random_vector(8)
    c = prover.init_g(g)

    y = group.generate_random_vector(8)
    v = prover.init_y(y)

    verifier = Verifier(group, g, c, y, v)

    #if hacked
    if hack:
        hack_u = group.generate_random_vector(8)
        prover.u = [item*G for item in hack_u]

    # start
    while True:
        cv_tuple = prover.one_prove()
        #print("cv_tuple : ", cv_tuple)
        if len(cv_tuple) == 1:
            return verifier.final_verify(cv_tuple)
            break
        update_tuple = verifier.challenge(cv_tuple)
        #print("update_tuple : ", update_tuple)
        prover.update(update_tuple)

if __name__ == "__main__":
    success = 0
    for i in range(10):
        if test_poly_commitment(False):
            success += 1
    for i in range(10):
        if not test_poly_commitment(True):
            success += 1
    if success == 20:
        print("验证成功！")




