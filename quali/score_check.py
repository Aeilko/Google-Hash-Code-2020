import sys


name = "d_tough_choices"
in_path = "./in/"
out_path = "./out/"


def calc_score(used_books, books_score):
    s = 0
    for book in used_books:
        s += books_score[book]
    return s


sys.stdin = open(in_path + name + ".in")
b, l, d = [int(x) for x in input().split()]
book_scores = [int(x) for x in input().split()]
for i in range(0, l):
    tmp = [int(x) for x in input().split()]
    tmp2 = {int(x) for x in input().split()}

sys.stdin = open(out_path + name + ".out")
l = [int(x) for x in input().split()][0]
books = set()
for i in range(0, l):
    tmp = [int(x) for x in input().split()]
    books = books | {int(x) for x in input().split()}

s = calc_score(books, book_scores)
sys.stdout = sys.__stdout__
print("\nScore\t" + str(s))



