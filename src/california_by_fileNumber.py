from selenium import webdriver
import collections
from selenium.common.exceptions import NoSuchElementException
import csv

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--disable-infobars")

browser = webdriver.Chrome(executable_path='../include/chromedriver', chrome_options=option)

for i in range(309694, 500000):
    try:
        print ('\n')
        business_url = "https://businesssearch.sos.ca.gov/CBS/SearchResults?SearchType=NUMBER&SearchCriteria=C0" + str(i) + "&SearchSubType=Exact"
        browser.get(business_url)

        #define all the id's in the browser
        titles_element = browser.find_element_by_xpath("//button[@name='EntityId']")
        titles_element.click()

        registration_key = browser.find_elements_by_xpath("//div[@class='col-sm-8 col-xs-6']")
        element1 = [x.text for x in registration_key]

        registration_element = browser.find_elements_by_xpath("//div[@class='col-sm-4 col-xs-6']")
        element2 = [x.text for x in registration_element]

        registration_name = browser.find_elements_by_xpath("// *[ @ id = 'maincontent'] / div[2] / div / h2")
        companyName = [x.text for x in registration_name]


        def convert(data):
            if isinstance(data, basestring):
                return str(data)
            elif isinstance(data, collections.Mapping):
                return dict(map(convert, data.iteritems()))
            elif isinstance(data, collections.Iterable):
                return type(data)(map(convert, data))
            else:
                return data

        comp = convert(companyName)
        for line in comp:
            Type = line.split("    ")
            x = Type[0]
            y = Type[1]
            print(x)
            print(y)
            mylist = [x, y]

        key = convert(element2)
        value = convert(element1)

        with open('california-state_22.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(mylist + value)
        csvfile.close()

    except NoSuchElementException:
        print("No agent found with this number!!")
        continue
