def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results
content = read_in('ManageEnergy_Small.in')
test = content[0:3]


def get_Case(content,n):
    case = content[2*n-1:2*n+1]
    return case

def SpecialCase(E,v):
    return E* sum(v)

        
E, R, N = map(int, case[0].replace('\n','').split())
v = list(map(int, case[1].replace('\n','').split()))
print ("E is ",E," R is ",R, "N is ",N)
print("v is ", v)

test1 = get_Case(content, 2)
rest = E

if E == R or N ==1:
    SepcialCase(E,v)
else:
    test(E,R,N,v)


def test(E,R,N,v):
    for i in range(N):
        for 
    Gains = 0
    
    return Gains
  

