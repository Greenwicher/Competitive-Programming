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
def solve(N, Q, array, LR):
    # record the start timing
    timing.append(time.time())
    new_array = []
    length = len(array)
    array = [0] + array
    for i in range(length):
        array[i+1] += array[i]
    for size in range(1, length + 1):
        for start in range(length - size + 1):
            new_array.append(array[start + size] - array[start])
    new_array = sorted(new_array)
    new_array = [0] + new_array
    for i in range(len(new_array)-1):
        new_array[i+1] += new_array[i]
    ans = []
    for i in range(Q):
        ans.append(new_array[LR[i][1]] - new_array[LR[i][0]-1])
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
for caseID in range(1, T+1):
    # read the input data of each case
    # f_in.read_string(), f_in.read_words()
    # f_in.read_int(), f_in.read_integers()
    # f_in.read_float(), f_in.read_floats()
    N, Q = f_in.read_integers()
    array = f_in.read_integers()
    LR = []
    for _ in range(Q):
        LR.append(f_in.read_integers())

    # solve the case
    ans = solve(N, Q, array, LR)

    # print the answer to output file
    context = "Case #%d:" % (caseID)
    print(context, ans, "\t\t Elapsed: %.2f seconds" % (timing[-1] - timing[-2]))
    f_out.write("Case #%d:" % caseID)
    for i in range(Q):
        f_out.write(str(ans[i]))

# close the input / output files
f_in.close()
f_out.close()

# output the total elapsed time
timing.append(time.time())
total_time = timing[-1] - timing[0]
print("Total elapsed time: %.2f seconds / %.2f minutes" % ((total_time, total_time/60)))
