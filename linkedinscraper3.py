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
import json
from scrape_linkedin import Scraper
import pandas as pd


dates = []
linkedin_urls = []

with open('Links/HunterCollegeCSlinks.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    next(csvReader, None)
    for row in csvReader:
        dates.append(row[0])
        linkedin_urls.append(row[1])


for linkedin_url in linkedin_urls:
    with Scraper() as scraper:
        profile = scraper.get_profile(linkedin_url)

# for personal info
        personalinfo = pd.DataFrame.from_dict(profile.personal_info, orient='index')
        personalinfo = personalinfo.transpose()

# for skills
        skills = pd.DataFrame.from_dict(profile.skills)

# for experiences
        experiences = pd.DataFrame.from_dict(profile.experiences, orient='index')
        experiences = experiences.transpose()

# for interests
        interests = pd.DataFrame.from_dict(profile.interests)
        #interests.columns = ['interests']

# for accomplishments
        accomplishments = pd.DataFrame.from_dict(profile.accomplishments, orient='index')
        accomplishments = accomplishments.transpose()

        result = pd.concat([personalinfo, skills, experiences, interests, accomplishments], ignore_index=True)

        result.to_csv('linkedindata/'+linkedin_url[28:-1]+'.csv')

        sleep(randrange(15,30))



#save profile as seperate CSVs and then join later in R
