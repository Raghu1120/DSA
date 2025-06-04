class Solution(object):
    def candy(self, ratings):
        sum = 1
        i=1
        peak =1
        down =1
        n= len(ratings)
        while i<n:
            if ratings[i] == ratings[i-1]:
                sum = sum+1
                i+=1
                continue
            while i<n and ratings[i] > ratings[i-1]: 
                peak+=1
                sum+=peak
                i+=1
                continue
            while i<n and ratings[i] < ratings[i-1]:
                sum+=down
                i+=1
                down+=1
            if down > peak:
                sum+= down-peak
            peak =1
            down =1
        return sum   
        