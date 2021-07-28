import grequests
from proxy_checker import ProxyChecker

f = open("proxy.txt", 'r')
good = open("proxy_valid.txt", 'a')
lines = f.read().split('\n')
checker = ProxyChecker()
# print(lines)
for i in lines:
    prx = checker.check_proxy(i)
    if prx != False:
        print(i, prx['anonymity'], "\nTimeout:", str(prx['timeout']), ("\nCountry:" + prx['country'] + "\n" if prx['country'] != '-' else '\n'))


f.close()
