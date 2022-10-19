a = "abdcdc"
a = set(a)
print(a)


'''
a = input("input your value for a:")
b = a 
a = 3
print(a, b)
'''


# this is a test for git proxy configuration.
# continue to test
'''
import collections
from collections import Counter

count = collections.Counter()

for i in range(10):
    count[i] += 1

print(count)

print(ord('A'))
print(ord('a'))


'''

'''
from collections import Counter

list = [2,3,3,2,5,4,5,6,3,3,4,4,5,5,2]
res = Counter(list)
print(res)
print(res[2])


'''

'''

brand = ("huawei","apple","samsung")
price = (1,2,4)
x = zip(brand,price)
x = list(x)
x.sort()
print(list(x))
for i in range(3):
    print(x[i][1])
'''

'''
s = "a"
print(s[1:]) 
if s[1:] > "":
    print(1)
if s[1:] == "":
    print(2)
'''


'''
from math import factorial


#print(factorial(3))
m = 2
n = 4
grid = [[1 for _ in range(n)] for x in range(m)]
print(grid)
list = [i for i in range(m)]
print(list)


'''
'''
string = "aaa"
string = "nn"
print(string)

k = 8
k = k>>1
print(k)
'''

'''
a = [1,3,4,2,5,3,2,5,6]
for i, e in reversed(a):
    print(i,e)
'''

'''
import time
import random

res1 = 0
res2 = 0

start_time1 = time.time()

for i in range(10000):
    res1 += random.randint(0,9999)

end_time1 = time.time()

start_time2 = time.time()

for i in range(10000):
    res2 += i
end_time2 = time.time()


print("calculate1 uses time: ", end_time1 - start_time1)
print("calculate2 uses time: ", end_time2 - start_time2)

print(res1, res2)
'''
'''
a = [2,2,3]
b = a.copy()
b.append(4)
print(b)
print(a)
'''

'''
from collections import Counter

# Counter with sequence of items
print(Counter(['b','b','a','c','b','a','b']))

# Counter with dictionary
print(Counter({'a':2,'b':3,'c':3}))

# Counter with keywords arguments
print(Counter(a=3,b=2,c=5))
'''

'''
list = [1, 3, 4, 3  ]
print(max(list))

test = []
if test:
    print(1)
'''

# you cannot pass anything by value in python :(
'''
a = [1,2,3]
b = []
b = a 
b.append(4)
print(a)
c = a[:]
c.append(9)
print(a)
print(c)
'''
''''
class ListNode:
    def __init__(self, data): # this part we define the node with input 
        self.data = data
        self.next = None
        
    def __repr__(self):       # this part return the value we want to repr the node
        return self.data   
        
 # initialize a linked list with a head node:
 
class LinkedList:
    def __init__(self, nodes=None): # define linkedlist quickly with input node value (default 0)
        self.head = None
        if nodes is not None:
            node = ListNode(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = ListNode(data=element)
                node = node.next

    def __repr__(self): # represent the whole list from head, then traverse the list
        node = self.head
        nodes = []    # create a nodes function to represent the linked list as a common list
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)

linkedlist2 = LinkedList(["a", "b", "c", "d","e"])
print(linkedlist2)

first_node = ListNode("M")  # we defined a repr module.
print(first_node)
'''


'''
list = [1,2,3]
a = list.pop(0)

print(a)
'''

'''
list = [1,2,3,4,5,6]
list.pop()
print(list)
list.pop(2)
print(list)
'''
'''
a = 2
b = 3
print(f"a = {a}, b = {b}")
a,b = b,a
print("after exchange: ")
print("a = {}, b = {}".format(a,b))
'''

'''
tuple = {"a", "b", "c"}
tuple2 = ("a", "b", "c")
res = []
res = "make".join(tuple2)
print(res)
# tuple is inordered like a set
dict = {
    "a": "1",
    "b": "2",
    "c": "3"
}
res2 = []
res2 = "make".join(dict)      # the "make" before join is a separator.
print(res2)
'''


