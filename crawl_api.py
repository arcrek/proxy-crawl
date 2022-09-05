#Simple run this file by call function crawl_r()

import requests
from data import *

def crawl_api_main():
  http = []
  socks4 = []
  socks5 = []

  for i in http_api:
    res = requests.get(i)
    http.append(res.text)

  for i in socks4_api:
    res = requests.get(i)
    socks4.append(res.text)

  for i in socks5_api:
    res = requests.get(i)
    socks5.append(res.text)

  with open("crawl_data/http_api.txt", 'w', encoding='utf8') as f:
    f.write(''.join(http))

  with open('crawl_data/socks4_api.txt', 'w', encoding='utf8') as f:
    f.write(''.join(socks4))

  with open('crawl_data/socks5_api.txt', 'w', encoding='utf8') as f:
    f.write(''.join(socks5))

# crawl_api_main()