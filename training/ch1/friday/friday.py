"""
ID: 16881681
LANG: PYTHON3
TASK: friday
"""

def is_hundred_year(yr):
   return int(yr%100)==0
def is_leap_year(n):
   # is hundred year?
   if is_hundred_year(n):
      return n%400==0

   else:
      return n%4==0



with open('friday.in', mode='r', encoding='utf-8') as fin:
   N=int(fin.readline().strip())
   #n = map(int, fin.readline().split())
print(" N: ", N)
dt=0
curr_yr=1900
ii=0
stats=[0]*7
short_months=[4, 6, 9,11]

def calc_13_days(isLeapYear, dt, mo, stats):
   if mo==2:
      numOfDays = 29 if isLeapYear else 28
   else:
      numOfDays = 30 if mo in short_months else 31

   dt = (6 + dt - 1) % 7
   stats[(dt - 5) % 7] += 1
   remaining_days = numOfDays - 13 + 1 + 1
   return (remaining_days % 7 + dt - 1)


for ii in range(N):
   isLeapYear=is_leap_year(curr_yr+ii)
   for jj in range(1, 13):
      dt = calc_13_days(isLeapYear, dt, jj, stats)

with open('friday.out', mode='w', encoding='utf-8') as fout:
   o= " ".join(map(str, stats))
   fout.write(o+"\n")


print(" stats: ", stats)