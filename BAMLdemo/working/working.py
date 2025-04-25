class A(object):

    def a(self):
        print("A.a")

    def b(self):
        self.a()
        print("A.b")


class B(A):

    def a(self):
        print("B.a")


def run():
    a = A()
    a.b()
    b = B()
    b.b()


if __name__ == "__main__":
    run()
