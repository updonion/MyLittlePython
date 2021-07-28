import requests

alphabet = "pqrstuvwxyz"
betbet = "0123456789abcdefghijklmnopqrstuvwxyz"
f = open("free-github.txt", "a")

for a in alphabet:
    for b in betbet:
        page = requests.get('https://github.com/' + a + a + b + b)
        if page.text == 'Not Found':
            print(a + a + b + b)
            f.write(a + a + b + b + "\n")
f.close()
