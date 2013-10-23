def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results

def get_Case(content,n):
    return content[n].replace('\n','')

def smallest(case):
    base = max(2,len(''.join(set(case))))
    baserange = list(range(base))
    l = len(case)
    output = 0
    lookUp = dict()
    output+= base**(l-1)
    lookUp[case[0]] = 1
    baserange.remove(1)
    count = 0
    for i in case[1:]:
        while(i not in lookUp):
            if case.index(i)==1:
                lookUp[i] = min(baserange)
            else:
                lookUp[i]= min(baserange)
            baserange.remove(lookUp[i])
        #print('i is',i,'output is',output,'case is',case)
        count +=1
        output+=lookUp[i]*base**(l - 1 - count)
        #print('add',lookUp[i]*base**(l - 1 - case.index(i)))
        #print('modified output is' ,output)
    #print('lookUp is',lookUp)
    return output

def codeJam(case):
    values = dict()
    values[case[0]] = 1
    for c in case:
        if c not in values:
            sz = len(values)
            if sz == 1:
                values[c] = 0
            else:
                values[c] = sz
    result = 0
    base = max(len(values), 2)
    for c in case:
        print('C is',c)
        result *= base
        print('result is',result)
        result += values[c]
        print('result is',result)
    return result
def run(coontent, size):
    out_f =open('AllYourBase'+size+'output.txt','w', encoding='utf-8')
    #open('C:\Users\mc31141\Desktop\miscellanea'+size+'output.txt','w',encoding='utf-8')

    for i in range(1,int(content[0])+1):
        case = get_Case(content,i)
        result = "Case #"+str(i)+": "+str(smallest(case))
        #print (results)
        out_f.write(result+'\n')   

content = read_in('AllYourBase_Small.in')
run(content,'small')

content = read_in('AllYourBase_Large.in')
run(content,'large')
test = get_Case(content , 1)

base = len(''.join(set(test)))
