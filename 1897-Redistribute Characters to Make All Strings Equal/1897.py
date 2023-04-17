class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True
        string = ''.join(words)
        counts = {}
        for char in string:
            if counts.get(char):
                counts[char] += 1
            else:
                counts[char] = 1
        for count in counts.values():
            if count % len(words) != 0:
                return False
        return True