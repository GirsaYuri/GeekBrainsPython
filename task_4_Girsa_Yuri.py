def val_checker(callback):
    def _val_checker(func):
        def wrapper(args):
            if not callback(args):
                raise ValueError
            else:
                a = func(args)
                return a
        return wrapper
    return _val_checker



@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

z = calc_cube(20)
print(z)

