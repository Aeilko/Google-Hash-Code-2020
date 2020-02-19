from sortedcontainers import SortedList
import sys


debug = False


name = "e_also_big"
in_path = "./in/"
out_path = "./out/"


sys.stdin = open(in_path + name + ".in")
if not debug:
    sys.stdout = open(out_path + name + ".out", "w")


def test(s_in, W):
    s_out = []
    s_sum = 0
    v = len(s_in) - 1
    for i in range(len(s_in)):
        if s_sum + s_in[v - i] < W:
            s_sum += s_in[v - i]
            s_out.append(v - i)
    return s_out


m, n = [int(i) for i in input().split()]
s_in = [int(i) for i in input().split()]
s = SortedList(s_in)
r = test(s_in, m)
print(len(r))
r.sort()
print(" ".join([str(x) for x in r]))

