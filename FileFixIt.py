import re

def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results

def get_Case(content,n):
    case = []
    add = 0 
    for i in range(1,n+1):
        tmp=sum(list(map(int,content[i+add].replace('\n','').split(' '))))
        add+=tmp
    case.append(list(map(int,content[add-tmp+n].replace('\n','').split(' '))))
    for j in range(add-tmp+n+1, add+n+1):
        crnt = content[j].replace('\n','').split('/')
        crnt.remove('')
        case.append(crnt)
    return case

def getExist(case):
    n = case[0][0]
    ext = []
    for i in range(1,n+1):
        ext.append(case[i])
    return ext

def count(case, ext):
    n = case[0][0]
    tests = case[n+1:]
    count = 0
    for test in tests:
        minDiff = len(test)
        for word in ext:
            start = 1
            i = 0
            minI = min(len(word),len(test))
            #print ('minI',minI)
            #print('Word is', word)
            #print('test is', test)
            while( i < minI and word[i]==test[i]):
                i+=1
            #print('i is',i)
            diff = len(test)-i
            #print('Diff is', diff)
            if minDiff > diff:
                minDiff = diff
        count+=minDiff
        if minDiff != 0:
            ext.append(test)
            #print('now exist',ext)
            #print('count so far is', count)
    return count
    
    
def run(content, size):
    out_f =open('FileFixIt'+size+'output.txt','w', encoding='utf-8')
    #open('C:\Users\mc31141\Desktop\miscellanea'+size+'output.txt','w',encoding='utf-8')
    N = int(content[0].replace('\n','').split(' ')[0])

    for i in range(1,N+1):
        case = get_Case(content,i)
        ext = getExist(case)
        result = "Case #"+str(i)+": "+str(count(case,ext))
        #print (results)
        out_f.write(result+'\n')    
content = read_in('FileFixIt_Small.in')
#case = get_Case(content, 3)
#ext = getExist(case)
#count(case,ext)          
run(content, 'Small')

content = read_in('FileFixIt_Large.in')
run(content, 'Large')
