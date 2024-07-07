class Solution:
    def minDeletions(self, s: str) -> int:
        store = {}
        for c in s:
            if c in store:
                store[c] += 1
            else:
                store[c] = 1
        
        result = 0
        used = set()
        
        for ch in store:
            freq = store[ch]
            while freq > 0 and freq in used:
                freq -= 1
                result += 1
            used.add(freq)
        
        return result