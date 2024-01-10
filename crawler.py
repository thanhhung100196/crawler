# crawler.py
from selenium import webdriver

def crawl(url):
    driver = webdriver.Chrome()
    driver.get(url)
    # Extract data from the web page
    driver.quit()