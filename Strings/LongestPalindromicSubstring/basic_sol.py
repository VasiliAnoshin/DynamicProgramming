class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = s[0]
        for i in range(len(s)):
            #odd length
            j=1
            while i-j>=0 and i +j <len(s) and s[i-j] == s[i+j]:
                tmp = s[i-j: i+j+1]
                if len(tmp) > len(output):
                    output = tmp
                j+=1
            #even length
            k,j=0,1
            while i-k>=0 and i+j<len(s) and s[i-k]==s[i+j]:
                tmp = s[i-k:i+j+1]
                if len(tmp) >= len(output):
                    output = tmp
                j+=2
                i-=1
        return output

sol = Solution()
res = sol.longestPalindrome("tattarrattat")
print(res)