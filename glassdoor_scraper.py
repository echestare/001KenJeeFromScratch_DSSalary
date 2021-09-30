# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
#original->    driver = webdriver.Chrome(executable_path="/Users/omersakarya/Documents/GitHub/scraping-glassdoor-selenium/chromedriver", options=options)
    driver.set_window_size(1120, 1000)
       
    url= "https://www.glasdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+keyword+"&sc.keyword"+keyword+"&sc.keyword=data+Scientist&locT=&locId=&jobType="    #<-Modification made by Ken Jee
#original->    url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=palo%20alto,ca,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
#THe next are just link example. They are not adapted with the keyword parameter (+keyword+)     30/Sep/2021
#Palo Alto: https://www.glassdoor.com/Job/jobs.htm?sc.occupationParam=%22data+scientist%22&sc.locationSeoString=Palo+Alto%2C+CA+%28US%29&locId=1147434&locT=C&clickSource=searchBox
#Bs As:     https://www.glassdoor.com/Job/jobs.htm?sc.occupationParam=%22data+scientist%22&sc.locationSeoString=Buenos+Aires+%28Argentina%29&locId=2242084&locT=C&clickSource=searchBox
#Madrid:    https://www.glassdoor.com/Job/jobs.htm?sc.occupationParam=%22data+scientist%22&sc.locationSeoString=Madrid+%28Spain%29&locId=2664239&locT=C&clickSource=searchBox

    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(slp_time)
# This was not working so I take it off:
        #Test for the "Sign Up" prompt and get rid of it.
#        try:
#            driver.find_element_by_class_name("selected").click()
#        except ElementClickInterceptedException:
#            pass

        time.sleep(.1)
#/////////////////////////////////////////////¿elimino esto?/////////////////////////////////////////////////////////////////////////////////////////////
#        try:
##original->            driver.find_element_by_class_name("ModalStyle__xBtn___29PT9").click()  #clicking to the X.
#            driver.find_element_by_css_selector('[alt="Close"]').click()  #clicking to the X.    <- Again Ken Jee magic
#        except NoSuchElementException:
#            pass
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////        
        
        #Going through each job in this page
#original->        job_buttons = driver.find_elements_by_class_name("jl")  #jl for Job Listing. These are the buttons we're going to click.
        job_buttons = driver.find_elements_by_class_name("react-job-listing")  #looks like this works. Buy since I don't understand what I'm doing....
        for job_button in job_buttons:  
                
            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))

            if len(jobs) >= num_jobs:
                break
  
            job_button.click()  #You might 
     
            time.sleep(1)
    
            collected_successfully = False
 
            try:
#original->                driver.find_element_by_class_name("SVGInline").click()  #clicking to the X.
                driver.find_element_by_css_selector('[alt="Close"]').click()  #clicking to the X.    <- Again Ken Jee magic
            except NoSuchElementException:
                pass
            
            while not collected_successfully:

                try:
                    company_name = driver.find_element_by_xpath('.//div[@class="css-xuk5ye e1tk4kwz5"]').text
