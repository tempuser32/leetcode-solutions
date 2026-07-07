"""class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        for i in range(0,len(s)//2):
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                r-=1
        print(l,r)
        if l==r:
            return True
        return False
"""
class Solution:
    def validPalindrome(self,s:str)->bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            if s[l]!=s[r]:
                if s[l+1]==s[r]:
                    return True
                if s[l]==s[r-1]:
                    return True
                if s[l+1]==s[r-1]:
                    return False
            return True
        if len(s)==1:
            return True
        return False