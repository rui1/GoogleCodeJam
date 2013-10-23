import re
def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results

def get_Case(content,n):
    D = int(content[0].replace('\n','').split(' ')[1])
    case = content[D+n].replace('\n','').replace('(','[').replace(')',']')
    return case

def get_Dict(content):
    D = int(content[0].replace('\n','').split(' ')[1])
    Dict = []
    for i in range(1,D+1):
        word = content[i].replace('\n','')
        Dict.append(word)
    return Dict

content = read_in('AlienLang_Small.in')


def existCount(case,Dict):
    search = re.compile(case).search
    a = list(filter(search,Dict))
    return len(a)
    
def run(content, size):
    out_f =open('AlienLang'+size+'output.txt','w', encoding='utf-8')
    #open('C:\Users\mc31141\Desktop\miscellanea'+size+'output.txt','w',encoding='utf-8')
    N = int(content[0].replace('\n','').split(' ')[2])

    for i in range(1,N+1):
        case = get_Case(content,i)
        Dict = get_Dict(content)
        result = "Case #"+str(i)+": "+str(existCount(case, Dict))
        #print (results)
        out_f.write(result+'\n')
    

content = read_in('AlienLang_Small.in')
content1 = read_in('AlienLang_Large.in')
run(content, 'small')
run(content1, 'large')
