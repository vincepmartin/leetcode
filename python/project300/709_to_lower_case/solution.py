class Solution:
    def toLowerCase(self, str: str) -> str:
        # How much do we have to subtract?
        n = ord('A') - ord('a')
        upper = []