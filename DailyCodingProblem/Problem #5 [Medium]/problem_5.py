def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair) -> int:
    def _(a, b): return a
    return pair(_)


def cdr(pair) -> int:
    def _(a, b): return b
    return pair(_)