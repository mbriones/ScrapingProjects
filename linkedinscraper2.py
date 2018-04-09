import csv
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import randrange
from parsel import Selector
import requests
from lxml import html
import os
import re
'''
---------------------------------------------------------
This function writes to csv excel file
---------------------------------------------------------
'''
def write_to_csv(filename,dict_array):
    myFile = open(filename, "w")
    with myFile:
        fieldnames = ['name', 'job description', 'company', 'school', 'location']
        writer = csv.DictWriter(myFile, fieldnames=fieldnames)
        writer.writeheader()
        for row in dict_array:
            writer.writerow(row)
'''
---------------------------------------------------------
This function validates field
---------------------------------------------------------
'''
def validate_field(field):
    if field:
        pass
    else:
        field = ''
    return field
def validate_button(button):
    if button is None:
        return -1
    else:
        return button
'''
------------------------------------------------------------------------
           ASK FOR EMAIL AND PASSWORD
------------------------------------------------------------------------
'''
user_email ="miguelabriones@gmail.com"
password ="outkst237"
'''
------------------------------------------------------------------------
            SELENIUM DRIVER STARTS
------------------------------------------------------------------------
'''
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com")
'''
------------------------------------------------------------------------
            SIGN IN
------------------------------------------------------------------------
'''
email_button = driver.find_element_by_xpath('//input[@id="login-email"]')
email_button.send_keys(user_email)
sleep(randrange(3,5))
pass_button = driver.find_element_by_xpath('//input[@id="login-password"]')
pass_button.send_keys(password)
sleep(randrange(3,5))
submit_button = driver.find_element_by_xpath('//input[@id="login-submit"]')
submit_button.click()
print("Log in...")
'''
-------------------------
LinkedIn Profiles Scraping
-------------------------
'''
dict_array=[]

dates = []
linkedin_urls = ["https://www.linkedin.com/in/victoriakythai/",
                 "https://www.linkedin.com/in/melinda-brown/"]

#with open('Links/cunylinks.csv') as csvDataFile:
#    csvReader = csv.reader(csvDataFile)
#    next(csvReader, None)
#    for row in csvReader:
#        dates.append(row[0])
#        linkedin_urls.append(row[1])

for linkedin_url in linkedin_urls:
    try:
        driver.get(linkedin_url)
    except Exception:
        continue
    sleep(3)
    sel = Selector(text=driver.page_source)
    try:
        menu_button = driver.find_element_by_xpath("//button[starts-with(@class,'pv-s-profile-actions__overflow-toggle')]")
        menu_button = validate_button(menu_button)
        if menu_button != -1:
            menu_button.click()
    except Exception:
        pass
    sleep(randrange(5, 10))
    name = sel.xpath("//h1[starts-with(@class,'pv-top-card-section__name')]/text()").extract_first()
    name = validate_field(name)
    job_description=sel.xpath("//h2[starts-with(@class,'pv-top-card-section__headline')]/text()").extract_first()
    job_description=validate_field(job_description)
    company = sel.xpath("//h3[starts-with(@class,'pv-top-card-section__company')]/text()").extract_first()
    company  =validate_field(company)
    school = sel.xpath("//h3[starts-with(@class,'pv-top-card-section__school')]/text()").extract_first()
    school  =validate_field(school)
    location = sel.xpath("//h3[starts-with(@class,'pv-top-card-section__location')]/text()").extract_first()
    location  =validate_field(location)

    dict_row={'name':name,'job description':job_description, 'company':company, 'school':school, 'location':location}
    dict_array.append(dict_row)
    sleep(randrange(5, 10))
write_to_csv("results.csv",dict_array)
dict_array.clear()
'''
------------------------------------------------------------------------
            Log out
------------------------------------------------------------------------
'''
driver.get('https://www.linkedin.com')
sleep(randrange(5,7))
try:
    nav_menu_button = driver.find_element_by_xpath("//*[@id='nav-settings__dropdown-trigger']")
    nav_menu_button.click()
except Exception:
    pass
sleep(randrange(5,7))
try:
    sign_out_button = driver.find_element_by_xpath("//a[@href='/m/logout/']")
    sign_out_button.click()
except Exception:
    pass
print("Log out...")
sleep(randrange(5,7))

print("Done...")
driver.close()
exit()
