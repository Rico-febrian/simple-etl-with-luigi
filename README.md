<<<<<<< HEAD
# ***Creating a Simple ETL Pipeline with LUIGI***

Hi there!, Welcome to my project. In this guide, I will explain how to develop a simple ETL pipeline based on a common use case

---

# Project Background
**A company wants to improve its sales performance by embarking on a digital transformation. To achieve this, they need to enhance data quality to enable more effective analysis and decision-making**

Based on this background, we can begin building the solution by following these steps:

# 1. Requirement Gathering
During the requirements gathering stage, I discussed with users and key stakeholders to understand the following:

- **Understanding how the business works**, including business workflows and overall operations.

- **Assessing the source data condition**, including data quality checks, validation, and data format.

- **Evaluating the business situation** to determine if implementation is feasible at this time and whether the company has sufficient budget

---

### User Problem
After discussing with the user, it turns out that the user has the following problem:
=======
# ***How I Built an ETL Pipeline Based on a Case Study***

**Hi there, Welcome to learning logs!**

As part of my ongoing career switch journey to data engineering, I’ve recently been learning about data wrangling, especially I learned about the steps as a Data Engineer takes to build an ETL pipeline.

**To track my progress and solidify my understanding, I created this project to share what I've learned.**

---
---

# Project Objective

In this project, I’ll explain the steps I’ve learned to build and ETL Pipeline, including:

**- Requirements Gathering**
  
**- Propose a Solution**

**- Implement the Solution:** ---> Click here if you want to jump into the main guide
>>>>>>> 6dc961e (Update: README, main pipeline and testing script)

  - Scraping additional data using Python
  - Developing an ETL pipeline using Python
  - Orchestrating the ETL pipeline with Luigi
  - Automating the ETL pipeline with Cron
  - Testing the pipeline

**These steps are based on a case study from an E-commerce business.**

<<<<<<< HEAD
### Main Problem

Based on the issues identified by users, there are 3 main problems:

- **Scattered Data**: Data is fragmented across different sources, including the database and CSV files.

- **Data Quality Issues**: The source data is messy, contains many missing values, and has inconsistent formatting.

- **Lack of Data for Research**: The Data Science team lacks sufficient data to build NLP models and needs additional data from online sources for effective analysis.

---

# 2. Proposed Solution
After understanding how the business operates, the condition of the data sources, and the main problems, **the next step is to discuss with the user to propose solutions and methods that are suitable for the company's current conditions**. Here's the proposed solution:

- **Data Integration**: Integrate all data into a centralized data warehouse to provide a single source of truth.

- **Data Quality Improvement**: Implement data cleaning and transformation processes to handle missing values and ensure data consistency across all sources.

- **Supplementary Data Collection**: Use web scraping techniques to gather additional data required by the Data Science team for NLP modeling.

- **Automated ETL Pipeline**: Develop an automated ETL (Extract, Transform, Load) pipeline using LUIGI to ensure that data is consistently updated and accessible to all relevant teams.

# 3. Implement a Solution
 Once the users and stakeholders agree with the proposed solution, we can proceed to implement it.

### - Create ETL Pipeline
=======
---
---

# Case Study Background

**A growing company seeks to enhance analytics effectiveness to boost sales performance. To achieve this, they aim to improve their current data quality for better analysis and decision-making.**

---
---

# Dataset Overview

There are three types of datasets I used in this project:  

