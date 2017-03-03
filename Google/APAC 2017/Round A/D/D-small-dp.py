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
problemSize = "small" # small, large, local
filename = "%s-%s-practice" % (problemID, problemSize)

### the algorithm that solve the cases ###
def solve(M, N, K, L, A, C):
    # record the start timing
    t = time.time()
    # calculate the cumulative cost matrix from current level
    for i in range(N):
        for level in range(L[i], K[i]-1):
            C[i][level] += C[i][level - 1]
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(N):
        c = [0] + C[i][L[i] - 1:]
        for v in range(M + 1):
            for k in range(len(c)):
                if v - c[k] >= 0:
                    dp[i+1][v] = max(dp[i+1][v], dp[i][v-c[k]] + A[i][k+L[i]-1])
    print("Case: (%d, %d), Elapsed %.2f seconds" % (M, N, time.time() - t))
    return dp[N][M]

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
        Cappend(f_in.read_integers())

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
