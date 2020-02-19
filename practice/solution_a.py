import sys


debug = False


name = "a_example"
in_path = "./in/"
out_path = "./out/"


sys.stdin = open(in_path + name + ".in")
if not debug:
    sys.stdout = open(out_path + name + ".out", "w")

m, n = [int(x) for x in input().split()]
p = [int(v) for v in input().split()]

def knapSack(W, wt, n, s=[]):
    if n == 0 or W == 0:
        return (0, s)
    if (wt[n-1] > W):
        return knapSack(W, wt, n-1, s)
    else:
        m1, s1 = knapSack(W-wt[n-1], wt, n-1, s + [wt[n-1]]) # Need to append s?
        m2, s2 = knapSack(W, wt, n-1, s)

        if wt[n-1] + m1 > m2:
            return (wt[n-1] + m1, s1)
        else:
            return (m2, s2)

# Running the algorithm
result = knapSack(m, p, len(p))[1]

i = 0
output = []
for x in sorted(result):
    output.append(p.index(x) + i)
    p.remove(x)
    i += 1

print(len(result))
print(*output)
