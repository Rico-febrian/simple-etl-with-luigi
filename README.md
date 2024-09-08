# Simple ETL Pipeline with LUIGI

In this project, I will explain how to develop a simple ETL pipeline based on a common use case

# Project Background
A company wants to improve its sales performance by embarking on a digital transformation. To achieve this, they need to enhance data quality to enable more effective analysis and decision-making

**Based on this background, we can begin building the solution by following these steps:**

# Requirement Gathering
During the requirements gathering stage, I discussed with users and key stakeholders to understand the following:

- Understanding how the business works, including business workflows and overall operations.

- Assessing the source data condition, including data quality checks, validation, and data format.

- Evaluating the business situation to determine if implementation is feasible at this time and whether the company has sufficient budget

## User Problem
After discussing with the user, it turns out that the user has the following problem:

- The Marketing team wants to analyze the sales performance of electronic products over the past 2 years. However, **the sales data is scattered across various sources, including databases and CSV files with inconsistent and messy contents. Many values are missing, and the formatting is inconsistent**.

- The Data Science team aims to build a Natural Language Processing (NLP) model to analyze market trends for electronic products. However, **the current data is insufficient for model building, poorly structured, and contains many missing values. Additionally, the team needs supplementary data from online sources, such as product reviews and descriptions, which they currently do not have**. 

## Main Problem

Berdasarkan problem dari user, terdapat 3 problem utama, yaitu:

- Scattered Data: Data is fragmented across different sources, including the database and CSV files.

- Data Quality Issues: The source data is messy, contains many missing values, and has inconsistent formatting.

- Lack of Data for Research: The Data Science team lacks sufficient data to build NLP models and needs additional data from online sources for effective analysis.

# Proposed Solution
After understanding how the business operates, the condition of the data sources, and the main problems, **the next step is to discuss with the user to propose solutions and methods that are suitable for the company's current conditions**. Here's the proposed solution:

- Data Integration: Integrate all data into a centralized data warehouse to provide a single source of truth.

- Data Quality Improvement: Implement data cleaning and transformation processes to handle missing values and ensure data consistency across all sources.

- Supplementary Data Collection: Use web scraping techniques to gather additional data required by the Data Science team for NLP modeling.

- Automated ETL Pipeline: Develop an automated ETL (Extract, Transform, Load) pipeline using LUIGI to ensure that data is consistently updated and accessible to all relevant teams.

# Implement a Solution
 Once the users and stakeholders agree with the proposed solution, we can proceed to implement it.

## Create ETL Pipeline

![etl_pipeline](assets/etl_pipeline.png)

- Extract: Read data from each source and save it to a CSV file.

- Transform: Validate, clean, and transform each dataset based on user requirements.

- Load: Load all transformed data into a single data warehouse


**Transformation requirements**
    
After discussing the data source conditions with each user, they provided requirements for handling and transforming each data source, here's the requirements:

- Product data transformation requirements

link....

- Sales data transformation requirements

link.....

- Scraped data transformartion requirements

link.... 

## Integrate and Automate ETL Pipeline 

- Data Integration: The Load task in the ETL process integrates data from various sources into a single data warehouse, ensuring that all teams have easy access to the necessary information.

- Automated Data Updates: Set up automatic scheduling with "crontab" for ETL processes to ensure that the data in the database is consistently updated.

## Web Scraping

**!! DISCLAIMER! !**

**INFORMATION FROM WEB SCRAPING IS ONLY DONE FOR LEARNING PURPOSES, NOT FOR CRIMINAL ACTIVITIES**

Scrape data from websites that provide information related to electronic products or sales, as required by the Data Scientist team. In this project, data was scraped from the e-commerce website, Aliexpress.com.

**ALWAYS CHECK THE TERM & CONDITIONS OF A WEBSITE BEFORE DO A WEB SCRAPING**

**Link**


## How the ETL Pipeline Works

The ETL pipeline invlolves several key tasks:

**Extract**
- Extract Product Data
- Extract Sales Data
- Extract Scraped Sata

This task will extract data from each source and save the output into CSV files

**Transform**
- Transform Product Data
- Transform Sales Data
- Transform Scraped Data

This task will validate, clean, and transform data based on the user requirements.

**Load**
- Load data

This final task will load the transformed data into a data warehouse.

- Snippet code dari masing-masing task

- ETL graph


## Testing Scenario
To test the robustness of the ETL pipeline, we will perform an UPSERT process. In this scenario, new data will be added to the sales database. This test will ensure that the ETL pipeline operates according to its schedule and can successfully retrieve and integrate the latest data.

- Add New Data: Insert new data into the sales database.

- Check Data Warehouse Before Update: Verify the current state of the data warehouse before performing updates.

- Modify Load Task: Adjust the Load task to ensure it updates the data warehouse with the new data.

- Check Updated Data Warehouse: Verify the data warehouse after the update to confirm that the new data has been correctly integrated.


# Tools
Tools: Python, Pandas, Luigi, Docker dan PostgreSQL

