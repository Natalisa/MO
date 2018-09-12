ep = 10**(-9)
f = lambda x: x**2 - 5*x
a,b = -10,10
const = 1.61803

#print (min([ f(i) for i in range(a, b, 1)]))

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

f2 = lambda x: (x[0] - 0.7)**2 + (x[1] - x[0]**2)**2

d =[a,b]
def GoldenSection2(fun,d, ep, var, am):
    l,r=d
    print(var)
    if len(var) == am:
         return var
    x1 = r - (r - l)/const
    x2 = l + (r - l)/const
    y1 = fun(GoldenSection2(fun,d,ep,var+(x1,),am))
    y2 = fun(GoldenSection2(fun,d,ep,var+(x2,),am))
    while abs(r-l) > ep:
        if y1 >= y2:
            l, x1, y1 = x1, x2, y2
            x2 = r - (r - l)/const
            y2 = fun(GoldenSection2(fun,d,ep,var+(x2,),am))
        else:
            r, x2, y2 = x2, x1, y1
            x1 = l + (r - l)/const
            y1 = fun(GoldenSection2(fun,d,ep,var+(x1,),am))
    return var+((l+r)/2,)
var = ()
min = GoldenSection2(f2,d, ep,var,2)
print(min,f2(min))
