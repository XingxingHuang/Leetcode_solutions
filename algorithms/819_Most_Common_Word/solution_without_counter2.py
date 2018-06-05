class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = "".join(char.lower() for char in paragraph if char not in "!?',;.")
        words = [word for word in paragraph.split(" ") if word not in banned]
        word_counts = dict()
        for word in words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1

        # notice that the vs may not be unique, v:k with same v will be updated through the process
        reverse_lookup = {v: k for k, v in word_counts.items()}
        return reverse_lookup[max(reverse_lookup.keys())]