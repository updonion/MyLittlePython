import requests

alphabet = "pqrstuvwxyz"
betbet = "0123456789abcdefghijklmnopqrstuvwxyz"
f = open("free-github.txt", "a")
dict = open("dict.txt", "r")
words = dict.readlines()

# print(words)
for word in words:
    page = requests.get('https://github.com/' + word[:-1])
    if page.text == 'Not Found':
        
        print(word[:-1])


f.close()
