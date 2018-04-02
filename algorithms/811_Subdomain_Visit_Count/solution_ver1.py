# https://leetcode.com/problems/subdomain-visit-count/


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        use hashmap, one pass
        """
        from collections import Counter
        results = Counter()
        for cpdomain in cpdomains:
            counts, domain = cpdomain.split(' ')
            counts = int(counts)
            split = domain.split('.')
            for subdomain in ['.'.join(split[i:]) for i in range(len(split))]:
                results[subdomain] += counts
        return [' '.join([str(v), k]) for k,v in results.items()]