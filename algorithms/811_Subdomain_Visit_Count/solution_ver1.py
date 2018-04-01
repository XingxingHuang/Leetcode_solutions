class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        results = {}
        for cpdomain in cpdomains:
            counts, domain = cpdomain.split(' ')
            counts = int(counts)
            split = domain.split('.')
            for subdomain in ['.'.join(split[i:]) for i in range(len(split))]:
                if subdomain not in results:
                    results[subdomain] = counts
                else:
                    results[subdomain] += counts
        return [' '.join([str(v), k]) for k,v in results.items()]