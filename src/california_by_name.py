from selenium import webdriver
import collections
from selenium.common.exceptions import NoSuchElementException
import csv
import pdb

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--disable-infobars")

browser = webdriver.Chrome(executable_path='../include/chromedriver', chrome_options=option)

myNameArray = open("california_names.txt").readlines()
myAddressArray = open("california_address.txt").readlines()

for item in myNameArray:
    try:
        print ('\n')
        business_url = "https://businesssearch.sos.ca.gov/CBS/SearchResults?SearchType=CORP&SearchCriteria=" + item + "&SearchSubType=Keyword"
        browser.get(business_url)

        # define all the id's in the browser
        #titles_element = browser.find_element_by_xpath("//button[@name='EntityId']")
        #titles_element.click()

        pdb.set_trace()

        #compare the address with our data
        #titles_address = browser.find_element_by_xpath('//*[@id="maincontent"]/div[8]/div[2]/label[1]')

        #if titles_address.startswith(myAddressArray, 0, len(myAddressArray)):

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

        with open('california-TEST_SECOND_ROUND.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(mylist + value)
        csvfile.close()

    except NoSuchElementException:
        print("No agent found with this number!!")
        continue