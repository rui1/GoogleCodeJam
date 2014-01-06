import math
import sys
from decimal import *

getcontext().rounding = ROUND_HALF_UP
getcontext().prec = 100
def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results

def revens(r):
	if r==0:
		return 0
	else:
		return (2*(r//2-1)+1)*((r//2-1)+1);

def rodds(r):
	if r==1:
		return 0
	else:
		return (r//2)*(2*(r//2)+1)

def proc(r,t):
	if r%2==0:
		ff= (Decimal(-3)+ Decimal(1+8*(revens(r)+t)).sqrt() ) /Decimal(4)
		rr = ff - Decimal(r//2)+Decimal(1)
	else:
		ff = (Decimal(-1)+ Decimal(1+8*(rodds(r)+t)).sqrt() ) /Decimal(4)
		rr = ff - Decimal(r//2)
	return rr

sys.stdin.readline()
case=1
out_f =open('BullSeye'+size+'output2.txt','w', encoding='utf-8')

for i in range(1,int(content[0])+1):
    case = get_Case(content,i)
    r = int(case[0])
    t = int(case[1])
    Results = "Case #"+str(i)+": "+str(proc(r,t))
    out_f.write(results+'\n')
