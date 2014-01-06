def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results
def get_Case(content,n):
    return list(content[n].replace('\n','').split(' '))
content = read_in("Bot_Trust_Small.in")

def move(case):
    n = case[0]
    buttons = case[1:]
    time_B= 0
    time_O= 0
    for i in range(len(buttons)):
        if buttons[i] == "B":
            i+=1
            time_B+= int(buttons[i])
        elif buttons[i] == "O":
            i+=1
            time_O+=int(buttons[i])
        i+=1
        print("time_B is",time_B)
        print("time_O is",time_O)
            