#original->                   company_name = driver.find_element_by_xpath('.//div[class="job_title"]').text   <-I guess this line didn't say "job_title", may be I modified this and can't remember the original parameter.
#In the next lines I compare code to find the correct way to modify the line above. I just choose two jobs lines.
#Theese are the code for the left column where you choose a work to read (in the internet page):
#<div class="d-flex flex-column pl-sm css-1buaf54 job-search-key-1mn3dn8 e1rrn5ka0"><div class="d-flex justify-content-between align-items-start"><a href="/partner/jobListing.htm?pos=101&amp;ao=1136043&amp;s=58&amp;guid=0000017c3476902794b1b8e9a26ad631&amp;src=GD_JOB_AD&amp;t=SR&amp;vt=w&amp;ea=1&amp;cs=1_8b4f2c90&amp;cb=1632967760782&amp;jobListingId=1007186540183&amp;jrtk=2-0-1fgq7d485u3gi801-1fgq7d48m3ojp001-c4d371c430bd4967" rel="nofollow noopener noreferrer" target="_blank" class=" job-search-key-l2wjgv e1n63ojh0 jobLink" style="pointer-events: all;"><span>Mercedes-Benz of San Francisco</span></a><div class="align-self-end d-flex flex-nowrap align-items-start"><span class="save-job-button-1007186540183 nowrap job-search-key-14vetv2 e4teh7x0" data-test="save-job"><span class="SVGInline css-9th5vf"><svg class="SVGInline-svg css-9th5vf-svg" style="width: 20px;height: 20px;" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 5.11l.66-.65a5.56 5.56 0 017.71.19 5.63 5.63 0 010 7.92L12 21l-8.37-8.43a5.63 5.63 0 010-7.92 5.56 5.56 0 017.71-.19zm7.66 6.75a4.6 4.6 0 00-6.49-6.51L12 6.53l-1.17-1.18a4.6 4.6 0 10-6.49 6.51L12 19.58z" fill="currentColor" fill-rule="evenodd"></path></svg></span></span></div></div><a class="jobLink job-search-key-1rd3saf eigr9kq1" data-test="job-link" href="/partner/jobListing.htm?pos=101&amp;ao=1136043&amp;s=58&amp;guid=0000017c3476902794b1b8e9a26ad631&amp;src=GD_JOB_AD&amp;t=SR&amp;vt=w&amp;ea=1&amp;cs=1_8b4f2c90&amp;cb=1632967760782&amp;jobListingId=1007186540183&amp;jrtk=2-0-1fgq7d485u3gi801-1fgq7d48m3ojp001-c4d371c430bd4967" rel="nofollow noopener noreferrer" target="_blank" style="pointer-events: all;"><span>DMV/Contracts Clerk</span></a><div class="d-flex flex-wrap job-search-key-1m2z0go e1rrn5ka2"><span class="css-1buaf54 pr-xxsm job-search-key-iii9i8 e1rrn5ka4">San Francisco, CA</span></div><div class="d-flex flex-wrap job-search-key-1a46cm1 e1rrn5ka3"><div class="css-1buaf54 pr-xxsm"><span data-test="detailSalary" class="job-search-key-1hbqxax e1wijj240">$30 - $40 Per Hour<span class="job-search-key-0 e1wijj242">(Employer est.)</span><span data-test="salaryIcon" class="SVGInline greyInfoIcon"><svg class="SVGInline-svg greyInfoIcon-svg" width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><g id="prefix__info-16-px" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><path d="M8 14A6 6 0 118 2a6 6 0 010 12zm0-1A5 5 0 108 3a5 5 0 000 10zm-.6-5.6a.6.6 0 111.2 0V11a.6.6 0 01-1.2 0V7.4zM8 5.6a.6.6 0 110-1.2.6.6 0 010 1.2z" id="prefix__a" fill="#505863"></path></g></svg></span><div class="d-none"></div></span></div><div class="d-flex justify-content-between css-pa6dqi"><div class="d-flex flex-wrap-reverse css-13cn532 css-pa6dqi"><div class="d-flex flex-wrap"><div class="mx-xxsm css-1s8337r"><div><div class="job-search-key-r3emcz eigr9kq3">Easy Apply</div></div></div></div></div><div data-test="job-age" class="d-flex align-items-end pl-std css-17n8uzw">30d+</div></div></div></div>
#   <a href="/partner/jobListing.htm?pos=101&amp;ao=1136043&amp;s=58&amp;guid=0000017c3476902794b1b8e9a26ad631&amp;src=GD_JOB_AD&amp;t=SR&amp;vt=w&amp;cs=1_8b4f2c90&amp;cb=1632967760782&amp;jobListingId=1007186540183&amp;jrtk=2-0-1fgq7d485u3gi801-1fgq7d48m3ojp001-c4d371c430bd4967" rel="nofollow noopener noreferrer" target="_blank" class=" job-search-key-l2wjgv e1n63ojh0 jobLink" style="pointer-events: all;"><span>Mercedes-Benz of San Francisco</span></a>
#       <span>Mercedes-Benz of San Francisco</span>
#<div class="d-flex justify-content-between align-items-start"><a href="/partner/jobListing.htm?pos=102&amp;ao=1136043&amp;s=58&amp;guid=0000017c3476902794b1b8e9a26ad631&amp;src=GD_JOB_AD&amp;t=SR&amp;vt=w&amp;cs=1_e552ebba&amp;cb=1632967760782&amp;jobListingId=1007319319405&amp;jrtk=2-0-1fgq7d485u3gi801-1fgq7d48m3ojp001-0d289ac0aa8668ff" rel="nofollow noopener noreferrer" target="_blank" class=" job-search-key-l2wjgv e1n63ojh0 jobLink" style="pointer-events: all;"><span>US Citizenship and Immigration Services</span></a><div class="align-self-end d-flex flex-nowrap align-items-start"><span class="save-job-button-1007319319405 nowrap job-search-key-14vetv2 e4teh7x0" data-test="save-job"><span class="SVGInline css-9th5vf"><svg class="SVGInline-svg css-9th5vf-svg" style="width: 20px;height: 20px;" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 5.11l.66-.65a5.56 5.56 0 017.71.19 5.63 5.63 0 010 7.92L12 21l-8.37-8.43a5.63 5.63 0 010-7.92 5.56 5.56 0 017.71-.19zm7.66 6.75a4.6 4.6 0 00-6.49-6.51L12 6.53l-1.17-1.18a4.6 4.6 0 10-6.49 6.51L12 19.58z" fill="currentColor" fill-rule="evenodd"></path></svg></span></span></div></div>
#   <a href="/partner/jobListing.htm?pos=102&amp;ao=1136043&amp;s=58&amp;guid=0000017c3476902794b1b8e9a26ad631&amp;src=GD_JOB_AD&amp;t=SR&amp;vt=w&amp;cs=1_e552ebba&amp;cb=1632967760782&amp;jobListingId=1007319319405&amp;jrtk=2-0-1fgq7d485u3gi801-1fgq7d48m3ojp001-0d289ac0aa8668ff" rel="nofollow noopener noreferrer" target="_blank" class=" job-search-key-l2wjgv e1n63ojh0 jobLink" style="pointer-events: all;"><span>US Citizenship and Immigration Services</span></a>
#       <span>US Citizenship and Immigration Services</span>
#Theese are the code for the work description on the right (in the internet page):       I had used theese.
#<div class="css-xuk5ye e1tk4kwz5">Mercedes-Benz of San Francisco<span data-test="detailRating" class="css-1m5m32b e1tk4kwz4">3.5<span class="css-y6inve e1tk4kwz3"></span></span></div>
#<div class="css-xuk5ye e1tk4kwz5">US Citizenship and Immigration Services<span data-test="detailRating" class="css-1m5m32b e1tk4kwz4">3.6<span class="css-y6inve e1tk4kwz3"></span></span></div>
#I had decided to use 'class="css-xuk5ye e1tk4kwz5"' but may be, I could have tried 'class=" job-search-key-l2wjgv e1n63ojh0 jobLink"'
                    location = driver.find_element_by_xpath('.//div[@class="css-56kyx5 e1tk4kwz1"]').text