'''
a = "aa"
ans = []
print(type(ans))
ans = "".join(a)
ans = "2"
ans = "".join("1")
print(ans)
print(type(ans))
'''


'''
nums = [-2,-1,-1,1,1,2,2]
new = sorted(nums)
print(new)

def twoSum(nums: list[int], target: int) -> list[list[int]]:
    
    nums = sorted(nums)
    res = []
    
    lo = 0
    hi = len(nums)-1
    while lo < hi:
        if nums[lo] + nums[hi] < target or (lo > 0 and nums[lo] == nums[lo - 1]):
            lo += 1
        elif nums[lo] + nums[hi] >  target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
            hi -= 1
        else: 
            res.append([nums[lo], nums[hi]])
            lo += 1
            hi -= 1
             
    return res

res = twoSum(nums, 0)
print(res)
'''


'''
res = []
if res == []:
    print(1)

num = 1
listnum = [num]
list = []
list.append(listnum)
print(list, type(list))
print(num, type(num))
'''

'''
res = []
res1 = [[]]
res2 = [[],[]]

print(res)
print(len(res2))
# if res == NULL: print(1)  there is no NULL keyword in python.
if res1 == None: print(2)
if res2 == None: print(3)
'''

'''
numbers = [1,2,3,4,5]
print(sum(numbers))
print(sum(numbers[:4]))
'''

'''
# sets are unordered, so you cannot be sure in which order the items will appear.
nums = [1, 2, 3, 2, 5, 5, 6, 4, 7,]
thisset = {"apple", "banana", "cherry", "apple"}
# duplicated items will be ignored
print(thisset)
print(len(thisset))
set1 = set()
set1.add("apple")  # use .add() funvtion to add items to a set
set2 = set(("apple",))
print(set1, set2)
'''

'''
#def threeSum(self, nums: List[int]) -> List[List[int]]:
if len(nums) < 3:
    print([])
ans = set()
nums.sort()
for i, target in enumerate(nums):
    if i > 0 and target == nums[i -1]:
        continue
    prev = set()
    for j in range(i + 1,len(nums)):
        diff = -target - nums[j]
        if diff in prev:
            ans.add((target, nums[j], diff))
        prev.add(nums[j])

print(ans)
print(type(ans))
'''

'''
seen = {1:3, 2:4, 5:6, 6:7}
for i in seen:
    print(i)
'''

'''
nums = [1, 2, 3, 2, 5, 5, 6, 4, 7,]
target = 9
seen1 = {}
res = []

def twosumfunction(target2, i):
    seen2 = {}
    res = {}
    for j, num in enumerate(nums[i+1:]):
        if target2 - num in seen2:
            res.append([target2-num, num])
        elif num not in seen2:
            seen2[num] = j
    return res
    
for i, num in enumerate(nums):
    if target - num in seen1:
        res1 = twosumfunction(target-sum, i)
        for i in res1:
            res += i.append(num)
    if num not in seen1:
        seen1[num] = i 

print(res) 
'''

'''
res = []
seen = {}
for i, num in enumerate(nums[:-2]):
    if target - num in seen:
        # return([seen[target-num], i]
        res.append([target-num, num])
    elif num not in seen:
        seen[num] = i 
print(res)
'''

'''
a = [1,[1,2], 3, 4, 5, 5, 5]
if [2,1] in a: print(0)
'''

'''
a = "abs" * 5
print(a)
'''

'''
test = {}
print(type(test))

b = 2

a = b == 1
print(a)
'''


'''
for i in range(-20, -8):
    print(-i)
'''

'''
testdic = {
    'path': "aa",
    'path': "bb",
    'path': "cc"
}
for i, image in enumerate(testdic):
    print(i, testdic[image])
    print(type(testdic[image]))

print(type(testdic))
'''
'''
images=[                             # C:/Users/16591/Desktop/Github/LongtailDistribution/code/  test   /  angry.jpg
            {'path': 'C:/Users/16591/Desktop/Github/LongtailDistribution/code/test/angry.jpg'},
            {'path': 'C:/Users/16591/Desktop/Github/LongtailDistribution/code/test/happy.jpg'},
            {'path': 'C:/Users/16591/Desktop/Github/LongtailDistribution/code/test/sad.jpg'},
            {'path': 'C:/Users/16591/Desktop/Github/LongtailDistribution/code/test/surprised.jpg'},
        ]
print(type(images))

for i, image in enumerate(images):
    print(i, image)
    print(image['path'])
'''

