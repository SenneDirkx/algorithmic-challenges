class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len(list(filter(lambda x: x in J, S)))