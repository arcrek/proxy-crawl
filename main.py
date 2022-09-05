#This file call crawl_r() and crawl_l() at same time by using Thread

from crawl_api import crawl_api_main
from openproxy import openproxy_crawl
from merge import merge_main
from threading import Thread
import time

if __name__ == "__main__":
  Thread1 = Thread(target=crawl_api_main)
  Thread2 = Thread(target=openproxy_crawl)
  Thread1.start()
  Thread2.start()
  Thread1.join()
  print('Finish craw api')
  Thread2.join()
  print('Finish craw openproxy')
  time.sleep(60)
  Thread3 = Thread(target=merge_main())
  Thread3.start()
  Thread3.join()
  print('Finish merge')

  