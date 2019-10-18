
def foo():
    pass


def add(x, y):
    return x + y


add(1, 2)


# Positional-or-Keyword Arguments
# Default Argument Values
def foo(name, age=None):
    print(name)
    if age is not None:
        print(age)


foo('Jimmy')
foo('Jimmy', 19)


def foo(name, *args, age=0, **kwargs):
    print(name, args, age, kwargs)


foo('Jimmy', 25, 'args1', 'args2', kw1='kw1', kw2='kw2')

# Unpacking Arguments
positional_args = ['args1', 'args2']
keyword_args = dict(kw1='kw1', kw2='kw2')
foo('Jimmy', 25, *positional_args, **keyword_args)


# Lambda Expressions
a_list = [1, 8, 19, 2, 5, 3]
map(lambda x: x + 1, a_list)
filter(lambda x: x > 5, a_list)
