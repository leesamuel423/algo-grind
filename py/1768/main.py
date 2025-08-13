class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        w1 = 0

        while w1 < len(word1) and w1 < len(word2):
            output += word1[w1]
            output += word2[w1]
            w1 += 1

        if w1 < len(word1):
            output += word1[w1:]
        elif w1 < len(word2):
            output += word2[w1:]

        return output
