from data import *

def merge_main():

  with open('proxy/http.txt', 'w', encoding='utf8') as outfile:
    for h in http_file:
      with open(h) as infile:
        for line in infile:
          outfile.write(line)

  with open('proxy/socks4.txt', 'w', encoding='utf8') as outfile:
    for h in socks4_file:
      with open(h) as infile:
        for line in infile:
          outfile.write(line)

  with open('proxy/socks5.txt', 'w', encoding='utf8') as outfile:
    for h in socks5_file:
      with open(h) as infile:
        for line in infile:
          outfile.write(line)

# merge_main()
