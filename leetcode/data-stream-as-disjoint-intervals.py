from lc import *

# https://leetcode.com/problems/data-stream-as-disjoint-intervals/discuss/3107304/Python-simple-approach.-Expand-around-each-number-to-find-the-interval

class SummaryRanges:
    def __init__(self):
        self.v = set()
    def addNum(self, value: int) -> None:
        self.v.add(value)
    def getIntervals(self) -> List[List[int]]:
        v = []
        e = set()
        for x in self.v:
            if x in e:
                continue
            a = x
            while a-1 in self.v:
                a -= 1
                e.add(a)
            b = x
            while b+1 in self.v:
                b += 1
                e.add(b)
            v.append([a,b])
        return sorted(v)

SummaryRanges = type('',(),{
    '__init__':lambda s:setattr(s,'v',set()),
    'addNum':lambda s,v:s.v.add(v),
    'getIntervals':lambda s:(v:=[],e:=set()) and [v.append([(f:=lambda x,d:next((a for _ in count() if not
        (a+d in s.v and (a:=a+d, e.add(a)))),a:=x))(x,-1),f(x,1)]) for x in s.v if x not in e] and sorted(v)
    })

SummaryRanges = type('',(),{'__init__':lambda s:setattr(s,'v',set()),'addNum':lambda s,v:s.v.add(v),'getIntervals':lambda s:(v:=[],e:=set()) and [v.append([(f:=lambda x,d:next((a for _ in count() if not (a+d in s.v and (a:=a+d,e.add(a)))),a:=x))(x,-1),f(x,1)]) for x in s.v if x not in e] and sorted(v)})

test('''

352. Data Stream as Disjoint Intervals
Hard

758

170

Add to List

Share
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int value) Adds the integer value to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
 

Example 1:

Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
 

Constraints:

0 <= value <= 10^4
At most 3 * 10^4 calls will be made to addNum and getIntervals.
 

Follow up: What if there are lots of merges and the number of disjoint intervals is small compared to the size of the data stream?

''', SummaryRanges)


