class A:
    def __init__(self, a):
        self.a = a

    def print_a(self):
        print(self.a)


class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def print_b(self):
        print(self.b)


b = B(10, 2)
b.print_a()
b.print_b()
