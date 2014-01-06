
def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results


#test = content[0:3]

def get_Case(content,n):
    case = content[n].replace('\n','').split(' ')
    return case
#test1 = get_Case(content, 2)


def same_lenEncode(source, target, alien_number):
    output = ""
    for n in alien_number:
        output = output+target[source.find(n)]
    return output

def convert(source, target, alien_number):
    number = 0
    srclen= len(source)
    tglen = len(target)
    alen= len(alien_number)
    i = 1
    for n in alien_number:
        power = alen-i
        number = int(number+source.find(n)*srclen**power)
        i+=1
        #print (number)
        #print (power)
    res = ""
    while number:
        res = target[number%tglen]+res
        number //=tglen
    return res
    #print (res)

def run(content,size):
    out_f =open('Alien'+size+'output.txt','w', encoding='utf-8')
    #open('C:\Users\mc31141\Desktop\miscellanea'+size+'output.txt','w',encoding='utf-8')

    for i in range(1,int(content[0])+1):
        case = get_Case(content,i)
        source = case[1]
        target = case[2]
        alien_number = case[0]
        result = "Case #"+str(i)+": "
        if len(source)== len(target):
            results = result + same_lenEncode(source, target, alien_number)
        else:
            results = result +convert(source, target, alien_number)
        #print (results)
        out_f.write(results+'\n')
def sol(src,trg,num):
    n = 0
    for c in num:
        n=n*len(src)+src.find(c)
    res = ""
    while n:
        res = trg[n%len(trg)] + res
        n/=len(trg)
    return res
def run1():
    out_f =open('Alien'+size+'output1.txt','w', encoding='utf-8')
    #open('C:\Users\mc31141\Desktop\miscellanea'+size+'output.txt','w',encoding='utf-8')

    for i in range(1,int(content[0])+1):
        case = get_Case(content,i)
        source = case[1]
        target = case[2]
        alien_number = case[0]
        result = "Case #"+str(i)+": "+sol(source,target, alien_number)
        #print (results)
        out_f.write(results+'\n')
        
content = read_in('Alien_Small.in')
content1 = read_in('Alien_Large.in')
run(content, 'small')
run(content1, 'large')
