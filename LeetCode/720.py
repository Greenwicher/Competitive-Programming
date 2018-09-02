class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        ix = {word:1 for word in words}
        words = sorted(words, key=lambda x: (-len(x), x))
        for word in words:
            flag = True
            for i in range(len(word)):
                if not(word[:i+1] in ix):
                    flag = False
                    break
            if flag:
                return word
        return ""