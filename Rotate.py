def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results
def get_Case(content, n):
    case = []
    add = 0
    for i in range(1,n+1):
        tmp = int(content[i+add].replace('\n','').split(' ')[0])
        #print('current read in is',content[i+add][0])
        #print('current read in length is',len(content[i+add]))
        #print('current read in is',content[i+add][0:2])
        #print('current read in is',content[i+add])
        #print('tmp is',tmp)
        add+=tmp
        #print('add is',add)
        
        
    case.append(list(map(int,content[add-tmp+n].replace('\n','').split(' '))))
    for j in range(add-tmp+n+1,add+n+1):
        case.append(list(content[j].replace('\n','')))
    return case

def RotGrav(case_org):
    if debug:
        print('Original case are',case_org)
    n = case_org[0][0]
    for l in range(1,n+1):
        dots = []
        if debug:
            print('Current case is',case_org)
        for v in range(n):
            if case_org[l][v]!='.':
                dots+=case_org[l][v]
                case_org[l][v]='.'
        if debug:
            print('Current dots is',dots)
        for k in range(0,len(dots)):
            case_org[l][n-len(dots)+k]=dots[k]
    return case_org

def win(case):
    blue = False
    red = False
    n =case[0][0]
    tg = case[0][1]
    tests = case[1:]
    for i in range(n):
        s = ''.join(tests[i])
        if'B'*tg in s:
            blue = True
        if 'R'*tg in s:
            red = True
        s = ''.join(tests[j][i]for j in range(n))
        if'B'*tg in s:
            blue = True
        if 'R'*tg in s:
            red = True
        j = 0
        s = ''.join(tests[i+d][j+d] for d in range(n-i))
        if'B'*tg in s:
            blue = True
        if 'R'*tg in s:
            red = True
        s = ''.join(tests[j+d][i+d] for d in range(n-i))
        if'B'*tg in s:
            blue = True
        if 'R'*tg in s:
            red = True
        s = ''.join(tests[i+d][n-d-1] for d in range(n-i))
        if'B'*tg in s:
            blue = True
        if 'R'*tg in s:
            red = True
        s = ''.join(tests[j+d][i-d] for d in range(i+1))
        if'B'*tg in s:
            blue = True
        if 'R'*tg in s:
            red = True
    if blue and red:
        return 'Both'
    elif blue:
        return 'Blue'
    elif red:
        return 'Red'
    return 'Neither'

def run(content, size):
    out_f =open('Rotate'+size+'output.txt','w', encoding='utf-8')
    #open('C:\Users\mc31141\Desktop\miscellanea'+size+'output.txt','w',encoding='utf-8')

    for i in range(1,int(content[0])+1):
        case_org = get_Case(content,i)
        case = RotGrav(case_org)
        result = "Case #"+str(i)+": "+ win(case)
        #print (results)
        out_f.write(result+'\n')

debug = False   
content = read_in('Rotate_Small.in')
run(content,'Small')

content1 = read_in('Rotate_Large.in')
run(content1,'Large')



test = get_Case(content,5)
#debug = True  
#Total = RotGrav(test)
#win1 = Total[0]
#Red = Total[1]
#Blue = Total[2]

            


    
 
