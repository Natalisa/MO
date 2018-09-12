ep = 10**(-9)
f = lambda x: x**2 - 5*x
a,b = -10,10
const = 1.61803

print (min([ f(i) for i in range(a, b, 1)]))

while abs(b-a) > ep:
    x1 = b - (b - a)/const
    x2 = a + (b - a)/const
    if f(x1) >= f(x2):
        a = x1
    else:
        b = x2
x = (a+b)/2
print (x, f(x))
