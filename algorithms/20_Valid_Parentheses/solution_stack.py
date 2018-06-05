class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        # use a stack to keep track of opening parenthese so far
        when we see a closing parenthese, if it is not a match for the latest open paren, then its not valid
        O(n) time
        O(n) space
        """
        if len(s) % 2 != 0:
            return False
        openings = set('{[(')
        matching = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for parenthese in s:
            if parenthese in openings:
                stack.append(parenthese)
            else:
                if len(stack) == 0:
                    return False
                last_open = stack.pop()
                if matching[last_open] != parenthese:
                    return False
        return len(stack) == 0