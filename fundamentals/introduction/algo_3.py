def isPalindrome(input):
    for i in range(0,len(input)//2):
        if input[i] != input[len(input)- 1 -i]:
            return False
    return True


def longestPalindrome(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return s
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    start = 0
    length = 1
        
    ##length==1
    for i in range(n):
        dp[i][i] = True
        
    ##length==2:
    for i in range(n-1):
        if s[i]==s[i+1]:
            dp[i][i+1] = True
            length =2
            start = i
        
    ##length >2:
    for l in range(n-3, -1, -1):
        for r in range(l+2, n):
            if s[l] == s[r] and dp[l+1][r-1]:
                dp[l][r] = True
                if r-l+1>length:
                    length = r-l+1
                    start = l
        
    return s[start: start+length]
    
print(longestPalindrome("Yikes! my favorite racecar erupted!"))