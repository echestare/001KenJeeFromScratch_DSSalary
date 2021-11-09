# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:21:59 2021

@author: s_eze
"""
import pandas as pd

df = pd.read_csv("data_scraped.csv")



############################## some details ##############################
#Cheking columns names:
#df.columns
#droping duplicates rows
df=df.drop_duplicates()
#deleting the undesirable column 1:
df = df.drop(['Unnamed: 0'], axis =1)
#deleting row without salary: our entirely analysis depends on salary info.
df = df[df['Salary Estimate'] != '-1']
#Reseting index
df=df.reset_index(drop=True)
#df.isnull().sum() #This line count how many nan data are in each column of the df
#filling nan data with '-1'
df = df.fillna('-1')

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
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1] if ',' in x else x)
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
                                                    #https://www.jigsawacademy.com/top-analytics-tools-every-data-scientist-must-learn/
    
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
#sql
df['sql_yn']  = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df.sql_yn.value_counts()
#sas 
df['sas_yn']  = df['Job Description'].apply(lambda x: 1 if (' sas ' in x.lower() or ' sas,' in x.lower() or ' sas.' in x.lower())  else 0)
df.sas_yn.value_counts()
#d3js
df['d3js_yn']  = df['Job Description'].apply(lambda x: 1 if 'd3' in x.lower() else 0)
df.d3js_yn.value_counts()
#julia
df['julia_yn']  = df['Job Description'].apply(lambda x: 1 if 'julia' in x.lower() else 0)
df.julia_yn.value_counts()
#jupyter
df['jupyter_yn']  = df['Job Description'].apply(lambda x: 1 if 'jupyter' in x.lower() else 0)
df.jupyter_yn.value_counts()
#keras
df['keras_yn']  = df['Job Description'].apply(lambda x: 1 if 'keras' in x.lower() else 0)
df.keras_yn.value_counts()
#matlab
df['matlab_yn']  = df['Job Description'].apply(lambda x: 1 if 'matlab' in x.lower() else 0)
df.matlab_yn.value_counts()
#matplotlib
df['matplotlib_yn']  = df['Job Description'].apply(lambda x: 1 if 'matplotlib' in x.lower() else 0)
df.matplotlib_yn.value_counts()
#pytorch
df['pytorch_yn']  = df['Job Description'].apply(lambda x: 1 if 'pytorch' in x.lower() else 0)
df.pytorch_yn.value_counts()
#scikit-learn
df['scikit_yn']  = df['Job Description'].apply(lambda x: 1 if 'scikit' in x.lower() else 0)
df.scikit_yn.value_counts()
#tensor
df['tensor_yn']  = df['Job Description'].apply(lambda x: 1 if 'tensor' in x.lower() else 0)
df.tensor_yn.value_counts()
#weka
df['weka_yn']  = df['Job Description'].apply(lambda x: 1 if 'weka' in x.lower() else 0)
df.weka_yn.value_counts()
#selenium
df['selenium_yn']  = df['Job Description'].apply(lambda x: 1 if 'selenium' in x.lower() else 0)
df.selenium_yn.value_counts()
#hadoop
df['hadoop_yn']  = df['Job Description'].apply(lambda x: 1 if 'hadoop' in x.lower() else 0)
df.hadoop_yn.value_counts()
#tableau
df['tableau_yn']  = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df.tableau_yn.value_counts()
#power bi
df['bi_yn']  = df['Job Description'].apply(lambda x: 1 if ('power bi' in x.lower() or 'powerbi' in x.lower()) else 0)
df.bi_yn.value_counts()
#bigml
df['bigml_yn']  = df['Job Description'].apply(lambda x: 1 if 'bigml' in x.lower() else 0)
df.bigml_yn.value_counts()
#rapidminer
df['rapidminer_yn']  = df['Job Description'].apply(lambda x: 1 if 'rapidminer' in x.lower() else 0)
df.rapidminer_yn.value_counts()
#apache flink
df['flink_yn']  = df['Job Description'].apply(lambda x: 1 if 'flink' in x.lower() else 0)
df.flink_yn.value_counts()
#datarobot
df['datarobot_yn']  = df['Job Description'].apply(lambda x: 1 if 'datarobot' in x.lower() else 0)
df.datarobot_yn.value_counts()
#sap hana
df['hana_yn']  = df['Job Description'].apply(lambda x: 1 if 'hana' in x.lower() else 0)
df.hana_yn.value_counts()
#mongo db
df['mongo_yn']  = df['Job Description'].apply(lambda x: 1 if 'mongo' in x.lower() else 0)
df.mongo_yn.value_counts()
#trifacta
df['trifacta_yn']  = df['Job Description'].apply(lambda x: 1 if 'trifacta' in x.lower() else 0)
df.trifacta_yn.value_counts()
#minitab
df['minitab_yn']  = df['Job Description'].apply(lambda x: 1 if 'minitab' in x.lower() else 0)
df.minitab_yn.value_counts()
#kafka
df['kafka_yn']  = df['Job Description'].apply(lambda x: 1 if 'kafka' in x.lower() else 0)
df.kafka_yn.value_counts()
#microstrategy
df['microstrategy_yn']  = df['Job Description'].apply(lambda x: 1 if 'microstrategy' in x.lower() else 0)
df.microstrategy_yn.value_counts()
#google analytics
df['google_an_yn']  = df['Job Description'].apply(lambda x: 1 if 'google analytics' in x.lower() else 0)
df.google_an_yn.value_counts()
#Statistical Package for the Social Sciences
df['spss_yn']  = df['Job Description'].apply(lambda x: 1 if 'spss' in x.lower() else 0)
df.spss_yn.value_counts()








############################## exporting the cleaned database ##############################
df_out=df
df_out.to_csv('data_cleaned.csv',index=False)

#Checking if the database was exported correctly:
#pd.read_csv('salary_data_cleaned.csv')