- **Sales data:** Stored in a database. You can access the dataset here: [sales-dataset](https://hub.docker.com/r/shandytp/amazon-sales-data-docker-db).  
- **Marketing data:** Provided as a CSV file. You can access the dataset here: [marketing-dataset](https://drive.google.com/file/d/1J0Mv0TVPWv2L-So0g59GUiQJBhExPYl6/view?usp=sharing).  
- **Web-scraped data:** I collected this data through web scraping, which I explain in detail below.

---
---

# Workflows

Here's the workflow I followed while building this project:

![project workflow]()

---
---
>>>>>>> 6dc961e (Update: README, main pipeline and testing script)

**Alright, let's begin!**

<<<<<<< HEAD
- **Extract**: Read data from each source and save it to a CSV file.

- **Transform**: Validate, clean, and transform each dataset based on user requirements.

- **Load**: Load all transformed data into a single data warehouse
=======
# Requirements Gathering

The very first step in this process is requirements gathering. **The main goal is to gain a deep understanding of the business problem, stakeholders’ needs, and the business itself.**

In reality, **this is a long and iterative process**. However, **let’s assume I’ve already discussed with the stakeholders**, and here’s my understanding so far:

---

## Understanding the Business
 
 **- Business Model:** The company adopted the Business-to-consumer (B2C) and Consumer-to-consumer (C2C).
 
 **- Business Type:** The company business type is E-commerce.
 
 **- Key Business Process:**
   
   - Order processing
   - Inventory management
   - Revenue management
   - Customer service

 **- Business High-priority Metrics/KPI's:**
  
   - **Sales performance:**

     Monitor revenue on a daily, monthly, and yearly basis
   
   - **Profitability analysis:**

     Evaluate which products, customer segments, or other factors are most profitable to refine business strategies.
   
   - **Customer segmentation:**

     Identify customer groups based on purchasing habits, demographics, and other factors.
   
   - **Sales forecasting:**

     Predicting future sales trends and demand to optimize business strategies.

---

## Understanding the Problem

  After discussing with the user, it turns out that the user has the following problem:

  - The Marketing team wants to analyze the sales performance of electronic products over the past 2 years. However, **the sales data is scattered across various sources with inconsistent and messy contents**.

  - The Data Science team aims to build a Natural Language Processing (NLP) model to analyze market trends for electronic products. However, **the current data is insufficient for model building and they need a supplementary data from online sources, which they currently don't have**. 

  Based on the issues identified by users, **there are three current main problems**:

  - **Scattered data**:

    Data is fragmented across different sources, including the database and CSV files.
  
  - **Data quality issues**:

    The source data is messy, contains many missing values, and has inconsistent formatting.
  
  - **Lack of data for research**:

    The Data Science team needs additional data to build a NLP model.

---
 
 ## Understanding the Needs of Stakeholders & Users
 
 **- Retrieve data quickly:**
 
 Stakeholders want an easy and fast access to the data anytime. 
 
 **- Improve data quality:**
 
 Users require a clean, accurate, and reliable data for analytics.
 
 **- Daily data updates:**
 
 Users need daily data updates for regular needs (such as meetings) and unexpected requests.
 
 **- Additional data for research:**
 
 The Data Science team requires extra data to build an NLP model
 
 **- Cost efficiency and scalability:**
 
 With limited funds, stakeholders prefer a low-cost, scalable solution that allows experimentation before larger investments

---

## Understanding the Current Data Source

- Sales data
- Marketing data
>>>>>>> 6dc961e (Update: README, main pipeline and testing script)

---



---
---

# Propose a Solution

After a long and iterative requirements gathering process, **let’s assume the stakeholders have agreed to this proposed solution, despite its advantages and disadvantages:**

**- Build an ETL Pipeline**
 
 - Integrate all data source into a centralized data warehouse for quick and easy access.
 - Clean and transform data to improve data quality across all sources.
 - Automate ETL Pipeline with Cron for daily updates

**- Web Scraping**

 - Use web scraping to collect additional data.

---
---

After reaching an agreement on the proposed solution, we can move onto the implementation stage. However, **before we begin scraping the web and building the ETL pipeline, take a look at the requirements below**: 

## Requirements

- OS:
    - Linux
    - WSL (Windows Subsystem For Linux)
      
- Tools:
    - Dbeaver (using postgreSQL)
    - Docker
    - Cron
      
- Programming Language:
    - Python
    - SQL
      
- Python Libray:
    - Luigi
    - Pandas
    - Playwright
    - Beautifulsoup4

 **Make sure these tools are installed and set up before starting the implementation!**.
      
---

# Implement a Solution: Web Scraping

**!! DISCLAIMER !!**

**ALL INFORMATION FROM WEB SCRAPING IN THIS PROJECT IS ONLY DONE FOR LEARNING PURPOSES!** 

**DO NOT USE WEB SCRAPING FOR CRIMINAL ACTIVITIES. ALWAYS CHECK THE TERM & CONDITIONS OF A WEBSITE BEFORE DO A WEB SCRAPING!**

**[!! CHECK THIS BEFORE SCRAPING !!](https://webscraping.ai/faq/aliexpress-scraping/is-there-a-limit-to-the-amount-of-data-i-can-scrape-from-aliexpress#:~:text=Terms%20of%20Service%3A%20Before%20you,the%20service%20you%20are%20using.)**

**!! DISCLAIMER !!**

---
 
## Run the Scraping Script

For this project, I scraped data from **[AliExpress.com](https://best.aliexpress.com/?browser_redirect=true)** to gather information aligned with the data science team's needs.

To scrape data, simply run the [scrape.py]() script to extract HTML data from the selected website.

```
python scrape.py
```

**The scraped data is saved as an HTML file, which will be processed and transformed during the ETL process**. You can check the scraped output here: [scraped-output]()

**For the full guide and documentation about web scraping you can check my other repository:** [scrape-data]().

---
---

# Implement a Solution: Build an ETL Pipeline

## Preparations

### - Get the dataset

- Sales dataset
  
  - Create and run Docker Compose with this image to get the sales dataset: [sales-dataset](https://hub.docker.com/r/shandytp/amazon-sales-data-docker-db)
  - Check here to see my docker compose configuration: [sales-docker-compose]()

- Marketing dataset

  Download this CSV file to get the marketing dataset: [marketing-dataset](https://drive.google.com/file/d/1J0Mv0TVPWv2L-So0g59GUiQJBhExPYl6/view?usp=sharing)

---

### - Setup project environment

Create and activate python environment to isolate project dependencies.

```
python -m venv your_project_name         
source your_project_name/bin/activate    # On Windows: your_project_name\Scripts\activate
```

---

### - Set up a directory structure

Set up your project directory structure to organize all project scripts.
  
  ```
  project/
  ├── dataset/ ------------------- # To store dataset
  ├── log/ ----------------------- # To store pipeline logs
  ├── scraping_output/ ----------- # To store scraping output data 
  │
  ├── src/ 
  │   └── helper/ ---------------- # To store utility function   
  ├── temp/ ---------------------- # To store temporary data from ETL task 
  │   ├── extract/
  │   ├── transform/
  │   └── load/
  │ ------------------------------ # Root project to store the main scripts
  │ 
  ├── .env
  ├── main_etl_pipeline.py 
  ├── pipeline.sh
  ├── scrape.py
  ├── docker-compose.yml
  └── requirements.txt
  ```

---

### - Install _requirements.txt_ in the created environment**
  
  ```
  pip install -r requirements.txt
  ```
  
**Note: You can install libraries as needed while developing the code. However, once complete, make sure to generate a _requirements.txt_ file listing all dependencies**.

---

### - Create _.env_ file

Create .env file to store all credential information.
  
  ```
  touch .env
  ```

---
---

## Developing the ETL Scripts

### - Setup Warehouse Database

  - Create a [docker-compose.yml]() configuration to set up warehouse database.
  
  - Store database credentials in _.env_ file.

    ```
    # Sales Data Source
    SRC_POSTGRES_DB=[YOUR SOURCE DB NAME]
    SRC_POSTGRES_HOST=localhost
    SRC_POSTGRES_USER=[YOUR USERNAME]
    SRC_POSTGRES_PASSWORD=[YOUR PASSWORD]
    SRC_POSTGRES_PORT=[YOUR PORT]
    
    # Data Warehouse
    DWH_POSTGRES_DB=[YOUR DWH DB NAME] 
    DWH_POSTGRES_HOST=localhost
    DWH_POSTGRES_USER=[YOUR USERNAME]
    DWH_POSTGRES_PASSWORD=[YOUR PASSWORD]
    DWH_POSTGRES_PORT=[YOUR PORT]
    ```
 
  - Run the _docker-compose.yml_ file 

<<<<<<< HEAD
- [Product data transformation requirements](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/user_requirements/product_data_requirements.txt)
- [Sales data transformation requirements](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/user_requirements/sales_data_requirements.txt)
- [Scraped data transformartion requirements](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/user_requirements/scraped_data_requirements.txt)

---
  
## - Integrate and Automate ETL Pipeline 

- **Data Integration**: The Load task in the ETL process integrates data from various sources into a single data warehouse, ensuring that all teams have easy access to the necessary information.

- **Automated Data Updates**: Set up automatic scheduling with "crontab" for ETL processes to ensure that the data in the database is consistently updated. [ETL Pipeline Script for Automate](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/etl_pipeline.sh)

---

## - Web Scraping

**!! DISCLAIMER! !**

**INFORMATION FROM WEB SCRAPING IS ONLY DONE FOR LEARNING PURPOSES, NOT FOR CRIMINAL ACTIVITIES**

Scrape data from websites that provide information related to electronic products or sales, as required by the Data Scientist team. In this project, data was scraped from the e-commerce website, Aliexpress.com.

**ALWAYS CHECK THE TERM & CONDITIONS OF A WEBSITE BEFORE DO A WEB SCRAPING!**

**[!! CHECK THIS BEFORE SCRAPING !!](https://webscraping.ai/faq/aliexpress-scraping/is-there-a-limit-to-the-amount-of-data-i-can-scrape-from-aliexpress#:~:text=Terms%20of%20Service%3A%20Before%20you,the%20service%20you%20are%20using.)**
=======
    ```
    docker-compose up -d
    ```

  - Connect the database to Dbeaver
    - Click **Database** > select **New Database Connection**
    - Select postgreSQL
    - Fill in the port, database, username, and password **as defined in your _.env_**
    - Click **Test Connection**
    - If no errors appear, the database connection is successful

---

### - Create utility functions

  **This utility function acts like a basic tool you can use repeatedly when building the pipeline script.**

  -  [Database connector]()
      -  Function to connect python and the database

---

### - Create ELT Pipeline task

Take a look at this image below
>>>>>>> 6dc961e (Update: README, main pipeline and testing script)

---

<<<<<<< HEAD
## - How the ETL Pipeline Works
=======
>>>>>>> 6dc961e (Update: README, main pipeline and testing script)

I developed each task separately to ensure everything function properly.

 - **EXTRACT Task**

<<<<<<< HEAD
This task will extract data from each source and save the output into CSV files. 
=======
   **The main goal of this task is to read dataset from each source and save it to a CSV file**.
>>>>>>> 6dc961e (Update: README, main pipeline and testing script)

    - Extract product data (CSV)
      
      - Read the product data and save it as a CSV file using Pandas.
    
    - Extract sales data (PostgreSQL Database)
    
      - Connect to sales database.
      - Create SQL query to read all data and save it as a CSV file using Pandas.
      
    - Extract scraped data (HTML file)
  
      - Open and parse the HTML file using Beautifulsoup4.
      - Convert the parsed data into DataFrame and save it as a CSV file using Pandas.

   **Ensure that all extracted data is saved in the selected directory, as it will be used in the Transform task!**
   
   Check here for the full Extract task: [extract-task]()

---

 - **TRANSFORM Task**

<<<<<<< HEAD
[Full ETL Pipeline Code](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/etl.py#L12)

***ETL Dependency Graph***

![etl_pipeline](assets/dag_graph.png)

---

## - Testing Scenario
=======
   **The main goal of this task is to validate, clean, and transform each extracted dataset based on user requirements**.

   These requirements are defined during the requirements gathering. Assume the user has determined the requirements, check here to see the assumed user requirements: [transformation requirements](https://github.com/Rico-febrian/simple-etl-with-luigi/tree/main/user_requirements)

    - Transform product data (CSV)
      
    - Transform sales data (CSV)
         
    - Transform scraped data (CSV)

   All three task above follow the same process:
    
    - Read the extracted data.
    
    - Validate the data.
    
    - Clean and transform the data based on the user requirements. 

   **Ensure that all transformed data is saved in the selected directory, as it will be used in the Load task!**
   
   Check here for the full Transform task: [transform-task]()

---

 - **LOAD Task**

   **The main goal of this task is to load all transformed data into the relevant tables in the data warehouse**.

   There is only one task: **Load Data**. Here's the task process:
    
    - Connect to warehouse database.
    
    - Read all transformed data
    
    - Define the table name for each dataset
      
    - Load each transformed data into the warehouse database 
   
   Check here for the full Load task: [load-task]()

---
---

## Orchestrating the Pipeline with Luigi

**NOTE: Luigi has some limitations you should be aware of when using it for data orchestration, such as:**

- History Task Retention (only 15 minutes by default)
- Idempotency Requirement
- No Built-in Scheduler

For a detailed explanation, you can check the documentation: [Luigi Limitations](https://luigi.readthedocs.io/en/stable/design_and_limitations.html)

### - Compile all task

Compile all task into a single main script, like this: [main_elt_pipeline.py]()

### - Run the ELT Pipeline

Run the main script to test the pipeline end-to-end
```
python YOUR_MAIN_PIPELINE_NAME.py
```

**NOTE: When developed the script you can run the Luigi task separately**
```
# In your task script, run this:
if __name__ == '__main__':
     luigi.build(<TASK NAME>()])
```

**Or you can execute all of them at once**
```
# In your final task script, run this:
if __name__ == '__main__':
     luigi.build([<TASK A>(),
                  <TASK B>(),
                  ..........
                  <UNTIL YOUR LAST TASK>()])
```

### - Verify all outputs
If your pipeline runs successfully, you can verify it in DBeaver by checking the warehouse database

---
---

# Implement the Solution: Automate the Pipeline with Cron

Since Luigi doesn't have a built-in scheduler, you can automate the pipeline using Cron

## Set up schedulers

- Create a cron job to automate pipeline execution.
  
  - Create shell script [elt_pipeline.sh](https://github.com/Rico-febrian/elt-dwh-for-online-bookstore-business/blob/main/elt_pipeline.sh)
    ```
    touch SHELL_SCRIPT_NAME.sh
    ```
    
    In SHELL_SCRIPT_NAME.sh, write this:
    ```
    #!/bin/bash
    
    # Virtual Environment Path
    VENV_PATH="/PATH/TO/YOUR/VIRTUAL/ENVIRONMENT/bin/activate"
    
    # Activate Virtual Environment
    source "$VENV_PATH"
    
    # Set Python script
    PYTHON_SCRIPT="/PATH/TO/YOUR/MAIN/PIPELINE/SCRIPT/main_elt_pipeline.py"
    
    # Run Python Script 
    python "$PYTHON_SCRIPT"
    ```

  - Make the script executable
    ```
    # In your shell script directory, run this
    chmod +x SHELL_SCRIPT_NAME.sh
    ```
  - Set up cron job
    ```
    # Open crontab
    crontab -e
    ```
    ```
    # In crontab editor

    # Set the schedule like this to run the pipeline EVERY HOUR
    0 * * * * /PATH/TO/YOUR/SHELL/SCRIPT/SHELL_SCRIPT_NAME.sh
    ```
  - Or you can run the shell script manually
    ```
    ./SHELL_SCRIPT_NAME.sh
    ```
  
---
---

# Implement the Solution: Testing Scenario

>>>>>>> 6dc961e (Update: README, main pipeline and testing script)
To test the robustness of the ETL pipeline, we will perform an UPSERT process. In this scenario, new data will be added to the sales database. This test will ensure that the ETL pipeline operates according to its schedule and can successfully retrieve and integrate the latest data.

- Add New Data: Insert new data into the sales database.

- Check Data Warehouse Before Update: Verify the current state of the data warehouse before performing updates.

- Modify Load Task: Adjust the Load task to ensure it updates the data warehouse with the new data.

- Check Updated Data Warehouse: Verify the data warehouse after the update to confirm that the new data has been correctly integrated.

Data warehouse **before adding a new record** in the sales database.
![Before](https://github.com/user-attachments/assets/ee9f3305-0049-4cf1-8d7a-133abce8acaa)

Data warehouse **after upsert**
![AFter](https://github.com/user-attachments/assets/b1b6a105-fd9a-407e-8527-89d89417a694)

[Testing Scenario Code](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/testing-scenario.py)

---
<<<<<<< HEAD

# - Tools
The following tools were used to create this project:

- Python
- Pandas
- Playwright
- Pangres
- Luigi
- Docker
- PostgreSQL
=======
---

# Final Result

## Luigi DAG Graph

![etl_pipeline](assets/dag_graph.png)

---
---
# Conclusion

Well, you’ve reached the end of this guide. In summary, I’ve shared my learning journey in data engineering, focusing on web scraping and building an ETL pipeline using Python orchestrated by Luigi, based on a case study in the E-commerce business. 

**For the full article about this project you can check out my article on Medium here:** [full-story]().

Thank you for joining me on this learning experience. I hope you’ve gained valuable insights that will help you in your own data engineering journey. If you have any questions or need additional information, feel free to reach out. I’m open to any feedback or suggestions you may have.

**You can connect with me on:** 

- [My LinkedIn](www.linkedin.com/in/ricofebrian)
- [My Medium](https://medium.com/@ricofebrian731)
>>>>>>> 6dc961e (Update: README, main pipeline and testing script)
