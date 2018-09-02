class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = ''
        flag = True
        l = min([len(foo) for foo in strs])
        if l == 0:
            return ''
        for i in range(l):
            if len(set([foo[i] for foo in strs])) != 1:
                flag = False
                break
        if flag:
            return strs[0][:i+1]
        else:
            return strs[0][:i]