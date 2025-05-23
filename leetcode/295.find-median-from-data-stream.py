from lc import *

# https://leetcode.com/problems/find-median-from-data-stream/discuss/74044/Very-Short-O(log-n)-%2B-O(1)

class MedianFinder:
    def __init__(self):
        self.data = 1, [], []

    def addNum(self, num):
        sign, h1, h2 = self.data
        heappush(h2, -heappushpop(h1, num * sign))
        self.data = -sign, h2, h1

    def findMedian(self):
        sign, h1, h2 = d = self.data
        return (h1[0] * sign - d[-sign][0]) / 2.0

class MedianFinder:
    def __init__(self):
        self.h = None, [], []
        self.i = 1

    def addNum(self, num):
        heappush(self.h[-self.i], -heappushpop(self.h[self.i], num * self.i))
        self.i *= -1

    def findMedian(self):
        return (self.h[self.i][0] * self.i - self.h[-1][0]) / 2.0

'''
# can't test those and they mess up local class but they work
class MedianFinder:
    def __init__(s):
        h = [[],1,-1,i:=[]]
        s.addNum=lambda n:heappush(h[-1],-heappushpop(h[0],n*h[1]))or h.reverse()
        s.findMedian=lambda:(h[0][0]*h[1]-i[0])/2
class MedianFinder:
    def __init__(s):
        h,s.addNum,s.findMedian=[[],1,-1,i:=[]],lambda n:heappush(h[-1],-heappushpop(h[0],n*h[1]))or h.reverse(),lambda:(h[0][0]*h[1]-i[0])/2

'''
MedianFilter=type('',(),{'__init__':lambda s:setattr(s,'h',(None,[],[]))or setattr(s,'i',1),'addNum':lambda s,n:(heappush(s.h[-s.i],-heappushpop(s.h[s.i],n*s.i)),setattr(s,'i',-s.i)),'findMedian':lambda s:(s.h[s.i][0]*s.i-s.h[-1][0])/2.0})

test('''
295. Find Median from Data Stream
Hard

8835

167

Add to List

Share
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
''', classname=MedianFinder)
