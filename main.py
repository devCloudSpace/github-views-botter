from proxy_requests import ProxyRequests
import time
import os

url = input('URL > ')
reqcount = int(input('How many requests? > '))
uagent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'

print('Sending Requests, This May Take A While')
for i in range(reqcount):
    headers = {
        'User-agent': f'{uagent}',
    }
    r = ProxyRequests(url)
    r.set_headers(headers)
    r.get_with_headers()
    print(r.get_status_code())
    print(r.get_proxy_used())  
