from lc import *

# https://leetcode.com/problems/lemonade-change/discuss/143719/C%2B%2BJavaPython-Straight-Forward

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                five, ten = five - 1, ten + 1
            elif ten > 0:
                five, ten = five - 1, ten - 1
            else:
                five -= 3
            if five < 0:
                return False
        return True

class Solution:
    def lemonadeChange(self, b: List[int]) -> bool:
        f = t = 0
        for x in b:
            if x == 5:
                f += 1
            elif x == 10:
                f -= 1
                t += 1
            elif t > 0:
                f -= 1
                t -= 1
            else:
                f -= 3
            if f < 0:
                return False
        return True

# https://leetcode.com/problems/lemonade-change/discuss/5637599/Greedy-1-loop-vs-recursionoror40ms-Beats-99.76

class Solution:
    def lemonadeChange(self, b: List[int]) -> bool:
        def f(i,x,y):
            if i == len(b):
                return x>=0 and y>=0
            if x<0 or y<0:
                return 0
            t = b[i];
            if t==5:
                return f(i+1, x+1, y)
            if t==10:
                return f(i+1, x-1, y+1)
            if t==20 and y>0:
                return f(i+1, x-1, y-1)
            return f(i+1, x-3, y)
        return f(0,0,0)

class Solution:
    def lemonadeChange(self, b: List[int]) -> bool:
        return(f:=lambda i,x,y:x>=0 and y>=0 if not b[i:]else 0 if(x<0 or y<0)else f(i+1,x+1,y)if(t:=b[i])==5 else f(i+1,x-1,y+1)if t==10 else f(i+1,x-1,y-1)if t==20 and y>0 else f(i+1,x-3,y))(0,0,0)

class Solution:
    def lemonadeChange(self, b: List[int]) -> bool:
        def f(i,x,y):
            r = not(x<0 or y<0)
            if b[i:]:
                return r and f(i+1,x+1,y)if(t:=b[i])==5 else f(i+1,x-1,y+1)if t==10 else f(i+1,x-1,y-1)if t==20 and y>0 else f(i+1,x-3,y)
            return r
        return f(0,0,0)

class Solution:
    def lemonadeChange(self, b: List[int]) -> bool:
        return(f:=lambda i,x,y:(f(i+1,x+1,y)if(t:=b[i])==5 else f(i+1,x-1,y+1)if t==10 else f(i+1,x-1,y-1)if t==20 and y>0 else f(i+1,x-3,y))if(r:=not(x<0 or y<0))and b[i:]else r)(0,0,0)

class Solution:
    def lemonadeChange(self, b: List[int]) -> bool:
        return(f:=lambda i,x,y:(f(i+1,x+1,y)if(t:=b[i])==5 else f(i+1,x-1,y+1)if t==10 else f(i+1,x-1,y-1)if t==20 and y>0 else f(i+1,x-3,y))if(r:=x>-1<y)and b[i:]else r)(0,0,0)

class Solution:
    def lemonadeChange(self, b: List[int]) -> bool:
        return(f:=lambda i,x,y:(f(i+1,*((x+1,y)if(t:=b[i])==5 else(x-1,y+1)if t==10 else(x-1,y-1)if t==20 and y>0 else(x-3,y))))if(r:=x>-1<y)and b[i:]else r)(0,0,0)

class Solution:
    def lemonadeChange(self, b: List[int]) -> bool:
        return(f:=lambda i,x,y:(f(i+1,*((((x+1,y),(x-1,y+1))[b[i]>5],((x-3,y),(x-1,y-1))[y>0])[b[i]>10])))if(r:=x>-1<y)and b[i:]else r)(0,0,0)

class Solution:
    def lemonadeChange(self, b: List[int]) -> bool:
        f=t=0;[x<10and(f:=f+1)or(x<20and(f:=f-1,t:=t+1))or(t>0and(f:=f-1,t:=t-1)or(f:=f-3))for x in b];return f>=0

class Solution:
    def lemonadeChange(self, b: List[int]) -> bool:
        f=t=0
        
        for x in b:
            
            if x<10:
                f += 1
            elif x<20:
                f -= 1
                t += 1
            elif t>0:
                f -= 1
                t += 1
            else:
                f -= 3

        return f>=0


test('''
860. Lemonade Change
Easy

2510

169

Add to List

Share
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

 

Example 1:

Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
Example 2:

Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
 

Other examples:

Input: bills = [5,5,5,10,5,5,10,20,20,20]
Output: false

Input: bills = [5,5,5,5,20,20,5,5,5,5]
Output: false

Constraints:

1 <= bills.length <= 105
bills[i] is either 5, 10, or 20.
Accepted
238,298
Submissions
432,544
''')
