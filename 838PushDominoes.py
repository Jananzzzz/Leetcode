# return can only be used within a funcion

dominoes = ".L.R...LR..L.."
dominoes1 = list(dominoes)

k = [0, '.']
for i in range(len(dominoes1)):
    if dominoes1[i] == 'L':
        if k[1] == 'L' or k[1] == '.':
            for j in range(k[0], i):
                dominoes1[j] = 'L'
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
        k = [i, 'R']

dominoes = "".join(dominoes1)
print(dominoes)
print(type(dominoes))
