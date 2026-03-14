from lc import *

# https://leetcode.com/problems/fancy-sequence/solutions/898753/python-time-o1-for-each-by-lee215-tp2c/?envType=daily-question&envId=2026-03-15

class Fancy:
    def __init__(self):
        self.d = []
        self.add = [0]
        self.mul = [1]

    def append(self, a: int) -> None:
        self.d.append(a)
        self.add.append(self.add[-1])
        self.mul.append(self.mul[-1])

    def addAll(self, inc: int) -> None:
        self.add[-1] += inc

    def multAll(self, m: int) -> None:
        self.add[-1] = self.add[-1] * m % (10 ** 9 + 7)
        self.mul[-1] = self.mul[-1] * m % (10 ** 9 + 7)

    def getIndex(self, i: int) -> int:
        if i >= len(self.d): return -1
        mod = 10 ** 9 + 7
        m = self.mul[-1] * pow(self.mul[i], mod - 2, mod) 
        inc = self.add[-1] - self.add[i] * m
        return (self.d[i] * m + inc) % mod

# TODO

class Fancy:
    def __init__(s):
        s.d = []
        s.a = [0]
        s.m = [1]
        s.t = 10**9+7

    def append(s, a: int) -> None:
        s.d.append(a)
        s.a.append(s.a[-1])
        s.m.append(s.m[-1])

    def addAll(self, i: int) -> None:
        self.a[-1] += i

    def multAll(s, m: int) -> None:
        s.a[-1] = s.a[-1] * m % s.t
        s.m[-1] = s.m[-1] * m % s.t

    def getIndex(s, i: int) -> int:
        if i < len(s.d):
            m = s.m[-1]*pow(s.m[i],s.t-2,s.t)
            p = s.a[-1]-s.a[i] * m
            return (s.d[i]*m+p) % s.t
        else:
            return -1

class Fancy:
    def __init__(s):
        s.d = []
        s.a = [0]
        s.m = [1]
        s.t = 10**9+7

    def append(s, a: int) -> None:
        s.d.append(a)
        s.a.append(s.a[-1])
        s.m.append(s.m[-1])

    def addAll(self, i: int) -> None:
        self.a[-1] += i

    def multAll(s, m: int) -> None:
        s.a[-1] = s.a[-1] * m % s.t
        s.m[-1] = s.m[-1] * m % s.t

    def getIndex(s, i: int) -> int:
        if i < len(s.d):
            m = s.m[-1]*pow(s.m[i],s.t-2,s.t)
            p = s.a[-1]-s.a[i] * m
            return (s.d[i]*m+p) % s.t
        else:
            return -1

test('''
1622. Fancy Sequence
Solved
Hard
Topics
premium lock icon
Companies
Hint
Write an API that generates fancy sequences using the append, addAll, and multAll operations.

Implement the Fancy class:

Fancy() Initializes the object with an empty sequence.
void append(val) Appends an integer val to the end of the sequence.
void addAll(inc) Increments all existing values in the sequence by an integer inc.
void multAll(m) Multiplies all existing values in the sequence by an integer m.
int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.
 

Example 1:

Input
["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
Output
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

Explanation
Fancy fancy = new Fancy();
fancy.append(2);   // fancy sequence: [2]
fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
fancy.append(7);   // fancy sequence: [5, 7]
fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10);  // fancy sequence: [13, 17, 10]
fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20
 

Constraints:

1 <= val, inc, m <= 100
0 <= idx <= 105
At most 105 calls total will be made to append, addAll, multAll, and getIndex.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
15,423/82.3K
Acceptance Rate
18.7%
Topics
Principal
Math
Design
Segment Tree
Biweekly Contest 37
icon
Companies
Hint 1
Use two arrays to save the cumulative multipliers at each time point and cumulative sums adjusted by the current multiplier.
Hint 2
The function getIndex(idx) ask to the current value modulo 10^9+7. Use modular inverse and both arrays to calculate this value.
''', Fancy)
