import calendar
from datetime import date
from dateutil.relativedelta import relativedelta  
import urllib.request

s = r"In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.[1] The method is named after Julius Caesar, who used it in his private correspondence."
s = s.split(" ")
print("len:",len(s))
res = []
i=0

today = date.today()
#today = date.today() - relativedelta(days=3)


while len(res)<=15:
    num = (i+len(s))
    print(num)
    res.append(num)
    i+=today.day # use date

print(res)
r=""
#calendar.day_name("24","20","10")

for x in res:
    r=""
    for c in range(today.year,1999,-1):
        wn = today - relativedelta(years=c%2000)
        i=97+(x+wn.weekday())%26
        r+=chr(i)

    url= "https://www."+r+".com"
    print(url)
    #with urllib.request.urlopen(url) as response:
    #    html = response.read().decode('utf-8')
    #    print(html)    
    print(r)

