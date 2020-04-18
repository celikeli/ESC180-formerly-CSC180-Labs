import random

def genBoard():
    list = [0,0,0,0,0,0,0,0,0]
    return list

def printBoard(T):
    list = [0,0,0,0,0,0,0,0,0]
    i=0
    while i<=8:
        if T[i]==0:
            list[i]=i
            i=i+1
        elif T[i]==1:
            list[i]='X'
            i=i+1
        elif T[i]==2:
            list[i]='O'
            i=i+1
        else:
            return False

    if len(T)==9:
        print( ' '+str(list[0]) + ' | ' + str(list[1]) + ' | ' + str(list[2]) + \
        '\n---|---|---\n ' + str(list[3]) + ' | ' + str(list[4]) + ' | ' + \
        str(list[5]) +'\n---|---|---\n '+str(list[6]) + ' | ' + str(list[7]) + \
        ' | ' + str(list[8]))
    else:
        return False

    return True

def analyzeBoard(T):
    for entry in T:
        if not (entry==0 or entry==1 or entry==2):
            return -1
        if not len(T)==9:
           return -1
    xwins = (T[0]==T[3]==T[6]==1) or (T[0]==T[4]==T[8]==1) or \
        (T[2]==T[4]==T[6]==1) or (T[2]==T[5]==T[8]==1) or \
        (T[1]==T[4]==T[7]==1) or (T[0]==T[1]==T[2]==1) or \
        (T[3]==T[4]==T[5]==1) or (T[6]==T[7]==T[8]==1)
    owins = (T[0]==T[3]==T[6]==2) or (T[0]==T[4]==T[8]==2) or \
        (T[2]==T[4]==T[6]==2) or (T[2]==T[5]==T[8]==2) or \
        (T[1]==T[4]==T[7]==2) or (T[0]==T[1]==T[2]==2) or \
        (T[3]==T[4]==T[5]==2) or (T[6]==T[7]==T[8]==2)


    if xwins:
        return 1
    elif owins:
        return 2
    for entry in T:
        if entry==0:
            return 0
    else:
        return 3
 def genWinningMove(T,player):
    list2 = T
    j=0
    while j<=8:
        if (list2[j]==0):
            if player==1:
                list2[j]=1
                state2 =analyzeBoard(list2)
                if state2==1:
                    return j
                else:
                    list2[j]=0
                    j=j+1

            elif player==2:
                list2[j]=2
                state2 =analyzeBoard(list2)
                if state2==2:
                    return j
                else:
                    list2[j]=0
                    j=j+1
            else:
                return -1
        elif (list2[j]==1 or list2[j]==2):
            j=j+1

        else:
            return -1

    return -1
def genRandomMove(T,player):
    list2=T
    number=random.randint(0,8)
    if list2[number]==0:
        return number
    else:
        return -1

def genOpenMove(T,player):
    list2=T
    k=0
    while k<=8:
        if list2[k]==0:
            return k
        elif (list2[k]==1) or (list2[k]==2):
            k=k+1
        else:
            return -1
    return -1
