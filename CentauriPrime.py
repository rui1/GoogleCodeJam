def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results

def get_Case(content,n):
    return content[n].replace('\n','')

def rule(case):
    consonants = "bcdfghjklmnpqrstvwxz"
    tmp= case.lower()
    word = tmp[len(case)-1]
    if word in consonants:
        return case+" is ruled by a king."
    elif word in "y":
        return case+" is ruled by nobody."
    else:
        return case+" is ruled by a queen."
        
    

def run(content, size):
    out_f =open('CentauriPrime'+size+'output.txt','w', encoding='utf-8')
    for i in range(1,int(content[0])+1):
        case = get_Case(content,i)
        result = "Case #"+str(i)+": "+rule(case)
        #print (results)
        out_f.write(result+'\n')

content = read_in("CentauriPrime_1.in")
run(content, "_1_")

content1 = read_in("CentauriPrime_2.in")
run(content1, "_2_")

case = get_Case(content, 1)
