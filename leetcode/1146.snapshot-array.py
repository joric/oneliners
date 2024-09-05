from lc import *

class SnapshotArray:
    def __init__(self, length: int):
        self.a = [[[-1,0]] for _ in range(length)]
        self.i = 0

    def set(self, index: int, val: int) -> None:
        self.a[index].append([self.i, val])

    def snap(self) -> int:
        self.i += 1
        return self.i - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.a[index][bisect_right(self.a[index],[snap_id+1])-1][1]

SnapshotArray=type('',(),{'__init__':lambda s,l:setattr(s,'a',[[[-1,0]]for _ in range(l)])or setattr(s,'i',0),'set':lambda s,i,v:s.a[i].append([s.i,v]),'snap':lambda s:setattr(s,'i',s.i+1) or s.i-1,'get':lambda s,i,d:s.a[i][bisect_right(s.a[i],[d+1])-1][1]})


test('''
1146. Snapshot Array
Medium

2212

315

Add to List

Share
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]

Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 

Constraints:

1 <= length <= 5 * 10^4
0 <= index < length
0 <= val <= 10^9
0 <= snap_id < (the total number of times we call snap())
At most 5 * 10^4 calls will be made to set, snap, and get.
Accepted
144,052
Submissions
389,534
Seen this question in a real interview before?

Yes

No
Use a list of lists, adding both the element and the snap_id to each index.
''',classname=SnapshotArray)
