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
problemID = "B" # A, B, C, D...
problemSize = "large" # small, large, local
filename = "%s-%s-practice" % (problemID, problemSize)
#filename = "B-large"

### the algorithm that solve the cases ###
import math
def solve(N, M):
    # record the start timing
    timing.append(time.time())
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for n in range(1, N+1):
        dp[n][0] = math.factorial(n)
        for m in range(1, min(n, M+1)):
            if n-1 > m: dp[n][m] += dp[n-1][m] * max(N - n + 1, 0)
            if n > m-1: dp[n][m] += dp[n][m-1] * max(M - m + 1, 0)
    ans = dp[N][M] / math.factorial(N+M)
#    prob = [[0.0 for _ in range(2002)] for _ in range(2002)]
#    for n in range(1, 2001):
#        prob[n][0] = 1.0
#        for m in range(1, n):
#            incProb = n / (n + m)
#            prob[n][m] = prob[n-1][m] * incProb + prob[n][m-1] * (1.0 - incProb)
    timing.append(time.time())
    return ans

### solve the test cases ###
# for the purpose of counting the total elapsed time
timing = [time.time()]

# open the input / output files
f_in = FileParser(filename+".in", "r")
f_out = FileParser(filename+".out", "w")


# solve each test case
T = f_in.read_int()
#prob = solve()
for caseID in range(1, T+1):
    # read the input data of each case
    # f_in.read_string(), f_in.read_words()
    # f_in.read_int(), f_in.read_integers()
    # f_in.read_float(), f_in.read_floats()
    N, M = f_in.read_integers()

    # solve the case
    #ans = prob[N][M]
    ans = solve(N, M)

    # print the answer to output file
    context = "Case #%d: %.10f" % (caseID, ans)
    print(context, "\t\t Elapsed: %.2f seconds" % (timing[-1] - timing[-2]))
    f_out.write(context)

# close the input / output files
f_in.close()
f_out.close()

# output the total elapsed time
timing.append(time.time())
total_time = timing[-1] - timing[0]
print("Total elapsed time: %.2f seconds / %.2f minutes" % ((total_time, total_time/60)))
