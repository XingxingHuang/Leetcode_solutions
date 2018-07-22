class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = dict()
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in hashmap:
                hashmap[ss] = [s]
            else:
                hashmap[ss].append(s)

        return [v for k, v in hashmap.items()]