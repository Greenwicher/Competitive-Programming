# Version 1, Dynamic Programming
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        ord1, ord2 = map(lambda s: [ord(x) for x in s], [s1, s2])
        # dp[i][j] represents the minimum cost given s1[:i+1] and s2[:j+1]
        dp = [[1e100] * n for _ in range(m)]
        flag, sumv = False, 0
        for i in range(m):
            if not(flag) and s1[i] == s2[0]:
                flag = True
            sumv += ord1[i]
            dp[i][0] = sumv + ord2[0] - 2 * ord2[0] * flag
        flag, sumv = False, 0
        for j in range(n):
            if not(flag) and s2[j] == s1[0]:
                flag = True
            sumv += ord2[j]
            dp[0][j] = sumv + ord1[0] - 2 * ord1[0] * flag
        for i in range(1, m):
            for j in range(1, n):
                subv = [dp[i][j]]
                # keep both s1[i] and s2[j] or delete both of them
                if s1[i] == s2[j]:
                    subv.append(dp[i-1][j-1])
                else:
                    subv.append(dp[i-1][j-1] + ord1[i] + ord2[j])
                # delete s1[i], delete s2[j]
                subv += [dp[i-1][j] + ord1[i], dp[i][j-1] + ord2[j]]
                dp[i][j] = min(subv)
        return dp[m-1][n-1]

s = Solution()
print(s.minimumDeleteSum("sea", "eat"))
print(s.minimumDeleteSum("delete", "leet"))
print(s.minimumDeleteSum("gqirsclhrchxsqgmpfdeploxfixowfqqubuvsupkejabcrfqgcnsauunllsfskclenkxmdyraerhfmmiwryeyqoldgxctuvsjarjvfelsglvlbnozmejncnlaqpxmbrgwayfzczvatel","kgievqcxvrgeyklbcidngseersbiubgdwzlraagerenyfavkdcriinaugodaoacfiasmhhoxxsnqcyfriknrjfwyfglplvodefdlbmykfgpdpzjndlrskzctfkfkwcjbibuglrjvdyfhnsgwuunpzoakyejkxczznfljimkkanlsyuhvwjitrdvktrvufgyllgjpjixotsgwjkzbdqhvzyappucwvberchznrzdqjwpvyckwbfnlulscxynfbqqkhgxxkdzawjtlncqqswfwwbvywdchnxtblboobjzkurpjutdbwaxlxkxuiaxiddntniuuvghprslmpctnokubadbbxhuezbesvgvptqbnfjpmxopjdrajectbpkszvzzjivzhlesfnzaetgvxcnrhuglvoncgsyoyucjnuedgcfdrnkhxfyhujxzvxieeevwqn"))