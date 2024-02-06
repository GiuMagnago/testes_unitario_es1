class String:
    def length(self, s):
        c = 0
        for i in s:
            c += 1
        return c
    def getCharIndex(self, s, c):
        for i in range(len(s)):
            if s[i] == c:
                return i
        return -1
    def charChange(self, s, c, cC):
        s = list(s)
        for i in range(len(s)):
            if s[i] == c:
                s[i] = cC
        return ''.join(s)