class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        def convert(word, i):
            if word[0].lower() in 'aeiou':
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word += 'a' * i
            return word
        S = S.split(' ')
        return ' '.join(list(map(convert, S, range(1, len(S)+1))))

s = Solution()
s.toGoatLatin("The quick brown fox jumped over the lazy dog")