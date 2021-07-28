import requests
import random

url = "http://api.my-ip.io/ip"

proxies = {
    "https": "106.110.218.39:4216"
}

f = open("proxy.txt", 'r') # your proxy list
good = open("proxy_valid.txt", 'a')
lines = f.read().split('\n')
print(lines)
for i in lines:
    try:
        proxy = {"https": i}
        r = requests.get(url, proxies=proxy, timeout=1) # timeout 1 second
        print(r.text)
        good.write(i + "\n")
    except:
        print(i, "is bad")


f.close()
