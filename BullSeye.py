import math
from decimal import *

def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results

def get_Case(content,n):
    case = [int(x) for x in content[n].replace('\n','').split(' ')]
    return case

content = read_in('BullSeye_Small.in')
case = get_Case(content, 1)

    
def Draw(case):
    i = 1
    r = case[0]
    paint = case[1]
    a = 0.5
    b = 0.5+r
    c = r-paint
    d = b**2-4*a*c
    sol = int((-b + math.sqrt(d)) / (2 * a))
    if sol %2 == 0:
        #circle = (sol-1)/2
        circle = max(1,sol/2)
    else:
        #circle = sol/2
        circle = max(1,(sol+1)/2)
    #print ('Sol is',sol,'Circle is', circle)
    return int(circle)
    
def run(content, size):
    out_f =open('BullSeye'+size+'output1.txt','w', encoding='utf-8')

    #out_f =open('BullSeye'+size+'output.txt','w', encoding='utf-8')

    for i in range(1,int(content[0])+1):
        case = get_Case(content,i)
        results = "Case #"+str(i)+": "+str(Draw(case))
        #print (results)
        out_f.write(results+'\n')

def run1(content,size):
    out_f =open('BullSeye'+size+'output2.txt','w', encoding='utf-8')

    #out_f =open('BullSeye'+size+'output.txt','w', encoding='utf-8')

    for i in range(1,int(content[0])+1):
        case = get_Case(content,i)
        r = int(case[0])
        t = int(case[1])
        
        lo = 0
        hi = 10000000000
        while hi > lo + 1:
            mid = (lo + hi) // 2
            if 2*r*mid + (2*mid-1)*mid <= t:
                lo = mid
            else:
                hi = mid
        results = "Case #"+str(i)+": "+str(lo)
        #print (results)
        out_f.write(results+'\n')
    
content = read_in('BullSeye_Small.in')    
run(content, "Small")
run1(content, "Small")

content1 = read_in('BullSeye_Large.in')
#run(content1, "Large")
run1(content1, "Large")

