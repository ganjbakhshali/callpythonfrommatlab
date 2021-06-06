def mul(a,b,common=1):
    from pgmpy.factors.discrete import DiscreteFactor
    import numpy as np
    import re
    import math

    a=np.asarray(a)
    b=np.asarray(b)

    # a1 = [row[0] for row in a]
    # b1 = [row[1] for row in a]
    # xa=['x1', 'x2']
    # xb=['x2', 'x3']

    xa=[]
    xb=[]
    # numrows = len(input)    # 3 rows in your example
    # numcols = len(input[0]) # 2 columns in your example
    size_a=int(math.log2(len(a)))
    size_b=int(math.log2(len(b)))

    for i in range(size_a):
        xa.append('x'+str(i+1))

    s=xa[-common]
    p=re.findall('(\d+)',s)
    starter=int(p[0])
    for i in range(size_b):
        xb.append('x'+str(i+starter))

    print(xa)
    print(xb)

    phi1 = DiscreteFactor(xa, [size_a, size_a], a)
    phi2 = DiscreteFactor(xb, [size_b, size_b], b)
    
    phi1.product(phi2, inplace=True)
    vars=phi1.variables
    # print(vars)
    ans=phi1.values
    ans=np.array(ans)
    ans=ans.reshape(-1)
    # print(ans)
    return ans, vars