#original->                    location = driver.find_element_by_xpath('.//div[@class="location"]').text
#<div class="css-56kyx5 e1tk4kwz1">San Francisco, CA</div>                    
                    job_title = driver.find_element_by_xpath('.//div[contains(@class, "css-1j389vi e1tk4kwz2")]').text
                    #I modified the original u.u'
#<div class="css-1j389vi e1tk4kwz2">DMV/Contracts Clerk</div>                    
                    job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                    #I modified the original u.u'
#<div class="jobDescriptionContent desc"><p>Euromotors Auto Group has an outstanding opportunity for an organized, taskoriented, motivated, attention to detail DMV Contracts Clerk. The DMV Contracts Clerk will be someone who likes the busy day to day tasks in a fast-paced environment and who understands the accounting side of a dealership.</p><p><b>Essential Functions &amp; Responsibilities: </b></p><ul><li>Examines sales/car deal contracts to assure conformity to specified requirements</li><li>Verifies all documents are signed and completed properly</li><li>Processes paperwork on a timely basis</li><li>Post vehicle sale transactions to accounting records</li><li>Reconciles monthly schedules</li><li>Receive and process paperwork from the F&amp;I department.</li><li>Prepare trade-in vehicle jackets and ensure title is obtained.</li><li>Ensure that name and address files are updated on an ongoing basis.</li><li>Perform other tasks as assigned.</li><li>Licensing all New, Wholesale and Used vehicles for in and out of state customers.</li><li>VITU Processing/DMV Manual Submission</li><li>Apply for all duplicate titles needed for in and out of state</li><li>Obey all DMV compliance filings</li></ul><p><b>Minimum Qualifications: </b></p><ul><li>Automotive experience preferred but will train the right candidate</li><li>This position requires a high school diploma or equivalent</li><li>Candidates must be proficient in Microsoft Word and Microsoft Excel</li><li>Strong attention to detail</li><li>General math skills and critical thinking to ensure clean and efficient work</li><li>Good written &amp; verbal communication skills</li><li>Ability to maintain confidentiality and integrity</li><li>Good attendance and punctuality</li><li>Understand deadlines and applies appropriate sense of urgency and prioritization to all tasks with minimal supervision.</li><li>Professional appearance and work ethic</li><li>Team-oriented and comfortable in an open office</li><li>Ability to work overtime as needed during Month End and 1st business day of each month</li></ul><p><b>Mercedes-Benz of San Francisco provided the following inclusive hiring information: </b></p><p>We are an equal opportunity employer and considers all qualified applicants equally without regard to race, color, religion, sex, sexual orientation, gender identity, national origin, veteran status, or disability status.</p><p>Job Type: Full-time</p><p>Pay: $30.00 - $40.00 per hour</p><p>Benefits:</p><ul><li>401(k)</li><li>Dental insurance</li><li>Health insurance</li><li>Paid time off</li><li>Vision insurance</li></ul><p>Schedule:</p><ul><li>8 hour shift</li><li>Monday to Friday</li></ul><p>Education:</p><ul><li>High school or equivalent (Preferred)</li></ul><p>Experience:</p><ul><li>Customer service: 1 year (Preferred)</li></ul><p>Work Location:</p><ul><li>One location</li></ul><p>Work Remotely:</p><ul><li>No</li></ul><p>Work Location: One location</p></div>
                    collected_successfully = True
                    
                except:
                    time.sleep(5)

            try:
