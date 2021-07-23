class Solution:
    def trailingZeroes(self, N):
        result=1
        for i in range(2,N+1):
            result*=i
        l=len(str(result))
        count=0
        for j in range(result):
            a=str(result)[l-1-j]
            if int(a)==0:
         	    count+=1
            else:
                break
        return count

    	#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input()) 
        ob = Solution()
        ans = ob.trailingZeroes(N)
        print(ans)
# } Driver Code Ends