import sys


debug = False


name = "d_quite_big"
in_path = "./in/"
out_path = "./out/"


sys.stdin = open(in_path + name + ".in")
if not debug:
    sys.stdout = open(out_path + name + ".out", "w")

m, n = [int(x) for x in input().split()]
p = [int(v) for v in input().split()]


def knapsack(W, wt, n):
    K = [[(0, []) for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = (0, [])
            elif wt[i - 1] <= w:
                m1, s1 = K[i - 1][w - wt[i - 1]]
                m2, s2 = K[i - 1][w]

                if (m1 + wt[i - 1] > m2):
                    K[i][w] = (m1 + wt[i - 1], s1 + [i - 1])
                else:
                    K[i][w] = (m2, s2)
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


# Running the algorithm
t = len(p) // 10 - 10

p_s = p[:t]
p_l = p[t:]

result = knapsack(m - sum(p_l), p_s, len(p_s))
output_indices = (result[1] + [i + t for i, _ in enumerate(p_l)])
print(len(output_indices))
print(*output_indices)