'''


for image in enumerate(images):
    print(image['path'])
'''


'''
a = "4"
print(-int(a))
'''

'''
s = "   sd  sd  sdfafd "

print(s.strip())
'''
'''
a = [['1'], ['2'], ['3'], ['4']]
res = ""
res += '->'.join(a)
print(res)
'''
# use for loop to join a string list
'''
a = {"1", "2", "3"}
res = ""
res = 'a'.join(a)
print(res)

'''








'''
a = 5

if a == 5:
    a -= 2
elif a == 3:
    a = 10

print(a)
'''

'''
a = 5

b = [[] for i in range(a)]
print(b)
'''

'''
a = [1, 2, 3]
print(a[1:2])
'''

'''
nums1 = [1, 2]
nums2 = [3, 4]
for i in nums1:
    nums2.append(i)
nums2.sort()
print(nums2)   

k = len(nums2)
if k%2 == 0:
    print ((nums2[int(k/2) - 1] + nums2[k//2])/2)
if k%2 == 1:
    print (nums2[k//2]/2)
'''

'''
a = [1, 3, 5, 4, 6, 6, 8]
a.sort()
print(a)

b = [1, 3, 4, 5, 6, 2, 2 ,2]           # you can't use sort function like this
c = b.sort()                        # b.sort() is not a list, it just an option to make
print(c)
'''


# TreeNode function:
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node], 
            self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1 :])
        )
'''



'''     # while x has not been assigned a specific value, the code 'x = y' just pass the address of y to x.
        # and then if we give a value to x (the addres of y), the value of y will also be changed.
y = [1, 2, 3]
x = y
x = [1, 7, 7]
m = 0
while m<3:
    x[m] = 6
    m += 1

print(x)
print(y)

'''

'''
splitInput = input("input your integers one by one: ").split()
print(splitInput)
# the type of splitInput is "list"
'''

'''
guess = int(3)
print(int(guess/2))
'''


'''
a = [1, 2, 3, 4, 5]
print(a[2: 4])
'''

'''
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
'''

'''
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

z = ListNode(5, )
k = ListNode(3, z)
M = ListNode(5, k)
j = ListNode(8, M)

fast = [j, M, k, z]
print(fast)
x = 0
while fast and x < 3:
    fast = fast.next      # here is the problem
    x += 1
print(fast)
'''


'''
if True:
    print(10)
if False:
    {}
else: print(1)
'''

'''
s = '222'   
for i in s:
    print(i) 
'''


'''
p = ["ss", 'ss', "sss"]
p.append("m")
print(p)
'''
'''
string = ""
string = string + "s"
print(string)
'''

'''
seen = {}  # dictionary is a collection which is ordered, changable and do not allow duplicates
seen = {1:"janan", "name": "Zhu"}
print(seen)
print(seen["name"])
print(len(seen))
print(type(seen))
print(type(3))

x = seen.keys()  
print(type(x))           # type of keys: dict_keys
seen["name"] = "Zyu"
print(x)

# add a new item to the list:
seen["color"] = "red"
print(seen)
if "name" in seen:
    print("you have learn the basic of python dictionary")
'''

'''
def return65():
    return 65

return65()
print(return65())
'''

'''
def testreturn(x: int):
    if x == 1 :
        return(True)

testreturn(int(input("enter your integer: ")))
'''

'''
for i in range(int(1.6)):
    print("test")
