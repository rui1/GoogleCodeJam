import math, itertools
from itertools import permutations
from itertools import product

def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results

def get_Case(content,n):
    return list(map(int,content[n].replace('\n','').split(' ')))

def contains(number):
    ls = list(map(str,list(range(4,9))))
    for i in ls:
        if i in set(str(number)):
            return False
    return True
def get_List():
    tmp = list(range(3,50,2))
    print('digit list is',tmp)
    psbItem = [0,1,2,3]
    for k in tmp:
        psbItem +=[sum([n*(10**i) for i,n in enumerate(([x]+list(ys)+[z]+list(ys)[::-1]+[x]) if k%2
                                else ([x]+list(ys)+list(ys)[::-1]+[x]))])
            for x in range(1,3)
            for ys in itertools.product(range(2), repeat = k//2-1)
            for z in (list(range(3)))]
        #mn = 10**(k-1)+1
        #mx =2*(10**(k-1))+10**((k-1)//2)+2
        #print ('max is',mx,'min is',mn)
    return psbItem


def get_List_new():
    tmp = list(range(5,50,2))
    print('digit list is',tmp)
    psbItem = [0,1,2,3,101,111,121,202,212]
    for k in tmp:
        psbItem +=[sum([n*(10**i) for i,n in enumerate(([1]+list(ys)+[z]+list(ys)[::-1]+[1]) if k%2
                                else ([1]+list(ys)+list(ys)[::-1]+[1]))])
            for ys in itertools.product(range(2), repeat = k//2-1)
            for z in (list(range(3)))]
        psbItem +=[sum([n*(10**i) for i,n in enumerate(([2]+[0 for x in range(k//2-1)]+[z]+list(ys)[::-1]+[2]) if k%2
                                else ([1]+list(ys)+list(ys)[::-1]+[2]))])

            for z in (list(range(2)))]
        #mn = 10**(k-1)+1
        #mx =2*(10**(k-1))+10**((k-1)//2)+2
        #print ('max is',mx,'min is',mn)
    return psbItem

def get_List2(psbItem):
    tmp = list(map(str, psbItem))
    results = []
    for i in tmp:
        count_2 = i.count('2')
        count_1 = i.count('1')
        if count_2 == 1 and count_1 <= 5:
            results+= [int(i)]
        elif count_2 ==2 and count_1<=1:
            results+= [int(i)]
        elif count_2 ==0 and count_1<=9:
            results+= [int(i)]
    return results
            
        
        

def Root1(case):
    
    minRt = math.ceil(math.sqrt(case[0]))
    maxRt = int(math.sqrt(case[1]))
    #print('minmum root is',minRt,'maximum root is',maxRt)
    palRt = 0
    for number in range(minRt,maxRt+1):
        if contains(number) and sum(int(x)**2  for x in str(number))<=9:
            palRt+= 1
    '''for i in range(minRt, maxRt+1):
        if set(str(i)) in ['1','2','3']:
            palRt+=[i]'''
    return palRt


def Root(case):
    minRt = math.ceil(math.sqrt(case[0]))
    maxRt = int(math.sqrt(case[1]))
    #print('minmum root is',minRt,'maximum root is',maxRt)
    palRt = []
    for i in range(minRt, maxRt+1):
        if str(i)[0] in ['1','2','3']:
            palRt+=[i]
    return palRt
        
def pal(root):
    count =0
    for i in root:
        stri = str(i)
        if len(stri)%2 ==0 and i%11 ==0:
            count+=1
        elif len(stri)%2 != 0 and int(stri[::-1]) == i:
            count +=1
    return count

def run(content, size):
    out_f =open('FairSquare'+size+'output.txt','w', encoding='utf-8')
    #open('C:\Users\mc31141\Desktop\miscellanea'+size+'output.txt','w',encoding='utf-8')
    #out_f1 =open('FairSquare'+size+'output1.txt','w', encoding='utf-8')

    for i in range(1,int(content[0])+1):
        case = get_Case(content,i)
        #root = Root(case)
        result = "Case #"+str(i)+": "+str(pal(root))
        result1 = "Case #"+str(i)+": "+str(Root1(case))
        #print (results)
        out_f.write(result+'\n')
        out_f1.write(result1+'\n') 
            
content = read_in('FairSquare_small.in')
run(content, 'small')
#content1 = read_in('FairSquare_large1.in')
#run(content1, 'Large1')
#content2 = read_in('FairSquare_large2.in')
#run(content2, 'large2')
test = get_Case(content,1)
