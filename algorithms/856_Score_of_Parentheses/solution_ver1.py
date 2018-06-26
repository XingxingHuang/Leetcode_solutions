class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        mapping = {
            '((': '2*(',
            '()': '1',
            ')(': '+',
            '))': ')'
        }
        return eval(''.join([mapping[combo] for combo in map(lambda x: ''.join(x), zip(S[:-1], S[1:]))]))
