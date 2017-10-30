def normalize(name):
    return name.capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

for x in L1:
    print('Hello,%s' % (x))


# -----------------------------------------------------------------------------------

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield (b)
        a, b = b, a + b
        n = n + 1
    return


# --------------------------------------------------------------------------------

from functools import reduce


def prod(xxx):
    def cheng(x, y):
        return x * y

    return reduce(cheng, xxx)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# ---------------------------------------------------------------------------------
def str2float(p):
    point = p.find('.')
    length = len(p)
    p = p[:point] + p[point + 1:]

    def str2int(x):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[x]

    def change(x, y):
        return x * 10 + y

    middle = reduce(change, map(str2int, p))

    print(middle / (length - point - 1))
    return middle / (length - point - 1)


print('str2float(\'123.456\') =', str2float('123.456'))

# ---------------------------------------------------------------------------------------------------------------------

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)


# ---------------------------------------------------------------------------------------------------------------------
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def count2():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


g1, g2, g3 = count2()
print(g1())
print(g2())
print(g3())
