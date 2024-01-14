class Q():
    var_Q='Hello'
    def __init__(self):
        self.q_value=0

class A():
    var_A='Hello'
    def __init__(self):
        self.a_value=1

class B(A):
    var_B='Hello'
    def __init__(self):
        self.b_value=2
class C(Q)
    var_C='Hello'
    def __init__(self):
        self.c_value=3
class D(B,C):
    var_D='Hello'
    def __init__(self)