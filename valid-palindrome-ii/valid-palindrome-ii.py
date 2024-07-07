class Solution:
    def validPalindrome(self, s: str) -> bool:
        length = len(s)
        if length % 2 == 0:
            offset = 0
        else:
            offset = 1
        last_index = len(s)//2 + offset
        
        current_index_l = 0
        current_index_r = 0
        deleted = 0
        deleted_index = 0
        
        while current_index_l < last_index and current_index_r < last_index:
            if s[current_index_l] != s[~current_index_r]:
                if deleted == 0:
                    current_index_r += 1
                    deleted += 1
                    deleted_index = current_index_l
                    last_index += 1
                elif deleted == 1:
                    current_index_l = deleted_index + 1
                    current_index_r = deleted_index
                    deleted += 1
                else:
                    return False
            else:
                current_index_l += 1
                current_index_r += 1
        
        return True