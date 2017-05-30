class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.data = defaultdict(int)

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.data[val]:
            return False
        else:
            self.data[val] = 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.data[val]:
            del self.data[val]
            return True
        else:
            del self.data[val]
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return random.choice(self.data.keys())


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.remove(44))
print(obj.getRandom())