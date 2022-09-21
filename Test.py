
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

n = int(input("enter the number of elements of your list: "))





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