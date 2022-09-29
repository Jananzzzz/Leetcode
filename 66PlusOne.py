digits = [9, 9, 9]
k = len(digits)
carry = 1
for i in range(1, len(digits)+1):
    if (digits[-i] + carry) >= 10:
        digits[-i] = (digits[-i]+carry) % 10
        carry = 1
    else:
        digits[-i] = (digits[-i]+carry) % 10
        carry = 0
    if i == len(digits) and carry == 1:
        digits = [1]
        for i in range(1, k+1):
            digits.append(0)
print(digits)
