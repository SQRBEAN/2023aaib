class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N=len(s)
        ansA=0
        ansB=0
        a=s[:N//2]
        b=s[N//2:]
        for c in a:
            if c=='a'or c=='e' or c=='i' or c=='o' or c=='u':
                ansA+=1
            if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
                ansA+=1
        for c in b:
            if c=='a'or c=='e' or c=='i' or c=='o' or c=='u':
                ansB+=1
            if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
                ansB+=1
        if ansA==ansB:return True
        else: return False