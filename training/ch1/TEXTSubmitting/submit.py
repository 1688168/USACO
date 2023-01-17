"""
ID: your_id_here
LANG: PYTHON2
TASK: test
"""
fin = open ('test.in', 'r')
fout = open ('test.out', 'w')
x,y = map(int, fin.readline().split())
sum = x+y
fout.write (str(sum) + '\n')
fout.close()



"""
with open('test.in', mode='r', encoding='utf-8') as fin:
    x,y = map(int, fin.readline().split())
with open('test.in', mode='r', encoding='utf-8') as fout:
    fout.write (str(sum) + '\n')
"""