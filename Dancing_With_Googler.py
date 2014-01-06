def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results
def get_Case(content,n):
    return list(map(int,content[n].replace('\n','').split(' ')))

def count(case):
    n = case[0]
    sup= case[1]
    least = case[2]
    scores = case[3:]
    count1 = 0
    count2 = 0
    for i in scores:
        tmp = i//3
        tmp1 = i /3
        if bug:
            print("tmp is",tmp)
        if tmp1 > least-1:
            count1+=1
            if bug:
                print("current count1 is",count1)
        elif tmp1 <= least-1 and tmp1 >=max(0,least-2+0.5) and count2<sup and tmp1 != 0:
            count2+=1
            if bug:
                print("current count2 is",count2)
    return count1+count2
def run(filename,size):
    out_f =open('DanceWGoogler'+size+'output.txt','w', encoding='utf-8')
    content = read_in(filename)
    caseN = get_Case(content,0)[0]
    for i in range(1,caseN+1):
        case = get_Case(content, i)
        result = "Case #"+str(i)+": "+str(count(case))
        out_f.write(result+'\n')
bug = False
run("Dancing_With_Googler_small.in","small")
run("Dancing_With_Googler_Large.in","large")   
#content = read_in("Dancing_With_Googler_small.in")
#case = get_Case(content, 10)

