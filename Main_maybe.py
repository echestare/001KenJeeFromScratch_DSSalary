# -*- coding: utf-8 -*-

import glassdoor_scraper as gs
import pandas as pd

path= "D:/ECHE/0-Datos/Projects Practicing/001 KenJeeFromScratch_DSSalary/chromedriver"

df = gs.get_jobs('data scientist',70,False,path,15)



# from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
# from selenium import webdriver
# import time
# import pandas as pd

# #'''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
#     #Initializing the webdriver
# options = webdriver.ChromeOptions()
    
#     #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
#     #options.add_argument('headless')
# path= "D:/ECHE/0-Datos/Projects Practicing/001 KenJeeFromScratch_DSSalary/chromedriver"    
#     #Change the path to where chromedriver is in your home folder.
# driver = webdriver.Chrome(executable_path=path, options=options)
# #original->    driver = webdriver.Chrome(executable_path="/Users/omersakarya/Documents/GitHub/scraping-glassdoor-selenium/chromedriver", options=options)
# driver.set_window_size(1120, 1000)
# keyword='data scientist'
# url= "https://www.glasdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+keyword+"&sc.keyword"+keyword+"&sc.keyword=data+Scientist&locT=&locId=&jobType="

# #original->    url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147434&locKeyword=palo%20alto,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
# driver.get(url)
# #Palo Alto: https://www.glassdoor.com/Job/jobs.htm?sc.occupationParam=%22data+scientist%22&sc.locationSeoString=Palo+Alto%2C+CA+%28US%29&locId=1147434&locT=C&clickSource=searchBox
# #Argentina: https://www.glassdoor.com/Job/argentina-data-scientist-jobs-SRCH_IL.0,9_IN15_KO10,24.htm?clickSource=searchBox
# #EEUU:      https://www.glassdoor.com/Job/united-states-data-scientist-jobs-SRCH_IL.0,13_IN1_KO14,28.htm?clickSource=searchBox
# #Spain:     https://www.glassdoor.com/Job/spain-data-scientist-jobs-SRCH_IL.0,5_IN219_KO6,20.htm?clickSource=searchBox
# #Bs As:     https://www.glassdoor.com/Job/jobs.htm?sc.occupationParam=%22data+scientist%22&sc.locationSeoString=Buenos+Aires+%28Argentina%29&locId=2242084&locT=C&clickSource=searchBox
# #Madrid:    https://www.glassdoor.com/Job/jobs.htm?sc.occupationParam=%22data+scientist%22&sc.locationSeoString=Madrid+%28Spain%29&locId=2664239&locT=C&clickSource=searchBox


