class Solution:
    def isValid(self, s: str) -> bool:
        stackdict={")":"(","}":"{","]":"["}
        stackpar=[]
        for c in s:
            if c in stackdict:
                if stackpar and stackpar[-1]==stackdict[c]:
                    stackpar.pop()
                else:
                    return False
            else:
                stackpar.append(c)
        return True if not stackpar else False
