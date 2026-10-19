class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s.lower():
            if (i.isalnum())==False:
                print(i)
                s=s.replace(i,"")
        
        print ("".join(reversed(s.lower())),s.lower())
        return ("".join(reversed(s.lower()))==s.lower())