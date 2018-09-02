class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True
        else:
            last = bits[-2:]
            bits = bits[:-2]
            i = 0
            while i < len(bits):
                if bits[i] == 0:
                    i += 1
                else:
                    i += 2
            if i == len(bits) and last != [0, 0]:
                return False
            else:
                return True
