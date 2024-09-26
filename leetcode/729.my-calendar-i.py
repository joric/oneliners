from lc import *

# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:
    def __init__(self):
        self.books = [[float('-inf'), float('-inf')], [float('inf'), float('inf')]]
    def book(self, start: int, end: int) -> bool:
        idx = bisect_left(self.books, [start, end])
        if start < self.books[idx-1][1] or end > self.books[idx][0]:
            return False
        insort(self.books, [start, end])
        return True

# https://leetcode.com/problems/my-calendar-i/discuss/2373496/Python-simple-but-slow-solution

class MyCalendar:
    def __init__(self):
        self.booklist = []
    def book(self, start: int, end: int) -> bool:
        for booked in self.booklist:
            if start > booked[0] and start < booked[1]:
                return False
            if end > booked[0] and end < booked[1]:
                return False
            if start <= booked[0] and end >= booked[1]:
                return False
        self.booklist.append([start, end])
        return True

class MyCalendar(list):
    def book(s, a: int, b: int) -> bool:
        for p,q in s:
            if a>p and a<q:
                return False
            if b>p and b<q:
                return False
            if a<=p and b>=q:
                return False
        s.append([a,b])
        return True

class MyCalendar(list):
    def book(s, a: int, b: int) -> bool:
        return not(any((p<a<q)or(p<b<q)or(a<=p and b>=q)for p,q in s)or s.append([a,b]))

MyCalendar=type('',(list,),{'book':lambda s,a,b:not(any((p<a<q)or(p<b<q)or(a<=p and b>=q)for p,q in s)or s.append([a,b]))})

MyCalendar=type('',(list,),{'book':lambda s,a,b:not(any(a<q and b>p for p,q in s)or s.append([a,b]))})

MyCalendar=type('',(list,),{'book':lambda s,a,b:not(any(q>a<b>p for p,q in s)or s.append([a,b]))})

class MyCalendar(list):book=lambda s,a,b:not(any(q>a<b>p for p,q in s)or s.append([a,b]))

class MyCalendar(list):
    def book(s, a: int, b: int) -> bool:
        return not(any(q>a<b>p for p,q in s)or s.append([a,b]))

test('''
729. My Calendar I
Medium

4232

112

Add to List

Share
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.
Accepted
293,051
Submissions
517,876
''', MyCalendar)

