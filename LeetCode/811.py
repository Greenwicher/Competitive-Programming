class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        res = defaultdict(int)
        for cpdomain in cpdomains:
            cnt, domain = cpdomain.split(' ')
            domains = domain.split('.')
            for i in range(len(domains)):
                res['.'.join(domains[i:])] += int(cnt)
        return ['%d %s' % (v, k) for k, v in res.items()]