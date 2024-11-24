# ***How I Built an ETL Pipeline Based on a Case Study***

![ETL Pipeline Design](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/assets/etl_pipeline_design.png)

**Hi there, Welcome to learning logs!**

As part of my ongoing career switch journey to data engineering, I’ve recently been learning about data wrangling, especially I learned about the steps as a Data Engineer takes to build an ETL pipeline.

**To track my progress and solidify my understanding, I created this project to share what I've learned.**

---
---

## Table of Contents

- [Project Objective](https://github.com/Rico-febrian/simple-etl-with-luigi?tab=readme-ov-file#project-objective)
  
- [Case Study Background](https://github.com/Rico-febrian/simple-etl-with-luigi?tab=readme-ov-file#case-study-background)
  
- [Dataset Overview](https://github.com/Rico-febrian/simple-etl-with-luigi?tab=readme-ov-file#dataset-overview)
  
- [Workflows](https://github.com/Rico-febrian/simple-etl-with-luigi?tab=readme-ov-file#workflows)
  
- [Requirements Gathering](https://github.com/Rico-febrian/simple-etl-with-luigi?tab=readme-ov-file#requirements-gathering)
  
- [Propose a Solution](https://github.com/Rico-febrian/simple-etl-with-luigi?tab=readme-ov-file#propose-a-solution)
  
- [Implement the Solution](https://github.com/Rico-febrian/simple-etl-with-luigi?tab=readme-ov-file#requirements)
  
- [Final Result](https://github.com/Rico-febrian/simple-etl-with-luigi?tab=readme-ov-file#final-result)
  
- [Conclusion](https://github.com/Rico-febrian/simple-etl-with-luigi?tab=readme-ov-file#final-result)

---
---

# Project Objective

In this project, I’ll explain the steps I’ve learned to build and ETL Pipeline, including:

**- Requirements Gathering**
  
**- Propose a Solution**

**- Implement the Solution:**

  - Scraping additional data using Python
  - Developing an ETL pipeline using Python
  - Orchestrating the ETL pipeline with Luigi
  - Automating the ETL pipeline with Cron
  - Testing the pipeline

**These steps are based on a case study from an E-commerce business.**

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

![project workflow](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/assets/project_workflows.png)

---
---

**Alright, let's begin!**

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

### - Sales data

The current sales data is stored in a PostgreSQL database.

- Data Structure and Format

  - Schema Structure: Single schema (public), all data is stored in one main table.
  
  - Data Types: All columns use VARCHAR.

- Data Flow

  The current source data is collected from an e-commerce platform:

  - Batch file uploads (e.g., daily exports from a transactional system).

  - APIs sending transactional data periodically or in real-time.

  Update Frequency: Daily updates to ensure the data stays relatively fresh.

- Data Volume and Growth Trends

  - The current data consists of approximately 100,000+ rows across one main table.
  
  - Data Growth: The data is expected to grow moderately (e.g., 1,000–10,000 rows per month).

- Data Quality

  - Missing values in the ratings and no_of_ratings columns.
  
  - Duplicate records and value are present in many columns.
  
  - Many column names are unclear, making it difficult to understand their purpose.
  
  - The table does not have a primary key to ensure record uniqueness.
  
---

### - Marketing data

The current marketing data is stored in a CSV file.

- Data Structure and Format

  - Data Types: A mix of VARCHAR, FLOAT, and BOOLEAN.

- Data Flow

  The current source data is collected from marketing campaigns, including:

  - Campaign tracking tools (e.g., Google Ads, Facebook Ads).

  - Surveys and feedback forms.
    
  - Email marketing platforms (e.g., Mailchimp, SendGrid).

  Update Frequency: Data is updated weekly to capture the latest marketing performance and customer interactions.

- Data Volume and Growth Trends

  - The current data consists of approximately 7,000+ rows across one main table.

  - Data Growth: The data is expected to grow at a moderate pace, around 500–1,000 rows per month, as new marketing campaigns and feedback are added.

- Data Quality

  - Missing values in some columns.
  
  - No duplicated records, but duplicate values are present in many columns.
  
  - Many column names are unclear, making it difficult to understand their purpose.

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

 > [!NOTE]
 > **Make sure these tools are installed and set up before starting the implementation!**.
      
---

# Implement a Solution: Web Scraping

> [!WARNING]
> **ALL INFORMATION FROM WEB SCRAPING IN THIS PROJECT IS ONLY DONE FOR LEARNING PURPOSES!**
>
> **DO NOT USE WEB SCRAPING FOR CRIMINAL ACTIVITIES. ALWAYS CHECK THE TERM & CONDITIONS OF A WEBSITE BEFORE DO A WEB SCRAPING!**
>
> **[!! CHECK THIS BEFORE SCRAPING !!](https://webscraping.ai/faq/aliexpress-scraping/is-there-a-limit-to-the-amount-of-data-i-can-scrape-from-aliexpress#:~:text=Terms%20of%20Service%3A%20Before%20you,the%20service%20you%20are%20using.)**

---

For this project, I scraped data from **[AliExpress.com](https://best.aliexpress.com/?browser_redirect=true)** to gather information aligned with the data science team's needs.

## Run the Scraping Script

To scrape data for this project, simply run the [scrape.py](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/scrape.py) script to extract HTML data from the selected website.

```
python scrape.py
```

**For a complete guide and documentation on how I scraped the data, check my other repository:** [scraping-ecommerce-web](https://github.com/Rico-febrian/scraping-ecommerce-website).

**The scraped output data is saved as an HTML file. This scraped output will be used in the ETL process.** Check the scraped output here: [scraped-output](https://github.com/Rico-febrian/simple-etl-with-luigi/tree/main/scraping_output)

---
---

# Implement a Solution: Build an ETL Pipeline

## Preparations

### - Get the dataset

- Sales dataset
  
  - Use Docker Compose with the provided image to get the sales dataset: [sales-dataset](https://hub.docker.com/r/shandytp/amazon-sales-data-docker-db)
  - For the explanation how to run Docker Compose are explain below.

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
  ├── helper/ -------------------- # To store SQL query schema
  ├── log/ ----------------------- # To store pipeline logs
  ├── scraping_output/ ----------- # To store scraping output data 
  │
  ├── pipeline/ ------------------ # To store ETL task script and utility function
  │   └── utils_function/
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

  > [!NOTE]
  > **You can install libraries or packages as needed while developing the code.**
  >
  > **However, once the development is complete, make sure to generate a requirements.txt file to list all the dependencies.**.

---

### - Create _.env_ file

Create .env file to store all credential information.
  
  ```
  touch .env
  ```

---

### - Set up Sentry for alerting

Set up a Sentry project to receive an e-mail notifications in case of any errors in the pipeline.

  - Open and signup to: https://www.sentry.io 
  - Create Project :
    - Select Platform : Python
    - Set Alert frequency : `On every new issue`
    - Create project name.
  - After create the project, **store the SENTRY DSN project key into the .env file**

---

### - Setup Database

  - Use Docker Compose to set up the sales and warehouse databases:
  
    - Warehouse Docker Compose configuration: [dwh-docker-compose](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/docker-compose-warehouse-db.yaml)
    
    - Sales Docker Compose configuration: [sales-docker-compose](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/docker-compose-sales-db.yaml)
  
  - Store each database credentials in _.env_ file.

    ```
    # Sales Data Source
    SRC_POSTGRES_DB=[YOUR SALES DB NAME]
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
 
  - Run the _docker compose_ file 

    ```
    # Run this command if you're using the default configuration
    docker-compose up -d
    
    # Or use this command if you need to specify a custom Docker Compose file
    docker-compose -f YOUR_DOCKER_COMPOSE_FILE_NAME up -d
    ```

  - Connect the database to Dbeaver

    - Click **Database** > select **New Database Connection**

    - Select postgreSQL

    - Fill in the port, database, username, and password **as defined in your _.env_**

    - Click **Test Connection**

    - If no errors appear, the database connection is successful

---

### - Create utility functions

  > [!NOTE]
  > **This utility function acts like a basic tool you can use repeatedly when building the pipeline script.**

  -  [Database connector](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/pipeline/utils_function/db_connector.py)
      
      -  Function to connect python and the database.

---
---

## Developing the ETL Scripts

Take a look at the image below to see how the ETL pipeline works:

![ETL Pipeline Workflow](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/assets/simple_etl_design.png)

---

### - Create ETL Pipeline task

I developed each task separately to ensure everything function properly.

 - **EXTRACT Task**

   **The main goal of this task is to read dataset from each source and save it to a CSV file**.

    - Extract product data (CSV)
      
      - Read the product data and save it as a CSV file using Pandas.
    
    - Extract sales data (PostgreSQL Database)
    
      - Connect to sales database.
      - Create SQL query to read all data and save it as a CSV file using Pandas.
      
    - Extract scraped data (HTML file)
  
      - Open and parse the HTML file using Beautifulsoup4.
      - Convert the parsed data into DataFrame and save it as a CSV file using Pandas.

   **Ensure that all extracted data is saved in the selected directory, as it will be used in the Transform task!**
   
   Check here for the full Extract task: [extract-task](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/pipeline/extract.py)

---

 - **TRANSFORM Task**

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
   
   Check here for the full Transform task: [transform-task](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/pipeline/transform.py)

---

 - **LOAD Task**

   **The main goal of this task is to load all transformed data into the relevant tables in the data warehouse**.

   There is only one task: **Load Data**. Here's the task process:
    
    - Connect to warehouse database.
    
    - Read all transformed data
    
    - Define the table name for each dataset
      
    - Load each transformed data into the warehouse database 
   
   Check here for the full Load task: [load-task](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/pipeline/load.py)

---
---

## Orchestrating the Pipeline with Luigi

> [!CAUTION]
> **Luigi has some limitations you should be aware of when using it for data orchestration, such as:**
> 
> - History Task Retention (only 15 minutes by default)
>   
> - Idempotency Requirement
>   
> - No Built-in Scheduler
>   
> - For a detailed explanation, you can check the documentation: [Luigi Limitations](https://luigi.readthedocs.io/en/stable/design_and_limitations.html)

### - Compile all task

Compile all task into a single main script, like this: [main_etl_script](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/etl.py)

### - Run the ETL Pipeline

Run the main script to test the pipeline end-to-end
```
python YOUR_MAIN_PIPELINE_NAME.py
```

> [!NOTE]
> **When developed the script you can run the Luigi task separately**
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

If your pipeline runs successfully, you can verify the output in DBeaver by checking the warehouse database.

---
---

# Implement the Solution: Automate the Pipeline with Cron

Since Luigi doesn't have a built-in scheduler, you can automate the pipeline using Cron.

## Set up schedulers

- Create a cron job to automate pipeline execution.
  
  - Create shell script
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

  Check here for the full shell script: [elt_pipeline.sh](https://github.com/Rico-febrian/elt-dwh-for-online-bookstore-business/blob/main/elt_pipeline.sh)

---
---

# Implement the Solution: Testing Scenario

To test whether the ETL pipeline works properly, I performed a simple testing process. The goal of this test is to ensure that the ETL pipeline runs on schedule and successfully retrieves and integrates the latest data.

**Watch this video to see the simulation of the testing scenario: [watch-here](https://youtu.be/M_WQtG4Oe4E)**

In this scenario, I followed these steps:

- Add new data to the sales database.

  ```
  insert into amazon_sales_data ("name", main_category, sub_category, image, link, ratings, no_of_ratings, discount_price, actual_price)
  values ('Testing Product Data', 'Testing Category', 'Testing Sub Category', 'https://sekolahdata-assets.s3.ap-southeast-1.amazonaws.com/notebook-images/mde intro-to-data-eng/testing_image.png', 'https://pacmann.io/', 5, 30, 450, 1000)
  ```

- Check current data in the data warehouse before making updates.

- Modify the Load task in the ETL script to update the data warehouse with the new data using the Pangres package. Alternatively, you can create a new script for testing based on the modified ETL script.

  Check here to see my modified ETL script for the testing scenario: [testing-script](https://github.com/Rico-febrian/simple-etl-with-luigi/blob/main/testing-scenario.py)

- Delete all temporary Load data if it is saved without a timestamp to ensure the Luigi task runs properly, **as it relies on idempotency**.

- Run the modified ETL script or testing script.

- Check the data warehouse again to verify if the new data is added correctly.

---
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