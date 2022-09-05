from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from data import *

def openproxy_crawl():

  PATH = "/bin/chromedriver"
  
  chrome_options = Options()
  chrome_options.add_argument("--disable-gpu")
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--no-sandbox")

  openproxyHttp = []
  openproxySocks4 = []
  openproxySocks5 = []

  for i in openproxy_http:
    driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
    driver.get(i)
    openproxyHttp.append(driver.find_element(By.CLASS_NAME, 'text-input').text)
    with open('crawl_data/openproxy_http.txt', 'w', encoding='utf8') as f:
      f.write(''.join(openproxyHttp))
    driver.quit()

  for i in openproxy_socks4:
    driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
    driver.get(i)
    openproxySocks4.append(driver.find_element(By.CLASS_NAME, 'text-input').text)
    with open('crawl_data/openproxy_socks4.txt', 'w', encoding='utf8') as f:
      f.write(''.join(openproxySocks4))
    driver.quit()

  for i in openproxy_socks5:
    driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
    driver.get(i)
    openproxySocks5.append(driver.find_element(By.CLASS_NAME, 'text-input').text)
    with open('crawl_data/openproxy_socks5.txt', 'w', encoding='utf8') as f:
      f.write(''.join(openproxySocks5))
    driver.quit()

# openproxy_crawl()
