# -*- coding: utf-8 -*-

import glassdoor_scraper as gs
import pandas as pd

path= "D:/ECHE/0-Datos/Projects Practicing/001 KenJeeFromScratch_DSSalary/chromedriver"

df = gs.get_jobs('data scientist' , 1500 , False , path , 15)

df.to_csv('glassdoor_jobs.csv' , index = False)