#original->                salary_estimate = driver.find_element_by_xpath('.//span[@class="gray small salary"]').text
                salary_estimate = driver.find_element_by_xpath('.//span[@class="css-1hbqxax e1wijj240"]').text#    <- Again Ken Jee magic
#Same work as before:
#<div class="css-1buaf54 pr-xxsm"><span data-test="detailSalary" class="job-search-key-1hbqxax e1wijj240">$50 - $100 Per Hour<span class="job-search-key-0 e1wijj242">(Employer est.)</span><span data-test="salaryIcon" class="SVGInline greyInfoIcon"><svg class="SVGInline-svg greyInfoIcon-svg" width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><g id="prefix__info-16-px" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><path d="M8 14A6 6 0 118 2a6 6 0 010 12zm0-1A5 5 0 108 3a5 5 0 000 10zm-.6-5.6a.6.6 0 111.2 0V11a.6.6 0 01-1.2 0V7.4zM8 5.6a.6.6 0 110-1.2.6.6 0 010 1.2z" id="prefix__a" fill="#505863"></path></g></svg></span><div class="d-none"></div></span></div>
#   <span data-test="detailSalary" class="job-search-key-1hbqxax e1wijj240">$50 - $100 Per Hour<span class="job-search-key-0 e1wijj242">(Employer est.)</span><span data-test="salaryIcon" class="SVGInline greyInfoIcon"><svg class="SVGInline-svg greyInfoIcon-svg" width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><g id="prefix__info-16-px" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><path d="M8 14A6 6 0 118 2a6 6 0 010 12zm0-1A5 5 0 108 3a5 5 0 000 10zm-.6-5.6a.6.6 0 111.2 0V11a.6.6 0 01-1.2 0V7.4zM8 5.6a.6.6 0 110-1.2.6.6 0 010 1.2z" id="prefix__a" fill="#505863"></path></g></svg></span><div class="d-none"></div></span>                
#<div><span data-test="detailSalary" class="css-1hbqxax e1wijj240"><span class="css-0 e1wijj242"><span class="SVGInline checkmark"><svg class="SVGInline-svg checkmark-svg" xmlns="http://www.w3.org/2000/svg" width="12" height="9" viewBox="0 0 12 9"><path fill="none" stroke="#0CAA41" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M11 1L3.759 8 1 5.333"></path></svg></span>Employer Provided Salary:</span>$50 - $100 Per Hour<span data-test="salaryIcon" class="SVGInline greyInfoIcon"><svg class="SVGInline-svg greyInfoIcon-svg" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><path d="M7 14A7 7 0 117 0a7 7 0 010 14zm0-.7A6.3 6.3 0 107 .7a6.3 6.3 0 000 12.6zm-.7-7a.7.7 0 011.4 0v4.2a.7.7 0 01-1.4 0zM7 4.2a.7.7 0 110-1.4.7.7 0 010 1.4z" fill="#505863" fill-rule="evenodd"></path></svg></span><div class="d-none"></div></span></div>
#   <span data-test="detailSalary" class="css-1hbqxax e1wijj240"><span class="css-0 e1wijj242"><span class="SVGInline checkmark"><svg class="SVGInline-svg checkmark-svg" xmlns="http://www.w3.org/2000/svg" width="12" height="9" viewBox="0 0 12 9"><path fill="none" stroke="#0CAA41" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M11 1L3.759 8 1 5.333"></path></svg></span>Employer Provided Salary:</span>$50 - $100 Per Hour<span data-test="salaryIcon" class="SVGInline greyInfoIcon"><svg class="SVGInline-svg greyInfoIcon-svg" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><path d="M7 14A7 7 0 117 0a7 7 0 010 14zm0-.7A6.3 6.3 0 107 .7a6.3 6.3 0 000 12.6zm-.7-7a.7.7 0 011.4 0v4.2a.7.7 0 01-1.4 0zM7 4.2a.7.7 0 110-1.4.7.7 0 010 1.4z" fill="#505863" fill-rule="evenodd"></path></svg></span><div class="d-none"></div></span>        
#<div class="css-1buaf54 pr-xxsm"><span data-test="detailSalary" class="job-search-key-1hbqxax e1wijj240">$50 - $55 Per Hour<span class="job-search-key-0 e1wijj242">(Employer est.)</span><span data-test="salaryIcon" class="SVGInline greyInfoIcon"><svg class="SVGInline-svg greyInfoIcon-svg" width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><g id="prefix__info-16-px" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><path d="M8 14A6 6 0 118 2a6 6 0 010 12zm0-1A5 5 0 108 3a5 5 0 000 10zm-.6-5.6a.6.6 0 111.2 0V11a.6.6 0 01-1.2 0V7.4zM8 5.6a.6.6 0 110-1.2.6.6 0 010 1.2z" id="prefix__a" fill="#505863"></path></g></svg></span><div class="d-none"></div></span></div>
#   <span data-test="detailSalary" class="job-search-key-1hbqxax e1wijj240">$50 - $55 Per Hour<span class="job-search-key-0 e1wijj242">(Employer est.)</span><span data-test="salaryIcon" class="SVGInline greyInfoIcon"><svg class="SVGInline-svg greyInfoIcon-svg" width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><g id="prefix__info-16-px" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><path d="M8 14A6 6 0 118 2a6 6 0 010 12zm0-1A5 5 0 108 3a5 5 0 000 10zm-.6-5.6a.6.6 0 111.2 0V11a.6.6 0 01-1.2 0V7.4zM8 5.6a.6.6 0 110-1.2.6.6 0 010 1.2z" id="prefix__a" fill="#505863"></path></g></svg></span><div class="d-none"></div></span>
#<div><span data-test="detailSalary" class="css-1hbqxax e1wijj240"><span class="css-0 e1wijj242"><span class="SVGInline checkmark"><svg class="SVGInline-svg checkmark-svg" xmlns="http://www.w3.org/2000/svg" width="12" height="9" viewBox="0 0 12 9"><path fill="none" stroke="#0CAA41" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M11 1L3.759 8 1 5.333"></path></svg></span>Employer Provided Salary:</span>$50 - $55 Per Hour<span data-test="salaryIcon" class="SVGInline greyInfoIcon"><svg class="SVGInline-svg greyInfoIcon-svg" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><path d="M7 14A7 7 0 117 0a7 7 0 010 14zm0-.7A6.3 6.3 0 107 .7a6.3 6.3 0 000 12.6zm-.7-7a.7.7 0 011.4 0v4.2a.7.7 0 01-1.4 0zM7 4.2a.7.7 0 110-1.4.7.7 0 010 1.4z" fill="#505863" fill-rule="evenodd"></path></svg></span><div class="d-none"></div></span></div>
#   <span data-test="detailSalary" class="css-1hbqxax e1wijj240"><span class="css-0 e1wijj242"><span class="SVGInline checkmark"><svg class="SVGInline-svg checkmark-svg" xmlns="http://www.w3.org/2000/svg" width="12" height="9" viewBox="0 0 12 9"><path fill="none" stroke="#0CAA41" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M11 1L3.759 8 1 5.333"></path></svg></span>Employer Provided Salary:</span>$50 - $55 Per Hour<span data-test="salaryIcon" class="SVGInline greyInfoIcon"><svg class="SVGInline-svg greyInfoIcon-svg" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><path d="M7 14A7 7 0 117 0a7 7 0 010 14zm0-.7A6.3 6.3 0 107 .7a6.3 6.3 0 000 12.6zm-.7-7a.7.7 0 011.4 0v4.2a.7.7 0 01-1.4 0zM7 4.2a.7.7 0 110-1.4.7.7 0 010 1.4z" fill="#505863" fill-rule="evenodd"></path></svg></span><div class="d-none"></div></span>
#I had decided to use 'class="css-1hbqxax e1wijj240"' but may be, I could have tried 'class="css-1buaf54 pr-xxsm'


            except NoSuchElementException:
                salary_estimate = -1 #You need to set a "not found value. It's important."

            try:
                rating = driver.find_element_by_xpath('.//span[@class="css-1m5m32b e1tk4kwz4"]').text
