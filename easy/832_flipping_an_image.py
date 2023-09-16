# https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            image[i] = [abs(k-1) for k in image[i]]
        return image



        