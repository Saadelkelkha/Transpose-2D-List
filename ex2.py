t = []
r = []

for i in range(0, 4):
    l = []
    for j in range(0, 6):
        n = int(input("Type number :"))
        l.append(n)
    t.append(l)

for j in range(0, 6):
    o = []
    for i in range(0, 4):
        b = t[i][j]
        o.append(b)
    r.append(o)

print(t)
print(r)
