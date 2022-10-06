def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    b = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' '}
    
    res = []
    for i in digits:
        if res == []:
            res = b[i]
        else:
            newlist = []
            for j in res:
                for x in b[i]:
                    newlist.append(j+x)
            res = newlist
                
    return res
