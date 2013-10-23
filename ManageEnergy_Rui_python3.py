def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results




def get_Case(content,n):
    case = content[2*n-1:2*n+1]
    return case

def SpecialCase(E,v):
    return E* sum(v)
    

def others(E,R,N,v):
    #v = map(int, case[1].replace('\n','').split())
    nextbig = [-1]*N
    current = E
    for i in range(N):
        for j in range(i+1,N):
            if v[j] > v[i]:
                nextbig[i]= j
                break
    Gains = 0
    for i in range(N):
        if nextbig[i] == -1:
            Gains += v[i]*current
            current = min(E,R)
        else:
            available = E - R*(nextbig[i]-i)
            spend = max(0,min(current, current-available))
            Gains += v[i]*spend
            current = min(E, current- spend + R)
    return Gains

def run(content, size):
    out_f =open('ManageEnergy'+size+'output.txt','w', encoding='utf-8')
    for i in range(1,int(content[0])+1):
        case = get_Case(content,i)
        E, R, N = map(int, case[0].replace('\n','').split())
        v = [int(x) for x in case[1].replace('\n','').split()]
        result = "Case #"+str(i)+": "
        if E == R or N ==1:
            results = result + str(SpecialCase(E,v))
        else:
            results = result + str(others(E,R,N,v))
        #print (results)
        out_f.write(results+'\n')

content = read_in('ManageEnergy_Small.in')    
run(content, "Small")
content1 = read_in('ManageEnergy_Large.in')
run(content1, "Large")
