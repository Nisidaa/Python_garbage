x1 = 0
x2=0
arrx1 = []
arrx2 = []


def iteration(x1, x2):
    tempx1 = x1 + 0.1*(-3*x1+x2-1)
    tempx2 = x2 + 0.1*(x1+x2)
    return tempx1, tempx2

for i in range(0, 6):
    x1,x2 = iteration(x1, x2)
    print(str.format("t = {}: x1 = {}, x2 = {}",i/10, float('{:.3f}'.format(x1)), float('{:.3f}'.format(x2))))

