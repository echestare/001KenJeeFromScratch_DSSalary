# 001KenJeeFromScratch_DSSalary
# Don't look at me. Just copying exactly what Ken is doing. Let me practice in peace!! baka!
I swore I gonna give a better look to this readme.

Data Science Salary Estimator: Project Overview

(Why had I done this? to practice; copy a profesional; understand some of my limitations)  <-- I'm still quite a noob.


What can one see in this project? (Ken Jee wrote the next). 
**Not yet**-Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
-Scraped over 1000 job descriptions from glassdoor using python and selenium
**Not yet**-Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
**Not yet**-Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
**Not yet**-Built a client facing API using flask






Code and Resources Used (Maybe I'm copying too much, srry, Ken Jee)
Python Version: 3.7
Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
**no idea what is this, yet** For Web Framework Requirements: pip install -r requirements.txt
Scraping: You can find the original code (from Ömer Sakarya) here: 
    -Explication link: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
    -Github link: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
**Not yet**Flask Productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2
And here is the whole and original data science analysis link (from Ken Jee): 
    -Github link: https://github.com/PlayingNumbers/ds_salary_proj
    -Awesome YouTube link: https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t
I want to say thanks both. ######I SHOULD PUT THIS IN BIG LETTERS########

Web Scraping

The glassdoor_scraper file that Ken Jee adapted needed a new update. Now, here is it. (09/30/2021)
(It works, but I had deduced the repairs. I mean I don't know what I'm doing. I used Selenium for the first time, I don't know javascript, html, css, etc.)
If you see a better way to improve, clean or something go ahead and please show me the results.

Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:
Job title
Salary Estimate
Job Description
Rating
Company
Location
[Company Headquarters] <- not anymore
Company Size
Company Founded Date
Type of Ownership
Industry
Sector
Revenue
[Competitors] <- not anymore


