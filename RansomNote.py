class Solution:
    # approach : construct two dicts
    # if all the characters in ransomnote are present at an equal or higher freq in magazine
    # eg if ransomnote contains 'a' 3 times, and 'b' two times, and if magazine contains 'a'more than or equal to 3 times and 'b' more than or equal to 2 times,
    # regardless of the order, then ransom note can be contructed otherwise not.
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(not ransomNote):
            return True
        
        if(ransomNote==magazine):
            return True
        
        d1={}
        d2={}
        for i in magazine:
            if(i not in d1.keys()):
                d1[i]=1
            else:
                d1[i]+=1
                
        for i in ransomNote:
            if(i not in d2.keys()):
                d2[i]=1
            else:
                d2[i]+=1  
           
        flag=True
        for i in d2.keys():
            if(i not in d1.keys() or d1[i]<d2[i]):
                flag=False
                break
                
        return flag
