# return can only be used within a funcion

# a beautiful solution:
class Solution:         # States for the dominoes:
                        #   • Any triplet that reaches the state 'R.L' remains
                        #     that state permanently.
                        #  
                        #   • These changes occur to pairs that are not part of an 'R.L':
                        #     'R.' --> 'RR', .L' --> 'LL'

                        #  Here's the plan:
                        #    1) To avoid the problem with the 'R.L' state when we  address the 
						#       'R.' --> 'RR' and  '.L' --> 'LL' changes, we replace each 'R.L' 
						#.       with a dummy string (say, 'xxx').
                        #       
                        #    2) We perform the 'R.' --> 'RR', .L' --> 'LL' replacements.

                        #    3) Once the actions described in 1) and 2) are completed, we repeat 
                        #       until no changes occur. We replace the dummy string with 'R.L'. 
    def pushDominoes(self, dominoes: str) -> str:
        temp = ''
        
        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')       # <-- 1)
            dominoes = dominoes.replace('R.', 'RR')         # <-- 2)
            dominoes = dominoes.replace('.L', 'LL')         # <-- 2)

        return  dominoes.replace('xxx', 'R.L')              # <-- 3)


# i'm dying here: ^^
'''
dominoes = ".L.R...LR..L.."
dominoes1 = list(dominoes)

k = [0, '.']
for i in range(len(dominoes1)):
    if dominoes1[i] == 'L':
        if k[1] == 'L' or k[1] == '.':
            for j in range(k[0], i):
                dominoes1[j] = 'L'
                k = [i, 'L']
        if k[1] == 'R':
            if (i-k[0])%2 == 1:
                for j in range(int(k[0]), int(k[0]+(i-k[0]-1)/2+1)):
                    dominoes1[j] = 'R'
                for j in range(int(k[0]+(i-k[0]-1)/2+1), i):
                    dominoes1[j] = 'L'
            if (i-k[0])%2 == 0 and (i-k[0])>0 :
                for j in range(int(k[0]), int(k[0]+(i-k[0])/2)):
                    dominoes1[j] = 'R'
                for j in range(int(k[0]+(i-k[0])/2+1), i):
                    dominoes1[j] = 'L'
                dominoes1[int(k[0]+(i-k[0])/2)] = '.'
            k = [i, 'L']
    if dominoes1[i] == 'R':
        for i in range(i, len(dominoes1)):
            if dominoes1[i] == '.':
                dominoes[i] = 'R'
            else:
                k = [i, 'R']

dominoes = "".join(dominoes1)

print(dominoes)

'''
