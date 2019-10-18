
class Foo:

    def foo(self):
        print(self)

    @staticmethod
    def unbound_method():
        print('unbound method')


f = Foo()
f.foo()
f.unbound_method()

Foo.foo(f)
