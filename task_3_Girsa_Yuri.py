def type_logger(callback):
    def wrapper(*args):
        for el in args:
            print(f'{callback.__name__}({el}: {type(el)})')
        a = callback(*args)
        return a
    return wrapper


@type_logger
def calc_cube(*args):
    for eli in args:
        return eli ** 3


calc_cube(5, 10, 20)
