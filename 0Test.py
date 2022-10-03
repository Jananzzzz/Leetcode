



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