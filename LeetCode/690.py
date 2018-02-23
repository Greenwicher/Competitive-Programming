"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        res = 0
        d = {}
        for foo in employees:
            d[foo.id] = [foo.importance, foo.subordinates, False]
        queue = [d[id]]
        while any(queue):
            _queue = []
            for foo in queue:
                res += foo[0]
                foo[2] = True
                for sub in foo[1]:
                    if not d[sub][2]:
                        _queue.append(d[sub])
            queue = _queue
        return res