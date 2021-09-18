class A:
    def __init__(self):
        print('in A init')

class B:
    def __init__(self):
        print('in B init')

class C(A,B):
    def __init__(self):
        print('in C init')
        super().__init__()


ob = C()