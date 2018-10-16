ep = 10**(-9)
f = lambda x: x**2 - 5*x
a,b = -10,10
const = 1.61803

def GoldenSection(fun, l, r, ep):
    while abs(r-l) > ep:
        x1 = r - (r - l)/const
        x2 = l + (r - l)/const
        if fun(x1) >= fun(x2):
            l = x1
        else:
            r = x2
    return (l+r)/2

min = GoldenSection(f,a,b, ep)
print ("x = ",min, "\ny = ",f(min))
print()


import math

f2 = lambda x: (x[0] - 0.7)**2 + (x[1] - x[0]**2)**2

class GoldenSection:
    def __init__(self):
        self.result = 0.0
        self.steps = 0

    def GoldenSection2(self, a, b, e, fun, vars, index):
        while abs(b - a) > e:
            x1 = b - (b - a) / const
            vars[index] = x1
            A = fun(vars)
            x2 = a + (b - a) / const
            vars[index] = x2
            B = fun(vars)
            if A >= B:
                a = x1
            else:
                b = x2
            self.steps += 1
        self.result = (a + b) / 2
        return self.result

gs = GoldenSection()
vars = [0, 0]
while True:
    A = f2(vars)
    for pos, elem in enumerate(vars):
        vars[pos] = gs.GoldenSection2(a, b, ep, f2, vars, pos)
    B = f2(vars)
    if abs(A - B) <= ep:
        break
print("x =",str(vars),"y =", f2(vars))
#print(gs.steps)
