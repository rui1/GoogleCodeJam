import string
letter_count = dict(zip(string.ascii_lowercase, [0]*26))


def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results

def get_Case(content,n):
    case = content[n].replace('\n','')
    return case
content = read_in('SpeakTong_Small.in')

results=['our language is impossible to understand',
         'there are twenty six factorial possibilities',
         'so it is okay if you want to just give up']

gtong= ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
        'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
        'de kr kd eoya kw aej tysr re ujdr lkgc jv']
lookUp = dict()
for i in range(len(results)):
    eng = results[i]
    goo = gtong[i]
    for j in goo:
        if not(j in lookUp):
            lookUp[str(j)]= eng[goo.index(j)]
          
        
lookUp['q'] = 'z'
lookUp['z'] = 'q'

def translate(case):
    eng = ''
    for i in case:
        eng += lookUp[i]
    return eng
        

def run(content, size):
    out_f =open('SpeakTong'+size+'output.txt','w', encoding='utf-8')
    #open('C:\Users\mc31141\Desktop\miscellanea'+size+'output.txt','w',encoding='utf-8')

    for i in range(1,int(content[0])+1):
        case = get_Case(content,i)
        result = "Case #"+str(i)+": "+translate(case)
        #print (results)
        out_f.write(result+'\n')  

run(content,'Small')
