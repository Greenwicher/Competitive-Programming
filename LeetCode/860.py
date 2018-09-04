class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        cnt = {5:0, 10:0, 20:0}
        for foo in bills:
            if foo == 5:
                cnt[5] += 1
            elif foo == 10:
                if cnt[5] > 0:
                    cnt[5] -= 1
                    cnt[10] += 1
                else:
                    return False
            elif foo == 20:
                if cnt[10] > 0 and cnt[5] > 0:
                    cnt[10] -= 1
                    cnt[5] -= 1
                    cnt[20] += 1
                elif cnt[5] > 2:
                    cnt[5] -= 3
                    cnt[20] += 1
                else:
                    return False
        return True