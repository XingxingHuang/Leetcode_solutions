class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line_nums = 1
        char_nums = 0
        for char in S:
            width_needed = widths[ord(char) - 97]
            if char_nums + width_needed > 100:
                char_nums = width_needed
                line_nums += 1
            else:
                char_nums += width_needed

        # print(line_nums, char_nums)
        return [line_nums, char_nums]
