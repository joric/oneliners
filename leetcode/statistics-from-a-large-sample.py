from lc import *

# Q1, https://leetcode.com/contest/weekly-contest-142

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:

        def countkth (count, k):
            yet = 0
            for i in range (len (count)):
                if yet <= k < yet + count[i]:
                    return i
                yet += count[i]

        for a in range (256):
            if count[a]>0:
                break
        Min = a

        for b in range (255, -1, -1):
            if count[b]>0:
                break
        Max = b

        Mean = sum (i*count[i] for i in range (256)) / sum (count)
        Mode = max (range (256), key = lambda x: count[x])

        total = sum (count)

        if total % 2 == 1:
            Median = countkth (count, total // 2)
        else:
            Median = (countkth (count, total // 2 - 1) + countkth (count, total // 2)) / 2

        return [float (x) for x in [Min, Max, Mean, Median, Mode]]

# numpy, out of memory
class Solution:
    def sampleStats(self, c: List[int]) -> List[float]:
        import numpy as p;a=[i for v in[x*[i]for i,x in enumerate(c)] for i in v];return(float(f(a))for f in(min,max,p.mean,p.median,mode))

# https://leetcode.com/problems/statistics-from-a-large-sample/discuss/1471732/Pure-NumPy-solution!-100-ms-31.3-MB-(python)
import numpy as p
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        c = p.asarray(count)
        nz = p.nonzero(c)[0]
        dot = p.dot(p.arange(c.size), c)
        n = p.sum(c)
        cs = p.cumsum(c)
        div, mod = p.divmod(n, 2)

        if mod == 0:
            spots = p.searchsorted(cs, [div, div+1], side='left')
            the_median = spots.mean()
        else:
            the_median = p.searchsorted(cs, div, side='right')

        the_minimum = p.min(nz)
        the_maximum = p.max(nz)
        the_mean    = p.divide(dot, n)
        the_mode    = p.argmax(c)
        return [the_minimum, the_maximum, the_mean, the_median, the_mode]

# https://leetcode.com/problems/statistics-from-a-large-sample/discuss/1803919/Python3-one-pass-O(n)

class Solution:
    def sampleStats(self, c: List[int]) -> List[float]:
        a,b,m,f,s,n,v=float('+inf'),float('-inf'),0,0,0,0,[]
        for i,x in enumerate(c):
            if x>0: 
                a = min(a,i)
                b = max(b,i)
            if x>f:
                m = i
                f = x
            s += x*i
            n += x
            v.append(n)
        return[a,b,s/n,(bisect_left(v,(n-1)//2)+bisect_right(v,n//2))/2,m]

class Solution:
    def sampleStats(self, c: List[int]) -> List[float]:
        a,b,m,f,s,n,v=float('+inf'),float('-inf'),0,0,0,0,[]
        for i,x in enumerate(c):
            x>0 and(a:=min(a,i),b:=max(b,i))
            x>f and(m:=i,f:=x)
            s += x*i
            n += x
            v.append(n)
        return[a,b,s/n,(bisect_right(v,(n-1)//2)+bisect_right(v,n//2))/2,m]

class Solution:
    def sampleStats(self, c: List[int]) -> List[float]:
        a,b,r=inf,-inf,bisect_right;m=f=s=n=0;v=[(x>0 and(a:=min(a,i),b:=max(b,i)),x>f and(m:=i,f:=x),s:=s+x*i)and(n:=n+x)for i,x in enumerate(c)];return[a,b,s/n,(r(v,(n-1)//2)+r(v,n//2))/2,m]

test('''
1093. Statistics from a Large Sample
Medium

134

102

Add to List

Share
You are given a large sample of integers in the range [0, 255]. Since the sample is so large, it is represented by an array count where count[k] is the number of times that k appears in the sample.

Calculate the following statistics:

minimum: The minimum element in the sample.
maximum: The maximum element in the sample.
mean: The average of the sample, calculated as the total sum of all elements divided by the total number of elements.
median:
If the sample has an odd number of elements, then the median is the middle element once the sample is sorted.
If the sample has an even number of elements, then the median is the average of the two middle elements once the sample is sorted.
mode: The number that appears the most in the sample. It is guaranteed to be unique.
Return the statistics of the sample as an array of floating-point numbers [minimum, maximum, mean, median, mode]. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
Explanation: The sample represented by count is [1,2,2,2,3,3,3,3].
The minimum and maximum are 1 and 3 respectively.
The mean is (1+2+2+2+3+3+3+3) / 8 = 19 / 8 = 2.375.
Since the size of the sample is even, the median is the average of the two middle elements 2 and 3, which is 2.5.
The mode is 3 as it appears the most in the sample.
Example 2:

Input: count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: [1.00000,4.00000,2.18182,2.00000,1.00000]
Explanation: The sample represented by count is [1,1,1,1,2,2,2,3,3,4,4].
The minimum and maximum are 1 and 4 respectively.
The mean is (1+1+1+1+2+2+2+3+3+4+4) / 11 = 24 / 11 = 2.18181818... (for display purposes, the output shows the rounded number 2.18182).
Since the size of the sample is odd, the median is the middle element 2.
The mode is 1 as it appears the most in the sample.
 

Constraints:

count.length == 256
0 <= count[i] <= 10^9
1 <= sum(count) <= 10^9
The mode of the sample that count represents is unique.
''', check=lambda res,expected,*_:[*map(lambda x:round(x,5),res)]==expected
)
