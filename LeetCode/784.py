class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        for s in S:
            _res = []
            for foo in res:
                if s.isdigit():
                    _res.append(foo+s)
                else:
                    _res += [foo+s.lower(), foo+s.upper()]
            res = _res
        return res




def letterCasePermutation(self, S):
    L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
    return [''.join(i) for i in itertools.product(*L)]