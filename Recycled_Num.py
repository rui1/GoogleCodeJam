def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results
def get_Case(content,n):
    return list(map(int,content[n].replace('\n','').split(' ')))

def count(case):
    rng1 = case[0]
    rng2 = case[1]
    power = 10**(len(str(rng1))-1)
    cnt = 0
    #print("rng1 is", rng1, "rng2 is",rng2, "power is",power, "initial cnt",0)
    for i in range(rng1, rng2+1):
        tmp = i//10+(i%10)*power;
        #print("first tmp is",tmp,"current i is",i)
        while(tmp != i):
            if(tmp>i and tmp <= rng2):
                cnt +=1
                #print("count is",cnt,"tmp is",tmp)
            tmp1 = tmp//10+(tmp %10)*power
            tmp = tmp1
    return cnt

def run(filename,size):
    out_f =open('Recycled_Num'+size+'output.txt','w', encoding='utf-8')
    content = read_in(filename)
    caseN = get_Case(content,0)[0]
    for i in range(1,caseN+1):
        case = get_Case(content, i)
        result = "Case #"+str(i)+": "+str(count(case))
        out_f.write(result+'\n')

run("Recycled_Num_Small.in","small")
run("Recycled_Num_Large.in","large")
content = read_in("Recycled_Num_Small.in")
test = get_Case(content,1)
count(test)
