# https://leetcode.com/problems/1-bit-and-2-bit-characters/

class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        while(i < len(bits)):
            if bits[i] == 0:
                if i == len(bits) - 1:
                    return True
                i += 1
            else:
                i += 2
        return False