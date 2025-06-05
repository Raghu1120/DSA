#Complete this function

class Solution:
    def josephus(self,n,k):
        #Your code here
        if n == 1:
            return 1  
        survivor = self.josephus(n - 1, k)
        return (survivor + k - 1) % n + 1
