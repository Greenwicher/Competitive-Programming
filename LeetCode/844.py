class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def run(str):
            i = 0
            while i < len(str):
                if str[i] == '#':
                    if i > 0:
                        str = str[:i-1] + str[i+1:]
                        i -= 1
                    else:
                        str = str[i+1:]
                        i = 0
                else:
                    i += 1
            return str
        return run(S) == run(T)

s = Solution()
print(s.backspaceCompare('ab#c', 'ad#c'), True)
print(s.backspaceCompare('ab##', 'c#d#'), True)
print(s.backspaceCompare('a##c', '#a#c'), True)
print(s.backspaceCompare('a#c', 'b'), False)