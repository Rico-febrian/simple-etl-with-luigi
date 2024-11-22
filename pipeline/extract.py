import luigi
import pandas as pd

from bs4 import BeautifulSoup
from .utils_function.db_connector import sales_database_engine


# Luigi task for extract the product data
class ExtractProductData(luigi.Task):
    
    def requires(self):
        """
        Define the required dependencies for this task. 
        If there are no dependencies from the previous task, skip to the next task using pass.
        
        """
        pass
    
    def output(self):
        """
        Specifies the output target for this task. 
        The output is the path where the extracted product data will be saved.
        
        """
        return luigi.LocalTarget('/home/ricofebrian/projects/simple-etl/output_data/extract/extract_product_data.csv')
        
    def run(self):
        """
        Main function to read the product data and export it to a CSV file
        
        """
        # Read the product data  
        product_data = pd.read_csv('dataset/ElectronicsProductsPricingData.csv')
        
        # Export to CSV
        product_data.to_csv(self.output().path, index=False)
        

# -------------------------------------------------------------------------------------------------------------------------- #


# Luigi task for extract the sales data       
class ExtractSalesData(luigi.Task):
    
    def requires(self):
        """
        Define the required dependencies for this task. 
        If there are no dependencies from the previous task, skip to the next task using pass.
        
        """
        pass
    
    def output(self):
        """
        Specifies the output target for this task. 
        The output is the path where the extracted sales data will be saved.
        
        """
        return luigi.LocalTarget('/home/ricofebrian/projects/simple-etl/output_data/extract/extract_sales_data.csv')
        
    def run(self):
        """
        Main function to read the sales data from database and export it to a CSV file
        
        """
        
        # Init database engine
        engine = sales_database_engine()
        
        # Create query to read the data
        query = 'SELECT * FROM amazon_sales_data'
        
        # Read the sales data from the database
        extract_sales_data = pd.read_sql(sql=query, con=engine) 
        
        # Export to CSV
        extract_sales_data.to_csv(self.output().path, index=False)
        

# -------------------------------------------------------------------------------------------------------------------------- #


# Luigi task for parse and extract the scraped data       
class ExtractScrapedData(luigi.Task):
    
    def requires(self):
        """
        Define the required dependencies for this task. 
        If there are no dependencies from the previous task, skip to the next task using pass.
        
        """
        pass
    
    def output(self):
        """
        Specifies the output target for this task. 
        The output is the path where the extracted scraped data will be saved.
        
        """
        return luigi.LocalTarget('/home/ricofebrian/projects/simple-etl/output_data/extract/extract_scraped_data.csv')
        
    def run(self):
        """
        Main function to read and parse the scraped data and export it to a CSV file
        
        """
        
        try:
            # Read and create beautifulsoup object for parsing the scraped HTML data
            with open('scraping_output/ali-express-scrape-us.html', 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')
            
            # Get all listings from scraped HTML data
            get_item_list = soup.find_all('div', class_= 'recommend-card--card-wrap--2jjBf6S')

            # Define an empty list to store the extracted data for each listing
            full_data = []

            # Iterate each item through all item listing
            for item in get_item_list:
                
                # Get title of the listing
                get_title = item.find('div', attrs={'title' : True}).text
                
                # Get price of the listing
                get_price = item.find('span', class_= 'rc-modules--price--1NNLjth').text
                
                # Get rating of the listing
                get_rating = item.find('div', class_= 'rc-modules--stars--o9mzAea').get('title')
                
                # Get url of the listing
                get_url = item.find('a', class_= 'recommend-card--recommend-card--36CHUyg').get('href')
                
                # Map the extracted data into a dictionary
                data = {
                    'title' : get_title,
                    'price' : get_price,
                    'rating' : get_rating,
                    'url' : get_url
                }
                
                # Append the mapped data to the full data list
                full_data.append(data)
            
        except Exception as e:
            print(f'Error: {e}')
        
        # Convert scraped data into a dataframe
        scrape_data = pd.DataFrame(full_data)
        
        # Export to CSV
        scrape_data.to_csv(self.output().path, index=False)
        
        
        
 # Run the Extract task     
if __name__ == '__main__':
    luigi.build([ExtractProductData(),
                 ExtractSalesData(),
                 ExtractScrapedData()])
    