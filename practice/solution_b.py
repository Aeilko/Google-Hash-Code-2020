import sys


debug = False


name = "b_small"
in_path = "./in/"
out_path = "./out/"


sys.stdin = open(in_path + name + ".in")
if not debug:
    sys.stdout = open(out_path + name + ".out", "w")

m, n = [int(x) for x in input().split()]
p = [(int(v), i) for i, v in enumerate(input().split())]

a = []
done = False
for i1, v1 in enumerate(p):
    for i2, v2 in enumerate(p):
        for i3, v3 in enumerate(p):
            s = v1[0] + v2[0] + v3[0]
            if s == m:
                a = sorted([i1, i2, i3])
                done = True
                break
    if done:
        break

if done:
    print(len(a))
    print(*a)
else:
    print("Failed")
