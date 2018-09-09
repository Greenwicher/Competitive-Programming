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


def MultiThread(fun, input):
    from multiprocessing.dummy import Pool as ThreadPool
    pool = ThreadPool()
    results = pool.starmap(fun, input)
    pool.close()
    pool.join()
    return list(filter(None.__ne__, results))


### specify the problem meta information ###
problemID = "A" # A, B, C, D...
problemSize = "local" # small, large, local
filename = "%s-%s-practice" % (problemID, problemSize)

### the algorithm that solve the cases ###
globalCaseID = 0
def solve(case):
    # record the start timing
    timing.append(time.time())

    timing.append(time.time())
    global globalCaseID
    globalCaseID += 1
    print("Case %d" % globalCaseID, ans, "\t\t Elapsed: %.2f seconds" % (timing[-1] - timing[-2]))
    return ans

### solve the test cases ###
# for the purpose of counting the total elapsed time
timing = [time.time()]

# open the input / output files
f_in = FileParser(filename+".in", "r")
f_out = FileParser(filename+".out", "w")


# parse the input, and store them into cases
cases = []
T = f_in.read_int()
for _ in range(T):
    # read the input data of each case
    # f_in.read_string(), f_in.read_words()
    # f_in.read_int(), f_in.read_integers()
    # f_in.read_float(), f_in.read_floats()

    cases.append()

# solve each test case
#anses = MultiThread(solve, zip(cases))
for caseID in range(1, T+1):
    # solve the case
    ans = solve(cases[caseID-1])
    #ans = anses[caseID-1]
    # print the answer to output file
    f_out.write("Case #%d: %d" % (caseID, ans))

# close the input / output files
f_in.close()
f_out.close()

# output the total elapsed time
timing.append(time.time())
total_time = timing[-1] - timing[0]
print("Total elapsed time: %.2f seconds / %.2f minutes" % (total_time, total_time/60))
