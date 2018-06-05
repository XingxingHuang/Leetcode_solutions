class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        # not sure why i did this, but sort seems needs longer time!
        """
        paragraph = "".join(char.lower() for char in paragraph if char not in "!?',;.")
        # words = [word for word in paragraph.split(" ") if word not in banned]
        # return Counter(words).most_common(1)[0][0]
        word_counts = {}
        for word in paragraph.split(" "):
            if word in banned:
                continue
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
        return sorted(word_counts.items(), key=lambda kv: kv[1], reverse=True)[0][0]