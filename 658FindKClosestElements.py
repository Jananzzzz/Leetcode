# a = [1, 2, 3, 4, 5]
# k = 4
# x = 3
import time

# dichotomy

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        start = 0
        limit = len(arr) - k 

        while start < limit:
            medium = (start + limit)//2
            if x - arr[medium] <= arr[medium + k] -x:
                r = medium 
            else:
                l = medium + 1

        return arr[start: start + k]


# implementation of GuessNumber using dichotomy



def guessNumber():
  global low
  global high
  global medium
  medium = int((low + high)/2)
  print(f"your number is: {medium}, am i right?")
  reply = int(input())
  if reply == 0:
    return True
  if reply == 1:
    high = medium - 1
    return False
  if reply == -1:
    low = medium + 1
    return False
 

low = 0
high = 100
medium = 50
number = int(input("Enter your number(between 1 and 100): "))
print("After I made a guess, type '0' if I am right, type -1 for less than your number and 1 for big: ")
time.sleep(2)
print("Start guessing...")
time.sleep(0.5)
print("...")
time.sleep(0.5)
print("...")
time.sleep(0.5)
print("...")

while not guessNumber(): {}

print("Finally guess it!")