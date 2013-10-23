def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results

def get_Case(content,n):
    case = []
    add = 0 
    for i in range(1,n+1):
        tmp=int(content[i+add])
        add+=tmp
    for j in range(add-tmp+n+1, add+n+1):
        case.append(list(map(int,content[j].replace('\n','').split(' '))))
    return case

def specialCount(case):
    return len(case)-1

def intrCount(case):
    count = 0
    for i in range(len(case)-1):
        for j in range(i+1,len(case)):
            tmp1 = case[i][0]-case[j][0]
            tmp2 = case[i][1]-case[j][1]
            if tmp1*tmp2 <0:
                count +=1
    return count
                
        

def run(content, size):
    out_f =open('RopeIntr'+size+'output.txt','w', encoding='utf-8')
    #open('C:\Users\mc31141\Desktop\miscellanea'+size+'output.txt','w',encoding='utf-8')

    for i in range(1,int(content[0])+1):
        case = get_Case(content,i)
        if len(case)==1:
            result = "Case #"+str(i)+": "+str(specialCount(case))
        else:
            result = "Case #"+str(i)+": "+str(intrCount(case))
        #print (results)
        out_f.write(result+'\n')


content = read_in('RopeIntr_Small.in')
run(content,'Small')

content1 = read_in('RopeIntr_Large.in')
run(content1,'Large')
