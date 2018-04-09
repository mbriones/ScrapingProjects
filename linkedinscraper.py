import csv
from selenium import webdriver
from time import sleep
from random import randrange
from linkedin_scraper import Person
'''
-------------------------------------------------------
This function writes to csv excel file
---------------------------------------------------------
'''

def write_to_csv_dict(filename,dict_array):
    myFile = open(filename, "w")
    with myFile:
        fieldnames = ['person']
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
user_email = "miguelabriones@gmail.com"
password = "outkst237"
print("Google Chrome Starting...")
sleep(randrange(5,7))
'''
------------------------------------------------------------------------
            SELENIUM DRIVER STARTS
------------------------------------------------------------------------
'''
driver = webdriver.Chrome()
#driver = webdriver.Chrome("/Users/miguelbriones/ByteflowProjects/PeopleAnalytics/chromedriver")
driver.get("https://www.linkedin.com")
'''
------------------------------------------------------------------------
            SIGN IN
------------------------------------------------------------------------
'''
email_button = driver.find_element_by_xpath('//input[@id="login-email"]')
email_button.send_keys(user_email)
sleep(randrange(5,9))
pass_button = driver.find_element_by_xpath('//input[@id="login-password"]')
pass_button.send_keys(password)
sleep(randrange(5,9))
submit_button = driver.find_element_by_xpath('//input[@id="login-submit"]')
submit_button.click()
print("Log in...")
'''
---------------------------------------------------------
LinkedIn Profiles Scraping
---------------------------------------------------------
'''
dict_array=[]

linkedin_urls = ["https://www.linkedin.com/in/victoriakythai/",
                 "https://www.linkedin.com/in/melinda-brown/"]
'''
for pizza in linkedin_urls:

    person = Person(linkedin_url = pizza, driver=driver, scrape = False)

    person.scrape(close_on_complete=False)

    dict_row={'person':person}

    dict_array.append(dict_row)

    sleep(randrange(5, 10))
'''

victoria = Person(linkedin_url = "https://www.linkedin.com/in/victoriakythai/", driver=driver, scrape = False)
victoria.scrape(close_on_complete=False)

pizza1 = " ".join(str(x) for x in [victoria])

dict_row={'person':pizza1}
dict_array.append(dict_row)

driver.delete_all_cookies()
driver.get("https://www.linkedin.com")
email_button = driver.find_element_by_xpath('//input[@id="login-email"]')
email_button.send_keys(user_email)
sleep(randrange(5,9))
pass_button = driver.find_element_by_xpath('//input[@id="login-password"]')
pass_button.send_keys(password)
sleep(randrange(5,9))
submit_button = driver.find_element_by_xpath('//input[@id="login-submit"]')
submit_button.click()
print("Log in...")

melinda = Person("https://www.linkedin.com/in/melinda-brown/", driver = driver, scrape = False)
melinda.scrape(close_on_complete=False)

pizza2 = " ".join(str(x) for x in [melinda])

dict_row={'person':pizza2}
dict_array.append(dict_row)

write_to_csv_dict("results.csv", dict_array)

dict_array.clear()

'''
------------------------------------------------------------------------
            Log out
------------------------------------------------------------------------
'''
driver.get('https://www.linkedin.com')
sleep(randrange(5,20))
try:
    nav_menu_button = driver.find_element_by_xpath("//*[@id='nav-settings__dropdown-trigger']")
    nav_menu_button.click()
except Exception:
    pass
sleep(randrange(10,20))
try:
    sign_out_button = driver.find_element_by_xpath("//a[@href='/m/logout/']")
    sign_out_button.click()
except Exception:
    pass
print("Log out...")
sleep(randrange(5,20))

print("Done...")
driver.close()
exit()
