# coding=utf-8

from prime_group import PrimeGroup

class Verifier:
    def __init__(self, group, g, c, y, v):
        self.group = group
        self.g = g
        self.c = c
        self.y = y
        self.v = v

    def challenge(self, cv_tuple):
        a = self.group.generate_random_vector(1)[0]
        self.c = self.group.update_num(self.c, a, cv_tuple[0], cv_tuple[1])
        self.v = self.group.update_num(self.v, a, cv_tuple[2], cv_tuple[3])

        self.g = self.group.update_list(self.g, a)
        self.y = self.group.update_list(self.y, a)

        self.print_status("challenge")
        return (a, self.c, self.v, self.g, self.y)

    def final_verify(self, final_tuple):
        u = final_tuple[0]
        if self.group.multiply(u, self.g[0]) == c and self.group.multiply(u, self.y[0]) == v :
            print("True!")
        else:
            print("False!")

    def print_status(self, str):
        print(str, self.g, self.c, self.y, self.v)
    

class Prover:
    def __init__(self, group, u):
        self.group = group
        self.u = u

    def init_g(self, g):
        self.g = g
        self.c = self.group.inner_product(u, g)
        return self.c

    def init_y(self, y):
        self.y = y
        self.v = self.group.inner_product(u, y)
        return self.v
    
    def one_prove(self):
        length = len(self.u)
        print("length", length)
        
        if length == 1:
            return (self.u)
        else:
            ul = self.u[ : length//2]
            ur = self.u[length//2 : ]
            gl = self.g[ : length//2]
            gr = self.g[length//2 : ]
            yl = self.y[ : length//2]
            yr = self.y[length//2 : ]

            cl = self.group.inner_product(ul, gr)
            cr = self.group.inner_product(ur, gl)
            vl = self.group.inner_product(ul, yr)
            vr = self.group.inner_product(ur, yl)

            self.print_status("one_prove")
            return (cl, cr, vl, vr)

    def update(self, update_tuple):
        (a, c, v, g, y) = update_tuple
        self.c = c
        self.v = v
        self.g = g
        self.y = y
        self.u = self.group.update_list(self.u, a)
        self.print_status("update")
        return

    def print_status(self, str):
        print(str, self.u, self.g, self.c, self.y, self.v)

if __name__ == "__main__":
    group = PrimeGroup(101)
    u = group.generate_random_vector(8)
    prover = Prover(group, u)

    g = group.generate_random_vector(8)
    c = prover.init_g(g)

    y = group.generate_random_vector(8)
    v = prover.init_y(y)

    verifier = Verifier(group, g, c, y, v)

    # start
    while True:
        cv_tuple = prover.one_prove()
        print("cv_tuple : ", cv_tuple)
        if len(cv_tuple) == 1:
            
            verifier.final_verify(cv_tuple)
            break
        update_tuple = verifier.challenge(cv_tuple)
        print("update_tuple : ", update_tuple)
        prover.update(update_tuple)




