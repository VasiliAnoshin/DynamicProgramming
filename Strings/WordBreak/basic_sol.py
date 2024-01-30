class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        def dfs(s, wordDict):
            if len(s) == 0:
                return True
            
            val = False
            for i in range(len(s)):
                if s[:i+1] in wordDict:
                    val = dfs(s[i+1:], wordDict)
                    if val:
                        return True
            return val    

        return dfs(s, wordDict)
    
sol = Solution()
sol.wordBreak("leetcode", ["leet", "code"])