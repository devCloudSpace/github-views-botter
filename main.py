from proxy_requests import ProxyRequests
import time
import os

url = input('URL > ')
reqcount = int(input('How many requests? > '))
uagent = 'Mozilla/4.0 (PSP; (PlayStation Portable); 2.60; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; InfoPath.2)'

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
