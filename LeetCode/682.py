class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        valid_points = []
        res = 0
        for foo in ops:
            if foo == "+":
                point = valid_points[-1] + valid_points[-2]
            elif foo == "D":
                point = 2 * valid_points[-1]
            elif foo == "C":
                point = -valid_points[-1]
            else:
                point = int(foo)
            if foo != "C":
                valid_points.append(point)
            else:
                valid_points.pop()
            res += point
        return res