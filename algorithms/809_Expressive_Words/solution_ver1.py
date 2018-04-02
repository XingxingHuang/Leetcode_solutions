

def make_grouped_chars(word):
    """
    :param word: the word to process, like 'heeelloo'
    :return: list of char groups, like ['h', 'eee', 'll', 'oo']
    """
    chars = list(word)
    grouped_chars = [chars[0]]
    for char in chars[1:]:
        if char in grouped_chars[-1]:
            grouped_chars[-1] += char
        else:
            grouped_chars.append(char)
    return grouped_chars

class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        Divide S and word into group of chars, compare them group by group
        """
        S_char_groups = make_grouped_chars(S)
        return sum([self.expressiveWord(S_char_groups, make_grouped_chars(word)) for word in words])

    @staticmethod
    def expressiveWord(S_char_groups, word_char_groups):
        """
        :param S_char_groups: like ['h', 'eee', 'll', 'oo']
        :param word_char_groups:  like ['h', 'e', 'l', 'o']
        :return:
        """
        if len(S_char_groups) != len(word_char_groups):
            return False
        i, j = 0, 0
        while i < len(S_char_groups):
            if S_char_groups[i] == word_char_groups[j]:
                # 'h' == 'h' => move to next group
                i += 1
                j += 1
            elif word_char_groups[j] in S_char_groups[i] and len(S_char_groups[i]) > 2:
                # 'e' from word 'eee' from S => move to next group
                i += 1
                j += 1
            else:
                # 'l' from word 'll' from S => return False
                # or 'e' from word 'l' from S => return False
                return False
        return True
