# webscraping

Scraping the web using Selenium, Beautifulsoup and requests in python

## Required packages and drivers

### Selenium

The [selenium package](https://pypi.org/project/selenium/) is used to automate web browser interaction from Python.

`pip install -U selenium`

or

`pip install -r setup.py`

i.e touch setup.py with 'selenium' in it

### ChromeDriver

ChromeDriver lets you perform tasks in the browser

I have included ChromeDriver in the 'include' folder,
but if you want to create your own project download ChromeDriver and include your path in your code

### Virtualenv

`[sudo] pip install virtualenv`

## Project Setup

### Create a virtual environment

`virtualenv webscraping`

### Install the dependency into your virtualenv

`pip install -r setup.py`

The setup.py file should contain dependency 'selenium'

### Activate the virtualenv

`Source webscraping/bin/activate`

i.e source and the location of your activate file in the bin

## Other required packages
```
pip install pandas
pip install requests
pip install bs4
```
