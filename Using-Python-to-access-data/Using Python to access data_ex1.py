import re
#x=open("regex_sum_1012006.txt") #sample file
#file=x.read()
#string=re.findall('[0-9]+',file)
#string=[int(i) for i in string]
#y=sum(string)
#print(y)

print( sum( [ int(i) for i in re.findall('[0-9]+',open("regex_sum_1012006.txt").read())]))
