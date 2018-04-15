from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = "".join(char.lower() for char in paragraph if char not in "!?',;.")
        words = [word for word in paragraph.split(" ") if word not in banned]
        return Counter(words).most_common(1)[0][0]