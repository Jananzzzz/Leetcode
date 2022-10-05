# binary to decimal: a = 11011
'''
a = format(int(input("enter your number: "), 2), "b")
print(a)
print(type(a))
print(int(a))
print(type(int(a)))
inta = int(a)

'''
ans = 0
a = format(int(input("enter your binary number: "), 2), "b")
for i in range(1, len(a) + 1):
    ans += int(a[-i]) * (2 ** (i - 1))
print(ans)
    

# input: 12
# output: 1100

# decimal to binary
'''
def decimalToBinary(n):
    global ans
    if (n > 1):
        decimalToBinary(n//2)
    ans = ans + str(n%2)
    

if __name__ == '__main__':
    ans = ''
    decimalToBinary(int(input("Enter your decimal number: ")))
    # transform ans to integer
    print(int(ans, 2))

'''












