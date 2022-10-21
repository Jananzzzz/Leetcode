class Solution:
    def minimumSum(self, num: int) -> int:
        list = []
        s = str(num)
        for i in s:
            list.append(int(i))
        list.sort()
        return 10 * (list[0] + list[1]) + list[2] + list[3]