# https://leetcode.com/problems/number-of-matching-subsequences/description/
# not accepted
class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        brute force check sub sequence word by word too slow
        """
        words = [word for word in words if set(word).issubset(set(S))]
        return sum(isSubSequence("".join(s for s in S if s in word), word, len("".join(s for s in S if s in word)), len(word)) for word in words)


# def isSubSequence(S, word, S_tail, word_tail):
#     if word_tail == 0:
#         return True
#     if S_tail == 0:
#         return False
#     if S[S_tail - 1] == word[word_tail - 1]:
#         return isSubSequence(S, word, S_tail - 1, word_tail - 1)
#     return isSubSequence(S, word, S_tail - 1, word_tail)

def isSubSequence(S, word, S_length, word_length):
    S_head = 0
    word_head = 0
    while S_head < S_length and word_head < word_length:
        if word[word_head]== S[S_head]:
            word_head = word_head+1
        S_head = S_head + 1
    return word_head == word_length
