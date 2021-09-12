import requests, threading, os

url = input('Link > ')
amount = input('Threads > ')

def thread():
  while True:
     s = requests.session()
     proxy = set()
     with open("proxies.txt", "r") as f:
     file_lines1 = f.readlines()
     for line1 in file_lines1:
         proxy.add(line1.strip())
proxies = {
    'http': 'http://'+line1
    }

     sent = 0
     r = requests.get(url, proxies=proxies)
     if r.status_code == 403:
         print('Invalid URL/Proxy blocked')
     else:
      pass
      sent += 1
      print(f'%s requests have been sent' % sent)

for _ in range(int(amount)):
    t = threading.Thread(target=thread)
    t.start()
