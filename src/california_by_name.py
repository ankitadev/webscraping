from selenium import webdriver
import collections
from selenium.common.exceptions import NoSuchElementException
import csv

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--disable-infobars")

browser = webdriver.Chrome(executable_path='../include/chromedriver', chrome_options=option)

for i in range(303928, 500000):
    try:
        print ('\n')


    except NoSuchElementException:
        print("No agent found with this number!!")
        continue