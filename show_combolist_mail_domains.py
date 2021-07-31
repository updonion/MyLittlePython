import re
import collections

file = input("Combolist: ")
of = open(file, 'r')

m = re.compile('[\w\d\-+_.]*@([\w\d\-.]*):.*')

x = m.findall(of.read())
y = collections.Counter(x)

print(y)
for i in sorted(y, key=y.get, reverse=False):
    print("\r", i, "\t\t", y[i])
    # if y[i] >= 100:
    #     print(i, "\t", y[i])
