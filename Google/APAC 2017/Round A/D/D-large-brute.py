import sys
import time

### I/O wrapper ###
class FileParser:
    """Read numbers/strings from file (or stdin by default), one line by one.
    """

    def __init__(self, filepath=None, type=None):
        if filepath is None:
            self.fd = sys.stdin
        else:
            self.fd = open(filepath, type)

    def read_string(self):
        return self.fd.readline().rstrip()

    def read_words(self):
        return [x for x in self.read_string().split()]

    def read_int(self):
        return int(self.fd.readline())

    def read_integers(self):
        return [int(x) for x in self.fd.readline().rstrip().split()]

    def read_float(self):
        return float(self.fd.readline())

    def read_floats(self):
        return [float(x) for x in self.fd.readline().rstrip().split()]

    def write(self, context):
        if self.fd is not sys.stdin:
            self.fd.write(context+"\n")
        else:
            print(context)
        return

    def close(self):
        if self.fd is not sys.stdin:
            self.fd.close()
        self.fd = None

### specify the problem meta information ###
problemID = "D" # A, B, C, D...
problemSize = "large" # small, large, local
filename = "%s-%s-practice" % (problemID, problemSize)

### the algorithm that solve the cases ###
def solve(M, N, K, L, A, C):
    start = time.time()
    import itertools
    combinations = itertools.combinations(range(N), 8)
    ans = 0
    for card in combinations:
        ans = max(ans, sub_solve(*construct(card, M, N, K, L, A, C)))
    print("ans = %d, elapsed %.2f seconds" % (ans, time.time() - start))
    return ans

def sub_solve(card, M, N, K, L, A, C):
    ac1 = brute(card[:4], M, N, K[:4], L[:4], A[:4], C[:4])
    ac2 = brute(card[4:], M, N, K[4:], L[4:], A[4:], C[4:])
    ans = 0
    for foo in ac1:
        ans = max(ans, foo[0] + bisection(ac2, M - foo[1]))
    return ans

def bisection(ac, c):
    if not(ac): return 0
    l, r = 0, len(ac) - 1
    assert r >= l, "no feasible solutions for bisection"
    while l != r:
        m = (l + r) // 2
        if ac[m][1] <= c:
            r = m
        else:
            l = m + 1
    if ac[l][1] <= c:
        return ac[l][0]
    else:
        return 0

def brute(card, M, N, K, L, A, C):
    import itertools
    level = [list(range(L[i] - 1, K[i])) for i in range(4)]
    levels = itertools.product(*level)
    ac = []
    c0 = cost([l - 1 for l in L], C)
    for l in levels:
        a, c = attack(l, A), cost(l, C)
        ac.append([a, c-c0])
    _ac = []
    ac = sorted(ac, reverse=True, key=lambda x: x[1])
    size = len(ac)
    for i in range(size):
        if ac[i][1] > M:
            continue
        flag = True
        for j in range(i+1, size):
            if ac[i][0] <= ac[j][0]:
                flag = False
                break
        if flag:
            _ac.append(ac[i])
    return _ac


def attack(level, A):
    return sum([A[i][level[i]] for i in range(len(A))])


def cost(level, C):
    return sum([C[i][level[i]] for i in range(len(C))])


def construct(foo, M, N, K, L, A, C):
    _K, _L, _A, _C = [[] for _ in range(4)]
    for card in foo:
        _K.append(K[card])
        _L.append(L[card])
        _A.append(A[card])
        _C.append(C[card])
    return foo, M, 8, _K, _L, _A, _C


### solve the test cases ###
# for the purpose of counting the total elapsed time
timing = [time.time()]

# open the input / output files
f_in = FileParser(filename+".in", "r")
f_out = FileParser(filename+".out", "w")


# solve each test case
T = f_in.read_int()
for caseID in range(1, T+1):
    # read the input data of each case
    # f_in.read_string(), f_in.read_words()
    # f_in.read_int(), f_in.read_integers()
    # f_in.read_float(), f_in.read_floats()
    M, N = f_in.read_integers()
    K, L = [[0 for _ in range(N)] for _ in range(2)]
    A, C = [], []
    Aappend, Cappend = A.append, C.append
    for i in range(N):
        K[i], L[i] = f_in.read_integers()
        Aappend(f_in.read_integers())
        Cappend([0] + f_in.read_integers())

    for i in range(N):
        for j in range(1, K[i]):
            C[i][j] += C[i][j-1]
    ans = solve(M, N, K, L, A, C)
    # print the answer to output file
    context = "Case #%d: %d" % (caseID, ans)
    f_out.write(context)

# close the input / output files
f_in.close()
f_out.close()

# output the total elapsed time
timing.append(time.time())
total_time = timing[-1] - timing[0]
print("Total elapsed time: %.2f seconds / %.2f minutes" % ((total_time, total_time/60)))
