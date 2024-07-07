class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return []
        
        sorted_p = sorted(p)
        result = []
        
        for i in range(len_s-len_p+1):
            sub_s = sorted(s[i:i+len_p])
            
            if sorted_p == sub_s:
                result.append(i)
        return result