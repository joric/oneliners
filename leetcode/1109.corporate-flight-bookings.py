from lc import *

# Q2 at Weekly contest 144 
# https://leetcode.com/problems/corporate-flight-bookings
# https://leetcode.com/contest/weekly-contest-144/problems/corporate-flight-bookings/

# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/solutions/1624291/crappy-testing-of-leetcode/comments/3104335/

'''
Python limits are fine but when Java on Leetcode is faster than C++ that is basically cheating. This bruteforce in Java was accepted:

https://leetcode.com/problems/corporate-flight-bookings/submissions/1114850361/
This bruteforce in C++ was rejected with TLE during contest:

https://leetcode.com/problems/corporate-flight-bookings/submissions/1114834655/
Better cut Java limits.

Related post:

https://leetcode.com/problems/merge-k-sorted-lists/solutions/10890/why-c-is-slower-than-java-or-python-thats-unbelievable/

class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] arr = new int[n];
        for(int[] booking : bookings){
            int k = booking[2];
            int i = booking[0];
            int j = booking[1];
            for(int idx = i-1;idx<j;idx++){
                arr[idx]+=k;
            }
        }
        return arr;
    }
}

class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> arr(n);
        for (vector<int> &booking:bookings) {
            int k = booking[2];
            int i = booking[0];
            int j = booking[1];
            for(int idx = i-1;idx<j;idx++){
                arr[idx]+=k;
            }
        }
        return arr;
    }
};

Also see https://leetcode.com/discuss/post/189808/java-13-is-the-official-version-on-leetc-mr8p/

'''

# https://leetcode.com/problems/corporate-flight-bookings/solutions/1313236/python-4-lines-o-n/


class Solution:
    def corpFlightBookings(self, b: List[List[int]], n: int) -> List[int]:
        a=[0]*(n+3)
        for i in b:
            a[i[0]]+=i[2]
            a[i[1]+1]-=i[2]
        for j in range(1,n+3):
            a[j]+=a[j-1]
        return a[1:-2]

# https://leetcode.com/problems/corporate-flight-bookings/solutions/2940321/python-3-5-lines-prefix-sum-t-s-96-81/

class Solution:
    def corpFlightBookings(self, b: List[List[int]], n: int) -> List[int]:
        c = [0]*(n+1)
        for i,j,x in b:
            c[i-1]+= x
            c[j]-= x
        return[*accumulate(c[:-1])]

class Solution:
    def corpFlightBookings(self, b: List[List[int]], n: int) -> List[int]:
        c=[0]*(n+1);[setitem(c,i-1,c[i-1]+x)or setitem(c,j,c[j]-x)for i,j,x in b];return[*accumulate(c[:-1])]

test('''
1109. Corporate Flight Bookings
Solved
Medium
Topics
premium lock icon
Companies
There are n flights that are labeled from 1 to n.

You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.

 

Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
Explanation:
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Total seats:         10  55  45  25  25
Hence, answer = [10,55,45,25,25]
Example 2:

Input: bookings = [[1,2,10],[2,2,15]], n = 2
Output: [10,25]
Explanation:
Flight labels:        1   2
Booking 1 reserved:  10  10
Booking 2 reserved:      15
Total seats:         10  25
Hence, answer = [10,25]

 

Constraints:

1 <= n <= 2 * 104
1 <= bookings.length <= 2 * 104
bookings[i].length == 3
1 <= firsti <= lasti <= n
1 <= seatsi <= 104
Seen this question in a real interview before?
1/5
Yes
No
Accepted
86,563/133.4K
Acceptance Rate
64.9%
Topics
Array
Prefix Sum
Weekly Contest 144
icon
Companies
Similar Questions
Zero Array Transformation II
Medium
Zero Array Transformation III
Medium
''')

