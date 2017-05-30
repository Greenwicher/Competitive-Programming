# Version 1, List[int] -> List[char] -> str -> int -> str -> List[char] -> List[int]
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(map(int, str(int(''.join(map(str, digits)))+1)))

# Version 2, Big Number Addition, O(n) time complexity, O(1) space complexity
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d = 1
        for i in range(n)[::-1]:
            r = (digits[i] + d) % 10
            d = (digits[i] + d) // 10
            digits[i] = r
        if d > 0:
            digits = [d] + digits
        return digits