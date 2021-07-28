from proxy_checker import ProxyChecker
import multiprocessing.dummy as mp

f = open("proxy.txt", 'r')
good = open("proxy_valid.txt", 'a')
lines = f.read().split('\n')
checker = ProxyChecker()

def chp(i):
    prx = checker.check_proxy(lines[i])
    if prx != False:
        print(lines[i], prx['anonymity'], "\nTimeout:", str(prx['timeout']), ("\nCountry:" + prx['country'] + "\n" if prx['country'] != '-' else '\n'))

p=mp.Pool(100)
p.map(chp,range(0,1000))
p.close()
p.join()
    
f.close()
