class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = [0] * 2
        for m in moves:
            if m == 'R':
                x, y = x+1, y
            elif m == 'L':
                x, y = x-1, y
            elif m == 'U':
                x, y = x, y+1
            else:
                x, y = x, y-1
        if (x, y) == (0, 0):
            return True
        else:
            return False