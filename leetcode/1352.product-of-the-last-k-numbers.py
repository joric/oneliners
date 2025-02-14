from lc import *

# https://leetcode.com/problems/product-of-the-last-k-numbers/solutions/510260/java-c-python-prefix-product/?envType=daily-question&envId=2025-02-14

class ProductOfNumbers:
    def __init__(self):
        self.a=[1]

    def add(self, x: int) -> None:
        if x==0:
            self.a=[1]
        else:
            self.a.append(self.a[-1]*x)

    def getProduct(self, k: int) -> int:
        return self.a[-1] // self.a[~k] if k<len(self.a) else 0

ProductOfNumbers=type('',(),{'__init__':lambda s: setattr(s,'a',[1]),'add':lambda s,x:setattr(s,'a',[1])if x<1 else s.a.append(s.a[-1]*x),'getProduct':lambda s,k:k<len(s.a)and s.a[-1]//s.a[~k]or 0})

test('''
1352. Product of the Last K Numbers
Medium
Topics
Companies
Hint
Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

 

Example:

Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
 

Constraints:

0 <= num <= 100
1 <= k <= 4 * 104
At most 4 * 104 calls will be made to add and getProduct.
The product of the stream at any point in time will fit in a 32-bit integer.
 

Follow-up: Can you implement both GetProduct and Add to work in O(1) time complexity instead of O(k) time complexity?
Seen this question in a real interview before?
1/5
Yes
No
Accepted
101.7K
Submissions
192.3K
Acceptance Rate
52.9%
Topics
Array
Math
Design
Data Stream
Prefix Sum
Companies
Hint 1
Keep all prefix products of numbers in an array, then calculate the product of last K elements in O(1) complexity.
Hint 2
When a zero number is added, clean the array of prefix products.
''', ProductOfNumbers)
