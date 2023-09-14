# https://leetcode.com/problems/image-smoother/description/
# python don't have a multi-line comment sign
# """this is just a long string"""

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        depth = len(img)
        width = len(img[0])
        new_img = [[0 for _ in range(width)] for i in range(depth)]
        for i in range(depth):
            for j in range(width):
                count = 1
                total = img[i][j]
                try:
                    if i > 0:
                        total += img[i-1][j]
                        count += 1
                except:
                    pass
                try:
                    total += img[i+1][j]
                    count += 1
                except:
                    pass
                try:
                    if j > 0:
                        total += img[i][j-1]
                        count += 1
                except:
                    pass
                try:
                    total += img[i][j+1]
                    count += 1
                except:
                    pass
                try:
                    if i>0 and j>0:
                        total += img[i-1][j-1]
                        count += 1
                except:
                    pass
                try:
                    if i > 0:
                        total += img[i-1][j+1]
                        count += 1
                except:
                    pass
                try:
                    if j > 0:
                        total += img[i+1][j-1]
                        count += 1
                except:
                    pass
                try:
                    total += img[i+1][j+1]
                    count += 1
                except:
                    pass
                total //= count
                new_img[i][j] = total
        return new_img



        