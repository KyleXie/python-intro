import time


@staticmethod
def foo():
    pass


def foo():
    pass


foo = staticmethod(foo)


def calculate_time(func):
    def wrapper(*args, **kwargs):
        begin = time.time()

        func(*args, **kwargs)

        end = time.time()

        total_cost = end - begin

        print(f'Takes: {total_cost}')

    return wrapper


@calculate_time
def slow_task():
    time.sleep(2)
    print('A slow task')


slow_task()