#original->                rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
#<span class=" job-search-key-srfzj0 e1cjmv6j0">4.2<i class="job-search-key-0 e1cjmv6j1"></i></span>
#<span data-test="detailRating" class="css-1m5m32b e1tk4kwz4">4.5<span class="css-y6inve e1tk4kwz3"></span></span>

            except NoSuchElementException:
                rating = -1 #You need to set a "not found value. It's important."

            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            #Going to the Company tab...
            #clicking on this:
            #<div class="tab" data-tab-type="overview"><span>Company</span></div>
            try:
                driver.find_element_by_xpath('.//div[@data-item="tab" and @data-tab-type="overview"]').click()
#original->                driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()                
#<div data-item="tab" data-test="overview" data-tab-type="overview" data-brandviews="" class="css-1ap6ha9 ef7s0la0"><span>Company</span></div>

#"Headquarters" is not longer provided by the page
#original->                try:
#original commented->                    #<div class="infoEntity">
#original commented->                    #    <label>Headquarters</label>
#original commented->                    #    <span class="value">San Francisco, CA</span>
#original commented->                    #</div>
#original->                    headquarters = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
#original->                except NoSuchElementException:
#original->                    headquarters = -1

                try:
#<div class="d-flex flex-wrap"><div class="d-flex justify-content-start css-daag8o e1pvx6aw2"><span class="css-1pldt9b e1pvx6aw1">Size</span><span class="css-1ff36h2 e1pvx6aw0">1 to 50 Employees</span></div><div class="d-flex justify-content-start css-daag8o e1pvx6aw2"><span class="css-1pldt9b e1pvx6aw1">Founded</span><span class="css-1ff36h2 e1pvx6aw0">2004</span></div><div class="d-flex justify-content-start css-daag8o e1pvx6aw2"><span class="css-1pldt9b e1pvx6aw1">Type</span><span class="css-1ff36h2 e1pvx6aw0">Company - Private</span></div><div class="d-flex justify-content-start css-daag8o e1pvx6aw2"><span class="css-1pldt9b e1pvx6aw1">Industry</span><span class="css-1ff36h2 e1pvx6aw0">Enterprise Software &amp; Network Solutions</span></div><div class="d-flex justify-content-start css-daag8o e1pvx6aw2"><span class="css-1pldt9b e1pvx6aw1">Sector</span><span class="css-1ff36h2 e1pvx6aw0">Information Technology</span></div><div class="d-flex justify-content-start css-daag8o e1pvx6aw2"><span class="css-1pldt9b e1pvx6aw1">Revenue</span><span class="css-1ff36h2 e1pvx6aw0">Unknown / Non-Applicable</span></div></div>
                    # driver.find_element_by_xpath('.//div[@class="d-flex flex-wrap"]//div[@class="d-flex justify-content-start css-daag8o e1pvx6aw2"]//span[@class="css-1pldt9b e1pvx6aw1"]')
                    # print("\nbandera 0\n")
                    # driver.find_element_by_xpath('.//div[@class="d-flex flex-wrap"]')
                    # print("\nbandera 0,1\n")
                    # driver.find_element_by_xpath('.//div[@class="d-flex justify-content-start css-daag8o e1pvx6aw2"]')
                    # print("\nbandera 0,2\n")
                    # driver.find_element_by_xpath('.//span[@class="css-1pldt9b e1pvx6aw1"]')
                    # print("\nbandera 0,3\n")
                    # driver.find_element_by_xpath('.//span[text()="Size"]')
                    # print("\nbandera 0,4\n")
                    size = driver.find_element_by_xpath('.//span[text()="Size"]//following-sibling::*').text
