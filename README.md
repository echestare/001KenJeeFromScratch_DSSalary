[![LinkedIn][linkedin-shield]][linkedin-url]
########################################
########################################????


# <p align="center"> Data Professions salaries - Analysing  and Data Science </p>


## A short epilogue:
#### My first approach about this project was to copy [Ken Jee](https://github.com/PlayingNumbers) [senior skills](https://github.com/PlayingNumbers/ds_salary_proj) and take what is nutritious for me.
#### Even so, as I was working, I was understanding that my skills was not soooo inferior as I thought and as I was adding stuff and enhancing some things I noticed that the work was differentiating more clearly. Therefore I decided to upload it as a proper work.
#### Actually at first, I was not going to share this and had set it as "private", but seeing that I was correcting things that other people were asking here or in StackOverflow and so, I decided to make it public.

#### This is where everything started: 
* **Ken Jee original DS Analysis code:** [ds_salary_proj](https://github.com/PlayingNumbers/ds_salary_proj) 
* [**Ken Jee YouTube Video explaining his project**](https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t) 
* [**Ken Jee GitHub Profile**](https://github.com/PlayingNumbers)



<!-- TABLE OF CONTENTS -->
## Index
<details open="open">
  <summary>Table of Contents: </summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-overview">Project Overview</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#stages-overview">Stages overview</a>
      <ul>
        <li><a href="#web-scraping">Web Scraping</a></li>
        <li><a href="#data-cleaning">Data Cleaning</a></li>
        <li><a href="#exploratory-data-analysis">Exploratory Data Analysis</a></li>
        <li><a href="#model-building">Model Building</a></li>
        <li><a href="#model-performance">Model performance</a></li>
        <li><a href="#productionization">Productionization</a></li>
      </ul>
    </li>
  </ol>
</details>
######################################## 
########################################


<!-- ABOUT THE PROJECT -->
## About The Project
<!-- PROJECT OVERVIEW -->
### Project résumé:
* Salary comparisson between **2020** and **2021** datasets.
* Created a tool that **estimates data related professions salaries** (MAE ~ $ 12K) to help data scientists negotiate their income when they get a job.
* **Scraped** over two datasets of 1000 job descriptions from glassdoor using python and selenium (**2020** and **2021**).
* Engineered features from the text of each job description to quantify the value companies put on **keywords** related to the data related professions for each year Some keywords: python, excel, aws, spark among others. 
* **Analyzed** many potential correlation for **others potential analysis objectives**.
* **ML** Algorithms optimized to reach the best model: Linear, Lasso, and Random Forest Regressors using GridsearchCV. 
* Built a ~~not so practical~~ client facing **API** using flask (a great experience that enjoyed).

<!-- BUILT WITH -->
### Built With
* **Python Version**: 3.8.8
* **Framework**: Anaconda (Jupyter Notebook and Spyder) and Kaggle Kernel.
* **Packages**: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle, statsmodels.
* **2020 dataset** and **the original idea**: 
    - Ken Jee code and DataSet: [ds_salary_proj](https://github.com/PlayingNumbers/ds_salary_proj) 
    - [Explanation videos](https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t)
* [**Ken Jee YouTube Video explaining his project**](https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t) 
* **Scraping**: You can find the original code (from [Ömer Sakarya](https://github.com/arapfaik)) here: 
    - [Github code](https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905).
    - [Explanation article](https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905).
* **Flask Productionization**: 
    - [Git Code](https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2)

 <h3 align="center">Many, MANY thanks Ken, Ömer and GeekDataGuy</h3>



<!-- INSTALLATION -->
## Installation 
Clone the repo
   ```sh
   git clone https://github.com/echestare/001KenJeeFromScratch_DSSalary.git
   ```
########################################
########################################


<!-- EXPLAINING STAGES -->
## Stages overview
<!-- WEB SCRAPING -->
### Web Scraping
The web scraped tweaked by Ken Jee was re-tweaked o updated by me (2021/09/30).
It was setted to scrape 1000+ job postings from glassdoor.com. The information extracted and stored as .csv is:
||||
|----------------|-------------------------------|-----------------------------|
|Job title|Salary Estimate|Job Description|
|Rating|Company|Location|
|Company Headquarters|Company Size|Company Founded Date|
|Type of Ownership|Industry|Sector|
|Revenue|Competitors|-|
||||

<!-- DATA CLEANING -->
### Data Cleaning

The data scraped needed to be cleaned up, so that it was usable for our model. 

 The following changes was made:
* Basic cleanings:
	* Drop duplicates and fill NaN values.
	* Remove first column (false index) and rows without salary.
	* Reset Index
* Parsed numeric data out of salary column as min, max and avg _salary:
	* Taked into account the hourly given salaries.
	* Added columns for employer provided salary and hourly wages.
* Parsed rating out of company text and removed undesired characters.
* Made a new column for company state and cleaned it.
* Transformed founded date into age of company 
* Made columns for if different skills were listed in the job description:

|||||||
|------------------|------------------|------------------|------------------|------------------|------------------|
|Python  |R|Spark|AWS|Excel|SQL|
|SAS|d3.js|Julia|Jupyter|Keras  |MatLab|
|MatPlotLib|PyTorch|Scikit-Learn|Tensor Flow|Weka|Selenium|
|Hadoop|Tableau|Power BI|BigML|RapidMiner|Apache Flink|
|DataRobot|SAP Hana|Mongo DB|Trifacta|MiniTab|Kafka|
|MicroStrategy|Google Analytics|SPSS|-|-|-|
||||||||
* Column for simplified Job Title.
* Column for Seniority:
	* by Jobs Title info and by Jobs Descriptoin info.
* Column for Job Description length
	* by quantity of letters and quantity of words
* Cleaned other columns:
	* Size
	* Type of ownership
	* Revenue
 
NOTE: In the EDA I added a new Column for quantity of keywords in Jobs Description.

<!-- EXPLORATORY DATA ANALYSIS-->
### Exploratory Data Analysis

The approach was to inspect each **categorical variable** and look for direct correlations with the salary distribution as well as between themself.
The analysis was extensive and interesting, but it is well explained in the respective notebook.
 ########################################
########################################

Finaly,  I reapeated each analysis with the new dataset. And compared main characteristics.

<!-- MODEL BUILDING-->
### Model Building

Working with the first dataset (2020) I splited the data into train (80%) and test (%20) and transformed cateorical variables into Dummy variables.

First, three models was evaluated using Mean Absolute Error, because it is not so sensible to attipical error and outliers in this model are not particularly bad.
Models used (I think Ken Jee approach is the correct):
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 

<!-- MODEL PERFORMANCE-->
### Model performance
########################################
########################################
```
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Random Forest** : MAE = 11.22
*	**Linear Regression**: MAE = 18.86
*	**Ridge Regression**: MAE = 19.67
```
########################################
########################################

### Productionization 


> I would say I get much fun doing this stage. Was quite interesting since I have not used Flask before. 
But, I must also say that the final results are not enought treated to be considered a good  finish.
Anyway, I leave it here for how much I enjoyed it


The description of this stage is:
>In this step, a flask API endpoint was built and was hosted on a local webserver by following along with the TDS. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 