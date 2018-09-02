class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        def process(foo):
            for punctuaion in "!?',;.":
                foo = foo.replace(punctuaion, '')
            return foo.lower()
        words = [process(foo) for foo in paragraph.split(' ')]
        from collections import Counter
        cnt_words = Counter(words)
        res, cnt = '', 0
        for foo in cnt_words:
            if not(foo in banned):
                if cnt_words[foo] > cnt:
                    res = foo
                    cnt = cnt_words[foo]
        return res