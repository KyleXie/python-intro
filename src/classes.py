
class Foo:
    pass


foo = Foo()
foo


Foo = type('Foo', (), {})