#//parent::div/following-sibling::div//input'
#original->                    size = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
#<div class="d-flex justify-content-start css-daag8o e1pvx6aw2"><span class="css-1pldt9b e1pvx6aw1">Size</span><span class="css-1ff36h2 e1pvx6aw0">10000+ Employees</span></div>
#   <span class="css-1pldt9b e1pvx6aw1">Size</span>
#   <span class="css-1ff36h2 e1pvx6aw0">1 to 50 Employees</span>
                except NoSuchElementException:
                    size = -1

                try:
                    founded = driver.find_element_by_xpath('.//span[text()="Founded"]//following-sibling::*').text
#original->                    founded = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Founded"]//following-sibling::*').text                    
#<div class="d-flex justify-content-start css-daag8o e1pvx6aw2"><span class="css-1pldt9b e1pvx6aw1">Founded</span><span class="css-1ff36h2 e1pvx6aw0">1939</span></div>
#   <span class="css-1pldt9b e1pvx6aw1">Founded</span>
#   <span class="css-1ff36h2 e1pvx6aw0">1939</span>
                except NoSuchElementException:
                    founded = -1

                try:
                    type_of_ownership = driver.find_element_by_xpath('.//span[text()="Type"]//following-sibling::*').text
#original->                    type_of_ownership = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Type"]//following-sibling::*').text
                except NoSuchElementException:
                    type_of_ownership = -1

                try:
                    industry = driver.find_element_by_xpath('.//span[text()="Industry"]//following-sibling::*').text
