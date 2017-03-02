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

def MultiThread(fun,input):
    from multiprocessing.dummy import Pool as ThreadPool
    pool = ThreadPool()
    results = pool.starmap(fun,input)
    pool.close()
    pool.join()
    return list(filter(None.__ne__, results))


### specify the problem meta information ###
problemID = "D" # A, B, C, D...
problemSize = "small" # small, large, local
filename = "%s-%s-practice" % (problemID, problemSize)

### the algorithm that solve the cases ###
def cost(level, C):
    return sum([C[i][level[i]-1] for i in range(len(level))])

def attack(level, A):
    return sum([A[i][level[i]] for i in range(len(level))])

def evaluate(level):
    c = cost(level, C)
    a = attack(level, A)
    print(c,a)
    return [c,a]

#def solve(input):
#    M, N, K, L, A, C = input
def solve(M, N, K, L, A, C):
    # record the start timing
    t = time.time()
    timing.append(time.time())
    import itertools
    level = [[j for j in range(L[i], K[i]+1)] for i in range(N)]
    combinations = itertools.product(*level)
    maxattack = -1
    for i in range(N):
        for j in range(1, len(C[i])):
            C[i][j] += C[i][j-1]
    cost0 = cost(L, C)
#    fc, fa = cost, attack
#    for foo in combinations:
#        cost1 = fc(foo, C)
#        attack1 = fa(foo, A)
#        if cost1 - cost0 <= M and attack1 > maxattack:
#            maxattack = attack1
    ac = MultiThread(evaluate, combinations)
    for foo in ac:
        if foo[0] - cost0 <= M and foo[1] > maxattack: maxattack = foo[1]
    timing.append(time.time())
    print("Case: (%d, %d), Elapsed %.2f seconds" % (M, N, time.time() - t))
    return maxattack

### solve the test cases ###
# for the purpose of counting the total elapsed time
timing = [time.time()]

# open the input / output files
f_in = FileParser(filename+".in", "r")
f_out = FileParser(filename+".out", "w")


# solve each test case
T = f_in.read_int()
case = []
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
        Aappend([0]+f_in.read_integers())
        Cappend([0]+f_in.read_integers())
    case.append([M, N, K, L, A, C])

results = MultiThread(solve, case)
#results = list(map(solve, case))
for caseID in range(1, T+1):
    ans = results[caseID-1]
    # print the answer to output file
    context = "Case #%d: %d" % (caseID, ans)
    print(context, "\t\t Elapsed: %.2f seconds" % (timing[-1] - timing[-2]))
    f_out.write(context)

# close the input / output files
f_in.close()
f_out.close()

# output the total elapsed time
timing.append(time.time())
total_time = timing[-1] - timing[0]
print("Total elapsed time: %.2f seconds / %.2f minutes" % ((total_time, total_time/60)))
