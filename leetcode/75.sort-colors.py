from lc import *

# dutch flag problem
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)-1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def f(a,b,l):l[a],l[b]=l[b],l[a]
        def fn(a,b):
            red, white, blue = a
            if nums[white] == 0:
                f(red,white,nums)
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                f(white,blue,nums)
                blue -= 1
            a = red, white, blue
            return a
        reduce(fn, nums, [0,0,len(nums)-1])

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def fn(t,b):
            red, white, blue = t
            return (swap:=lambda a,x,y: exec('a[x],a[y]=a[y],a[x]'), (swap(nums,red,white),(red+1,white+1,blue))[1] if nums[white]==0 else ((red,white+1,blue) if nums[white]==1 else (swap(nums,white,blue),(red,white,blue-1))[1]))[1]
        reduce(fn, nums, [0,0,len(nums)-1])

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        reduce(lambda a,_:(f:=lambda a,x,y:exec('a[x],a[y]=a[y],a[x]'),(f(nums,a[0],a[1]),(a[0]+1,a[1]+1,a[2]))[1]if nums[a[1]]==0 else((a[0],a[1]+1,a[2])if nums[a[1]]==1 else(f(nums,a[1],a[2]),(a[0],a[1],a[2]-1))[1]))[1],nums,[0,0,len(nums)-1])

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        reduce(lambda a,_:(f:=lambda a,x,y:(t:=a[x],setitem(a,x,a[y]),setitem(a,y,t)),(f(nums,a[0],a[1]),(a[0]+1,a[1]+1,a[2]))[1] if nums[a[1]]==0 else ((a[0],a[1]+1,a[2]) if nums[a[1]]==1 else (f(nums,a[1],a[2]),(a[0],a[1],a[2]-1))[1]))[1], nums, [0,0,len(nums)-1])

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        (s:=lambda a,x,y:(t:=a[x],setitem(a,x,a[y]),setitem(a,y,t),a)[3],f:=lambda a,i,j,k:(f(s(a,i,j),i+1,j+1,k) if a[j]==0 else f(a,i,j+1,k) if a[j]==1 else f(s(a,j,k),i,j,k-1)) if i<=j<=k else None)[1](nums,0,0,len(nums)-1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        (s:=lambda a,x,y:exec('a[x],a[y]=a[y],a[x]')or a,(f:=lambda a,i,j,k:i<=j<=k and(f(s(a,i,j),i+1,j+1,k)if a[j]==0 else f(a,i,j+1,k)if a[j]==1 else f(s(a,j,k),i,j,k-1)))(nums,0,0,len(nums)-1))

# updated 2024-06-12

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = one = 0
        for color in nums:
            zero += color == 0
            one += color == 1
        for i in range(len(nums)):
            nums[i] = 0 if i<zero else 1 if i<zero+one else 2
        return nums

class Solution:
    def sortColors(self, n: List[int]) -> None:
        n.sort()

test('''
75. Sort Colors
Medium

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

'''
, check=lambda res,exp,nums: nums==sorted(nums)

)