'''
'''
print(2//2)     # // is floor division in python
x = 2
x ^= 3
x >>= 3
# operator in python:
x is y
x is not y
# and or not
x in y
x not in y
'''
'''
tuple = (1, 2, 3, 45, 5)
print(tuple.index(3))
print(tuple.count(1))
# .append(one value)
# .extend(one list)
'''






"""
x = int(2.3)
print(x)
while x:
    print(1)
    x = x - 1
while int(2.3):                       # return can only used within a function
"""


# global variable
"""
x = "awesome"
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is: "+ x)
"""


'''
x = str(3)             # x will be '3'
y = int(3)             # y will be 3
z = float(3)           # z will be 3.0
print(type(z))
'''

# test input
'''
lst = []
n = int(input("Enter your number of elements: "))       # the default input type is character, to get a integer, you need add an int()
for i in range(0, n):
    ele=[input(), int(input())]
    lst.append(ele)
print(lst)
'''
# better one 
'''
lst1 = []
lst2 = []
lst1 = [item for item in input("enter your list item: ").split()]
lst2 = [int(item) for item in input("enter your list item: ").split()]
print(lst1)
print(lst2)
'''

# lambda function
# lambda is a small anonymous function:
# it has a form like this:
# lambda arguments : expression
# it can have many numbers of arguments, but only one expression
'''
x = lambda a : a + 3
print(x(2))
y = lambda a, b : a + b
print(y(1, 1))
def myfunc(n):
    return lambda a : a*n
mytripler = myfunc(3)
print(mytripler(10))
'''

# map function
# map(function, iterator)
# the iterator can be a tuple, which consisted of multiple items
'''
def double(x):
    return x + x;

numberlist = (1, 2, 3, 4)
result = map(double, numberlist)  
print(list(result))                   # list() converts a tuple to a list

tuple = (1, 'aa')
print(list(tuple))             # a list can also consists of  string and number

numbers = (1, 2, 3, 4)
result = map(lambda x: 2*x, numbers)
print(list(result))
'''
'''
number1 = (1, 2, 3, 4)
number2 = (9, 2, 3 ,4)
result = map(lambda x, y : x + y, number1, number2)
print(list(result))
relist = list('abc')             # list can convert a string or tuple into a list 
print(relist)
l = ['aaa', 'bbb', 'ccc']
test = list(map(list, l))
print(test)
'''

# getting an input of a list (third method)
'''
n = int(input("enter the number of elements of your list: "))
a = list(map(int, (input("\nenter your numbers: ").strip().split())))[:n]
print(a)
'''
'''
x = '3'
print("hello:" + x)
'''
# what is [:n] in python?
'''
txt = "hello, world!"
x1 = txt[2:]
x2 = txt[:2]
x3 = txt[:-2]
x4 = txt[2:-2]
print(f"{x1}\n{x2}\n{x3}\n{x4}")
'''
'''
txt = "welcome to janan's workplace"
x = txt.split()           # def:     .split(delimiter, max number of the delimiter)
print(x)
phase = "hello everyone, my name is Janan Zyu"
y = phase.split(",")
print(y)
z = phase.split(" ",3)
print(z)
'''

# strip     # remove character 
'''
text = "   welcome to china   "
print(text)
print(len(text))
print(text.strip())     # default is to remove the begining and trailing space of a character  
text1 = "welcome to china"         # you can set to remove some characters in the begining and trailing
print(text1.strip())
txt1 = "hello, janan, welcome to our community"
print(txt1.strip("h,eloyt "))

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)
'''

# test int
# if the value inside 'int' is not an integer, then there will be an error
'''
k = int(input("enter your number: "))
print(k)
'''


# getting an input of a list (another method)
'''
try:
    mylist = []
    while True:
        mylist.append(int(input()))  # if input is not an integer, then the append int is False, then goto except.
except:
    print(mylist)
'''

# getting  an input of a list 
'''
mylist = []
inlist = int(input("Enter number of elements: "))
for i in range(0, inlist):
    ele = int(input())          # here enter your content of the list
    mylist.append(ele)
print(mylist)
'''

# getting input 
'''
name = input("Enter your name:")
print("Your name is: " + name)
print("Your name is: ", name)
'''


# class deploy
'''
class Myclass:
    name = 'Janan Zyu'

p1 = Myclass()
print(p1.name)
'''