def getDest(content, n):
    return content[n].replace('\n','').split()
debug = False
def minimumPath(FinalDest):
    x= int(FinalDest[0])
    y = int(FinalDest[1])
    tmpDest = abs(x)+abs(y)
    n = 0
    while ((n+1)*n/2 < tmpDest or ((n+1)*n/2-tmpDest)% 2 != 0):
        n +=1
        if debug == True:
            print 'current n is:'
            print n
    path = []
    revN = range(1,n+1)
    revN.reverse()
    if debug == True:
        print 'total N is:'
        print revN
    for i in revN:
        if abs(x)>abs(y):
            if x >0:
                x-=i
                path+='E'
            else:
                x+=i
                path+='W'
        else:
            if y >0:
                y-=i
                path+='N'
            else:
                y+=i
                path+='S'
        if debug == True:
            print 'Current i :'
            print i
            print 'Current path :'
            print path
    path.reverse()
    return path

def run(content, size):
    out_f = open('C:/Users/Rui/Desktop/ProgrammingAssign/code_jam/'+size+'output_Pogo.txt','w')
    for i in range(1,int(content[0])+1):
        out = 'Case #'+str(i)+':'+' '
        FinalDest = getDest(content, i)
        minPath = minimumPath(FinalDest)
        out+=''.join(minPath)
        out_f.write(out+'\n')
        print out

with open('C:/Users/Rui/Desktop/ProgrammingAssign/code_jam/Pogo-small-practice.in') as f :
    content = f.readlines()
run(content, 'small')

with open('C:/Users/Rui/Desktop/ProgrammingAssign/code_jam/Pogo-large-practice.in') as f1 :
    content1 = f1.readlines()
run(content1, 'large')           

