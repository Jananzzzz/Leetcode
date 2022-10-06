
class Solution:
    def intToRoman(self, num: int) -> str:
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = ""
        for i in range(len(integers)):
            if num < 0:
                break

            while num >= integers[i]:
                num -= integers[i]
                result += romans[i]

        return result
    
    
    # Error messages usually mean precisely what they say. So they must be read very carefully. 


# brute force method, if by case
'''
def intToRoman(self, num: int) -> str:
	result = ""

	if num >= 1000:
		times = num // 1000
		result += "M" * times
		num -= 1000 * times

	if num >= 900:
		result += "CM"
		num -= 900

	if num >= 500:
		result += "D"
		num -= 500

	if num >= 400:
		result += "CD"
		num -= 400

	if num >= 100:
		times = num // 100
		result += "C" * times
		num -= 100 * times

	if num >= 90:
		result += "XC"
		num -= 90

	if num >= 50:
		result += "L"
		num -= 50

	if num >= 40:
		result += "XL"
		num -= 40

	if num >= 10:
		times = num // 10
		result += "X" * times
		num -= 10 * times

	if num == 9:
		result += "IX"   
		num -= 9

	if num >= 5:
		result += "V"
		num -= 5

	if num == 4:
		result += "IV"
		num -= 4

	if num > 0:
		result += "I" * num

	return result
'''