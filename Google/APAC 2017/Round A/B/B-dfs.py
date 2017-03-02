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

### the algorithm that solve the cases ###
def sea(connected, R, C):
    for foo in connected:
        x, y = foo
        if x == 0 or x == R - 1 or y == 0 or y == C - 1:
            return True
    return False

import sys
sys.setrecursionlimit(5000)
def dfs(i, j, H, R, C, h):
    visited[i][j] = True
    connected.append((i,j))
    for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        _i, _j = i + x, j + y
        if not(_i == -1 or _i == R or _j == -1 or _j == C):
            if not(visited[_i][_j]):
                if H[_i][_j] <= h:
                    dfs(_i, _j, H, R, C, h)
                else:
                    global bh
                    bh = min(bh, H[_i][_j])
    return

def fill(H, R, C):
    for i in range(1, R-1):
        for j in range(1, C-1):
            global visited
            visited = [[False] * C for _ in range(R)]
            if not(visited[i][j]):
                # find all the connected cell that have height equal or less than H[i][j]
                global connected
                connected = []
                global bh
                bh = 1e100
                dfs(i, j, H, R, C, H[i][j])
                # check whether any connected cells connect the sea
                flag = sea(connected, R, C)
                # update H if the connected cells can collect water
                h = H[i][j]
                if not(flag):
                    for foo in connected:
                        x, y = foo
                        H[x][y] = bh
                        visited[x][y] = False
            else:
                continue
    return H

def solve(H, R, C):
    # record the start timing
    timing.append(time.time())
    import copy
    W = copy.deepcopy(H)
    M = fill(copy.deepcopy(W), R, C)
    while (W != M):
        W = copy.deepcopy(M)
        M = fill(copy.deepcopy(W), R, C)
    ans = sum([W[i][j] - H[i][j] for i in range(R) for j in range(C)])
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
    R, C = f_in.read_integers()
    H = []
    for _ in range(R):
        H.append(f_in.read_integers())

    # solve the case
    ans = solve(H, R, C)

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
