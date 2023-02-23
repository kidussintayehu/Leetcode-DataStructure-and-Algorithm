class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        oldCheck = list(words[0])
        for word in words[1:]:
            newCheck = []
            for ch in word:
                if ch in oldCheck:
                    newCheck.append(ch)
                    oldCheck.remove(ch)
            oldCheck = newCheck
        return oldCheck