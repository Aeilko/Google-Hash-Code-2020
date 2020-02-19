import sys


debug = False


name = "c_medium"
in_path = "./in/"
out_path = "./out/"


sys.stdin = open(in_path + name + ".in")
if not debug:
    sys.stdout = open(out_path + name + ".out", "w")

m, n = [int(x) for x in input().split()]
p = [(int(v), i) for i, v in enumerate(input().split())]

d = sum([v[0] for v in p]) - m

done = False
for i1, v1 in enumerate(p):
    for i2, v2 in enumerate(p):
        s = v1[0] + v2[0]
        if s == d:
            if i1 > i2:
                i1, i2 = i2, i1
            del p[i1]
            del p[i2 - 1]
            done = True
            break
    if done:
        break

if done:
    print(len(p))
    print(*[v[1] for v in p])
else:
    print("Failed")