#original->                    industry = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Industry"]//following-sibling::*').text
                except NoSuchElementException:
                    industry = -1

                try:
                    sector = driver.find_element_by_xpath('.//span[text()="Sector"]//following-sibling::*').text
#original->                    sector = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Sector"]//following-sibling::*').text
                except NoSuchElementException:
                    sector = -1

                try:
                    revenue = driver.find_element_by_xpath('.//span[text()="Revenue"]//following-sibling::*').text
#original->                    revenue = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Revenue"]//following-sibling::*').te
                except NoSuchElementException:
                    revenue = -1

#"Competitors" is not longer provided by the page
#original->                try:
#original->                    competitors = driver.find_element_by_xpath('.//span[text()="Competitors"]//following-sibling::*').text
#original->                    competitors = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text           
#original->                except NoSuchElementException:
#original->                    competitors = -1

            except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
#original->                 headquarters = -1
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1
#original->                competitors = -1

                
            if verbose:
#original->                 print("Headquarters: {}".format(headquarters))
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
#original->                print("Competitors: {}".format(competitors))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
#original->             "Headquarters" : headquarters,
            "Size" : size,
            "Founded" : founded,
            "Type of ownership" : type_of_ownership,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue})
#original->            "Revenue" : revenue,
#original->            "Competitors" : competitors})
            #add job to jobs

        #Clicking on the "next page" button
        try:
            driver.find_element_by_xpath('.//span[@class="SVGInline"]').click()
#original->           driver.find_element_by_xpath('.//li[@class="next"]//a').click()
#<span class="SVGInline"><svg class="SVGInline-svg" style="width: 16px;height: 16px;" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M16.72 11.29L9.19 3.9a1.3 1.3 0 00-1.83 0 1.26 1.26 0 000 1.78L13.78 12l-6.42 6.3a1.26 1.26 0 000 1.78 1.3 1.3 0 001.83 0l7.53-7.39a1 1 0 000-1.4z" fill="currentColor" fill-rule="evenodd"></path></svg></span>
#   <svg class="SVGInline-svg" style="width: 16px;height: 16px;" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M16.72 11.29L9.19 3.9a1.3 1.3 0 00-1.83 0 1.26 1.26 0 000 1.78L13.78 12l-6.42 6.3a1.26 1.26 0 000 1.78 1.3 1.3 0 001.83 0l7.53-7.39a1 1 0 000-1.4z" fill="currentColor" fill-rule="evenodd"></path></svg>

        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame. 



