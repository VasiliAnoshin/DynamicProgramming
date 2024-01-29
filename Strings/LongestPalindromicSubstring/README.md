``` python
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
```
Time Complexity: ![O(n^3)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^3)>)

Explanation:for each character check both for palindrom that in odd length and even length. This solution is O(N^3)



``` python
def longestPalindrome(s):
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        #filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
				# j starts from the i location : to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:  #if the chars mathces
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]
                
        return longest_palindrom
```

Explanation:
