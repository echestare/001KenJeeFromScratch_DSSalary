# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:21:59 2021

@author: s_eze
"""
import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")


##############################SALARY PARSING##############################

#Since cells were found to have a different salary format, they should be highlighted.
#So two new columns with 1 for the detected cells and 0 for the normal cells are needed (one for each case):
df["hourly"] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df["employer_provided"] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

#Creating a new dataframe with the salary data and processed it:
    #Here we are deleting those rows without the salary data.
df = df[df['Salary Estimate'] != '-1']
    #Here is taken everything before the '(' ignoring the rest and pasting that in the serie "salary".
salary = df["Salary Estimate"].apply(lambda x: x.split('(')[0])
    #Here are erased the 'K' and '$
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))
    #Here are replaced the cases previously detected with a blank space instead.
min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

#Now that only numbers are left, separated with a '-', split them and put them in two different dataframe will help to calculate the average
    #This doesn't take into consideration the data presented in an hourly form:
df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
    #calculating average:

#Here, Ken Jee forgot to take into consideration those salary values that where given in an hourly form. Maybe, I should had declared a serie and do it there. However, it works anyway:
    #It is logical to think tha the companies that are hiring telling an hourly salary couldnot be hiring annualy, hiring by season, or are not sure about investment in this area, so  the salaries could be irregualr (generally worst)
        #Later if I don't want to add them in the EDA step, then there we got the "hourly" column
            #Why I multiply by 1.92? 8 hours, 5 days, 4 weeks, 12 months: 8*5*4*12=1920... The values in the column are in miles, so I need to divide by 1000.
df['min_salary']= df.apply(lambda x: x['min_salary'] if x['hourly']==0 else (int)(x['min_salary']*1.92), axis = 1)
df['max_salary']= df.apply(lambda x: x['max_salary'] if x['hourly']==0 else (int)(x['max_salary']*1.92), axis = 1)
        
    #Finally, averaging:
df['avg_salary'] = (df.min_salary+df.max_salary)/2


##############################Company name text only##############################
#Taking into account that the Company_Name  column has not only the name of the company, but also the information of the ratings, it is necessary to remove ir the latter.
#If you know the glassdoor_scraping.py code you will know that when there is no rating, the cell will be filled with "-1", but when there is rating the content of the cell will be cero above (this also can be seen just looking the data).
#Finally, the rating (when exist) has 3 characters (number dot number)
#So, the next line is telling that when the Rating column has a value greater than zero, the company name will have 3 characters removed.
    #the "axis = 1" parameter says that the data will be searched in the same row
df['company_txt']= df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis = 1)


##############################state field##############################
#Here can be seeing that States are after the comma.
    #The next line split the cell and take what is after the comma. Simple.
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
    #If we want to see how many are in each state (it prints the result in the console):
#df.job_state.value_counts()

#This works in Ken Jee work, but since the site glassdoor does not give HeadQuarters information anymore it is irrelevant to do this now. In any case, I left it here.
#df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)


##############################age of company##############################
#How many years are these companies working?
    #Here you must to put the year acording to the data. If I use the data that Ken Jee extracted I must to use 2020 (in that year was the data extracted), then if I want to compare this data with data extracted other year and I don't use the correct year, the comparisson become meaningless
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2021-x)


##############################parsing of job description(py, etc)##############################
#We may see what we got.
#df['Job Description']
    #Looks like it is the full job description. Great! We can extract many information from this.

#Now, what Analysis should we do?
#Perhaps to watch how many job description mentions 2019 most used data science tool
    #Why 2019: cause Ken Jee is doing this analysis in 2020 and when he searched "top data science tool" to know (how one must do in every project "investigate what is important there") he found this site https://data-flair.training/blogs/data-science-tools/ and considered relevant enough.
    #This is just a little representation about how one must to investigate, take into consideration source with criterion and a judgment approach
    #So he determined (beginning with this example investigation) 5 keywords from the source: python, r studio, sparks, aws and excel.
    
    #Could this source be enough for me now (2021)?: https://searchbusinessanalytics.techtarget.com/feature/15-data-science-tools-to-consider-using 
    
    #Well, we count how many jobs_descriptions mention each keyword:
#python 
    #I think if some job description calls pySpark or py-something it is implicit "python"
df['python_yn']  = df['Job Description'].apply(lambda x: 1 if 'py' in x.lower() else 0)
    #NOTE: the _yn in the name means that what I'm doing is split by yes or no there is "python" in the description.
df.python_yn.value_counts()
#r studio
    #If you say "hey, I know r and py" looks like " r " is the correct way to search it.
df['R_yn']  = df['Job Description'].apply(lambda x: 1 if ' r ' in x.lower() or 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()
#spark
df['spark_yn']  = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark_yn.value_counts()
#aws
df['aws_yn']  = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws_yn.value_counts()
#excel
df['excel_yn']  = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel_yn.value_counts()





############################## last details ##############################
#Cheking columns names:
#df.columns
#new dataframe withouut the undesirable column 1:
df_out = df.drop(['Unnamed: 0'], axis =1)




############################## exporting the cleaned database ##############################
df_out.to_csv('salary_data_cleaned.csv',index=False)

#Checking if the database was exported correctly:
#pd.read_csv('salary_data_cleaned.csv')

