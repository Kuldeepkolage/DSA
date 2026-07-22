class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        ans = []
        
        prime = [True for _ in range(n+1)]
        prime[0] = prime[1] = False
        
        for i in range(2, n+1):
            if prime[i]:
                j = i*i
                
                while j<=n:
                    prime[j] = False
                    j += i
        for i in range(2,n):
            if i+i>n: break
            if prime[i] and prime[n-i]:
                ans.append([i,n-i])
        return ans
    