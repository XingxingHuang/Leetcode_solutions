class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        common_prefix_length = 0
        max_length = min(map(len, strs))
        for i in range(max_length):
            if all([s[i] == strs[0][i] for s in strs]):
                common_prefix_length += 1
            else:
                break
        return strs[0][:common_prefix_length] if common_prefix_length > 0 else ""