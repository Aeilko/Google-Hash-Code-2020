import sys


debug = False


name = "d_tough_choices"
in_path = "./in/"
out_path = "./out/"


sys.stdin = open(in_path + name + ".in")
if not debug:
    sys.stdout = open(out_path + name + ".out", "w")

b, l, d = [int(x) for x in input().split()]
books = [int(x) for x in input().split()]
libraries = [None]*l
for i in range(0, l):
    tb, r, bpd = [int(x) for x in input().split()]
    bs = {int(x) for x in input().split()}
    lib = {
        "id": i,
        "totalBooks": tb,
        "register": r,
        "books_per_day": bpd,
        "books": bs,
    }
    libraries[i] = lib


def tuple_val(e):
    return e[1]


# Calculate the max possible score with these books
def max_score(possible_books, book_scores, books_per_day, days_left):
    if books_per_day*days_left > len(possible_books):
        s = 0
        for book in possible_books:
            s += book_scores[book]
        return s
    else:
        sl = []
        for book in possible_books:
            sl.append(book_scores[book])
        sl = sorted(sl, reverse=True)
        return sum(sl[:books_per_day*days_left])


# Calculate the amount of score which is lost in days_lost days
def score_lost(possible_books, book_scores, books_per_day, days_left, days_lost):
    if books_per_day*(days_left-days_lost) >= len(possible_books):
        return 0
    else:
        sl = []
        for book in possible_books:
            sl.append(book_scores[book])
        sl = sorted(sl, reverse=True)
        filtered = sl[books_per_day*(days_left-days_lost):books_per_day*days_left]
        return sum(filtered)


# Returns the ids of the most valuable books
def get_book_ids(possible_books, book_scores, books_per_day, days_left):
    if books_per_day*days_left > len(possible_books):
        return possible_books
    else:
        sl = []
        for book in possible_books:
            sl.append((book, book_scores[book]))
        sl = sorted(sl, reverse=True, key=tuple_val)
        filtered = sl[:books_per_day*days_left]
        return {x[0] for x in filtered}


# Determines the next best library to register
def next_library(libraries, books_score, scanned_books, days_left):
    # Calculate the maximum score
    ms = 0
    ms_library = None
    for lib in libraries:
        s = max_score(lib['books'], books_score, lib['books_per_day'], days_left)
        if ms_library is None or s > ms or (s == ms and lib['register'] < ms_library['register']):
            ms = s
            ms_library = lib

    # Check which library loses the most score in this register time
    sl = 0
    sl_library = None
    for lib in libraries:
        s = score_lost(lib['books'], books_score, lib['books_per_day'], days_left-lib['register'], ms_library['register'])
        if sl_library is None or s > sl or (s == sl and lib['register'] < sl_library['register']):
            sl = s
            sl_library = lib

    # So we add the library which loses the most points in the timespan of the most valuable library register time
    out = {
        'id': sl_library['id'],
        'books': get_book_ids(sl_library['books'], books_score, sl_library['books_per_day'], days_left)
    }

    return out


def calc_score(used_books, books_score):
    s = 0
    for book in used_books:
        s += books_score[book]
    return s


output = []
scanned_books = set()
d_left = d
libs_left = list(libraries)
while len(libs_left) > 0:
    lib = next_library(libs_left, books, scanned_books, d_left)

    # Register this library
    output.append(lib)
    libs_left.remove(libraries[lib['id']])
    d_left -= libraries[lib['id']]['register']
    scanned_books = scanned_books | lib['books']

    # Update other libraries
    remove_items = []
    for libb in libs_left:
        if libb['register'] >= d_left:
            remove_items.append(libb)
        else:
            # Remove te books we just scanned
            libb['books'] = libb['books']-lib['books']

            if len(libb['books']) < 1:
                remove_items.append(libb)

    for ri in remove_items:
        libs_left.remove(ri)

    if debug:
        print("Adding library\t" + str(lib['id']))
        print("Days left\t\t" + str(d_left))


print(len(output))
for o in output:
    print(str(o['id']) + " " + str(len(o['books'])))
    print(*o['books'])

sys.stdout = sys.__stdout__
print("\nScore\t" + str(calc_score(scanned_books, books)))
