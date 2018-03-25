class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        char_to_codes = dict(zip(
                [chr(code) for code in range(97, 123)],
                [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
                 "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            ))
        return len(set(["".join(char_to_codes[char] for char in word) for word in words]))