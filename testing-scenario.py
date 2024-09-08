import luigi
import pandas as pd
from bs4 import BeautifulSoup
from src.helper.db_connector import sales_database_engine, dwh_load_engine
from pangres import upsert

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
        



# Luigi task for transform the product data
class TransformProductData(luigi.Task):
    
    def requires(self):
        """
        This task depends on the "ExtractProductData" task and requires the CSV file produced by that task.
        
        """
        return ExtractProductData()
    
    def output(self):
        """
        Specifies the path where the transformed product data file will be saved.
        
        """
        return luigi.LocalTarget('/home/ricofebrian/projects/simple-etl/output_data/transform/transformed_product_data.csv')
    
    def run(self):
        """
        Main function to read, validate, clean and transform the product data then export it to a CSV file.
        
        """
        # Read the output file from "ExtractedProductData" task
        with self.input().open('r') as raw_product_data:
            product_data = pd.read_csv(raw_product_data)
        
        # Drop unused column
        # Specify the column to be dropped from the product data
        drop_cols = ['upc', 'weight', 'prices.sourceURLs', 'ean', 'imageURLs', 'keys', 'prices.shipping', 
                     'dateAdded', 'dateUpdated','manufacturer', 'manufacturerNumber', 'Unnamed: 26', 
                     'Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30']

        # Drop the column
        product_data = product_data.drop(columns=drop_cols, axis=1)

        # Transform "amountMax" and "amountMin" columns
        # Get the average value from "amountMax" and "amountMin" columns, then store it in a new column called "avg_price"
        product_data['avg_price'] = product_data[['prices.amountMax', 'prices.amountMin']].mean(axis=1).round(2)

        # Drop "amountMax" and "amountMin" columns
        product_data = product_data.drop(columns=['prices.amountMax', 'prices.amountMin'], axis=1)

        # Transform "availability" column
        def mapping_availability_cols(value):
            """
            This function used to map the new values to the 'availability' column.
            
            """
            # Convert the values to a lowercase
            value = value.strip().lower()
            
            # Define the new mapping for values
            true_value = ['yes', 'in stock', 'true', 'more on the way', 'special order', 'sold', '32 available', '7 available']
            false_value = ['no', 'out of stock', 'false', 'retired']
            
            # Map the new values to boolean based on stock availability
            if value in true_value:
                return True
            
            elif value in false_value:
                return False
            
            else:
                return None

        # Apply the function to update the current data
        product_data['prices.availability'] = product_data['prices.availability'].apply(mapping_availability_cols)

        # Cast the data type to boolean
        product_data['prices.availability'] = product_data['prices.availability'].astype(bool)

        # Transform "condition" column
        def mapping_condition_cols(value):
            """
             This function used to map the new values to the 'condition' column.
   
            """
            # Convert the values to lowercase
            value = value.strip().lower()
            
            # Define the new mapping for values
            new_value = ['new', 'new other (see details)']
            used_value = ['used', 'pre-owned', 'refurbished']
            refurbished_value = ['seller refurbished', 'refurbished', 'manufacturer refurbished']
            
            # Map the new values based on the current product condition
            if value in new_value:
                return 'New'
            
            elif value in used_value:
                return 'Used'
            
            elif value in refurbished_value:
                return 'Refurbished'
            
            else:
                return "Detailed Description"

        # Apply the function to update the current data
        product_data['prices.condition'] = product_data['prices.condition'].apply(mapping_condition_cols)

        # Transform "dateSeen" column
        def get_latest_date(date_str):
            """
            This function is used to extract the latest date from 'dateSeen' column.
            
            """
            try:
                
                # Split the string value by comma
                date_list = date_str.split(',')

                # Convert all dates to a datetime
                dates = pd.to_datetime(date_list, errors='coerce')
            
                # Get the latest date and return it
                latest_date = dates.max()
                
                return latest_date
            
            except Exception as e:
                print(f'Error: {e}')
                return None

        # Apply the function to update the current data
        product_data['prices.dateSeen'] = product_data['prices.dateSeen'].apply(get_latest_date)

        # Change the datetime format
        product_data['prices.dateSeen'] = product_data['prices.dateSeen'].dt.strftime('%Y-%m-%d')

        # Cast the data type to datetime
        product_data['prices.dateSeen'] = product_data['prices.dateSeen'].astype('datetime64[ns]')

        # Transform "merchant" column
        # Convert the values to a lowercase
        product_data['prices.merchant'] = product_data['prices.merchant'].str.lower()

        # Transform "brand" column
        # Convert the values to a lowercase
        product_data['brand'] = product_data['brand'].str.lower()

        # Transform "categories" column
        # Convert the values to a lowercase
        product_data['categories'] = product_data['categories'].str.lower()

        # Transform "name" column
        # Convert the values to a lowercase
        product_data['name'] = product_data['name'].str.lower()

        # Transform "primaryCategories" column
        # Change the values to "electronics"
        product_data['primaryCategories'] = 'electronics'

        # Rename the columns
        # Specify the column to be renamed from the product data
        rename_cols = {
            'id' : 'product_code',
            'name' : 'product_name',
            'prices.availability' : 'stock_availability',
            'prices.condition' : 'condition',
            'prices.currency' : 'price_currency',
            'prices.dateSeen' : 'latest_date',
            'prices.isSale' : 'is_sale',
            'prices.merchant' : 'merchant',
            'categories' : 'sub_category',
            'primaryCategories' : 'main_category',
            'sourceURLs' : 'source_url'
        }

        # Update the data
        product_data = product_data.rename(columns=rename_cols)

        # Mapping the columns
        # Define the order of columns to be mapped
        mapping_cols = [
            'product_code',
            'product_name',
            'stock_availability',
            'condition',
            'avg_price',
            'price_currency',
            'is_sale',
            'brand',
            'merchant',
            'main_category',
            'sub_category',
            'asins',
            'source_url',
            'latest_date'
        ]

        # Update the data
        product_data = product_data[mapping_cols]
        
        # Drop the duplicated data
        product_data = product_data.drop_duplicates()
        
        # Export the transformed data to a CSV
        product_data.to_csv(self.output().path, index=False)
    
    
            
        
# Luigi task for transform the sales data
class TransformSalesData(luigi.Task):
    
    def requires(self):
        """
        This task depends on the ExtractSalesData task and requires the CSV file produced by that task.
        
        """
        return ExtractSalesData()
    
    def output(self):
        """
        Specifies the path where the transformed sales data file will be saved.
        
        """
        return luigi.LocalTarget('/home/ricofebrian/projects/simple-etl/output_data/transform/transformed_sales_data.csv')
    
    def run(self):
        """
        Main function to read, validate, clean and transform the sales data then export it to a CSV file.
        
        """
        
        # Read the output file from "ExtractedSalesData" task
        with self.input().open('r') as raw_sales_data:
            sales_data = pd.read_csv(raw_sales_data)
            
        # Drop unused column
        # Specify the column and drop it from the sales data
        drop_cols = ['image', 'Unnamed: 0']
        sales_data = sales_data.drop(columns=drop_cols, axis=1)

        # Transform "name" column
        # Convert the values to a lowercase
        sales_data['name'] = sales_data['name'].str.lower()

        # Transform "main_category" column
        # Specify the values to be mapped
        category_mapping = {
            
            "women's clothing": "women's fashion",
            "men's clothing": "men's fashion",
            "men's shoes": "men's fashion",
            "women's shoes": "women's fashion",
            "kids' fashion": "kid's fashion",
            'sports & fitness': 'sports & outdoor',
            'accessories': 'jewelry & accessories',
            'appliances': 'electronics',
            'tv, audio & cameras': 'electronics',
            'car & motorbike': 'automotive & motorcycle',
            'stores': 'retail store',
            'grocery & gourmet foods': 'food & beverages',
            'music': 'film & music',
            'home, kitchen, pets': 'home & kitchen',
            "toys & baby products": "toys & baby",
            
            # Categories that are not mapped
            'beauty & health': 'beauty & health',
            'home & kitchen' : 'home & kitchen',
            'bags & luggage': 'bags & luggage',
            'pet supplies': 'pet supplies',
            'industrial supplies': 'industrial supplies'
        }

        # Update the data 
        sales_data['main_category'] = sales_data['main_category'].map(category_mapping)

        # Transform "sub_category" column
        # Convert the values to a lowercase
        sales_data['sub_category'] = sales_data['sub_category'].str.lower()

        # Transform "ratings" column
        # Remove non-numeric characters using a regex pattern
    
        # Set regex pattern to extract specific digits
        get_digit = r'(\d+\.\d+|\b[0-5]\b)'

        # Extract and update the data using the regex pattern
        sales_data['ratings'] = sales_data['ratings'].str.extract(get_digit)
        
        # Cast the data type to a numeric
        sales_data['ratings'] = pd.to_numeric(sales_data['ratings'], errors='coerce')

        # Transform "no_of_ratings" column
        # Remove non-numeric characters using a regex pattern and update the data
        sales_data['no_of_ratings'] = sales_data['no_of_ratings'].str.replace(r'\D', '', regex=True)
        
        # Cast the data type to a numeric
        sales_data['no_of_ratings'] = pd.to_numeric(sales_data['no_of_ratings'], errors='coerce')

        # Transform "discount_price" and "actual_price" column
        # Remove non-numeric characters using a regex pattern and update the data
        sales_data['discount_price'] = sales_data['discount_price'].str.replace(r'\D', '', regex=True)
        sales_data['actual_price'] = sales_data['actual_price'].str.replace(r'\D', '', regex=True)

        # Cast the data type to a numeric
        sales_data['discount_price'] = pd.to_numeric(sales_data['discount_price'], errors='coerce')
        sales_data['actual_price'] = pd.to_numeric(sales_data['actual_price'], errors='coerce')

        # Convert the price from INR to USD
        # Set the exchange rate from INR to USD
        usd_rate = 0.012

        # Convert the values in the 'discount_price' and 'actual_price' columns to USD
        discount_to_usd = round(sales_data['discount_price'] * usd_rate, 2)
        actual_to_usd = round(sales_data['actual_price'] * usd_rate, 2)
        
        # Update the data with the converted values
        sales_data['discount_price'] = discount_to_usd 
        sales_data['actual_price'] = actual_to_usd 

        # Create new column to store the price currency
        sales_data['price_currency'] = 'USD'

        # Rename the columns
        # Specify the column to be renamed from the sales data
        rename_cols = {
            'name' : 'product_name',
            'link' : 'source_url',
            'ratings' : 'rating_value',
            'no_of_ratings' : 'ratings_received'
        }

        # Update the data
        sales_data = sales_data.rename(columns=rename_cols)

        # Mapping the columns
        # Define the order of columns to be mapped
        mapping_cols = ['product_name', 'actual_price', 'discount_price', 'price_currency', 'rating_value',
                        'ratings_received', 'main_category', 'sub_category', 'source_url']

        # Update the data
        sales_data = sales_data[mapping_cols]

        # Handle missing values in the "actual_price" column
        # Impute missing values with the median value for each main category

        # Group the sales data by the "main_category" column
        sales_by_category = sales_data.groupby(by='main_category')

        # Get the median value for each category
        get_median_price = sales_by_category['actual_price'].transform('median')

        # Impute missing values in "actual_price" column with the median values from each main category
        sales_data.loc[:, 'actual_price'] = sales_data['actual_price'].fillna(get_median_price)

        # Handle missing values in the "discount_price" column
        # Impute missing values with zero (no discount)
        sales_data.loc[:, 'discount_price'] = sales_data['discount_price'].fillna(0)
        
        # Handle missing values in the "ratings_received" column
        # Drop rows with missing values in the "ratings_received" column
        sales_data = sales_data.dropna(subset='ratings_received')
        
        # Drop duplicated data
        sales_data = sales_data.drop_duplicates()

        # Export the transformed sales data to a CSV
        sales_data.to_csv(self.output().path, index=False) 



# Luigi task for transform the scraped data
class TransformScrapedData(luigi.Task):
    
    def requires(self):
        """
        This task depends on the ExtractScrapedData task and requires the CSV file produced by that task.
        
        """
        return ExtractScrapedData()
    
    def output(self):
        """
        Specifies the path where the transformed scraped data file will be saved.
        
        """
        return luigi.LocalTarget('/home/ricofebrian/projects/simple-etl/output_data/transform/transformed_scraped_data.csv')
    
    def run(self):
        """
        Main function to read, validate, clean and transform the scraped data then export it to a CSV file.
        
        """
        
        # Read the output file from "ExtractedScrapedData" task
        with self.input().open('r') as raw_scraped_data:
            scraped_data = pd.read_csv(raw_scraped_data)
            
        # Transform "title" column
        # Convert the values to a lowercase
        scraped_data['title'] = scraped_data['title'].str.lower()

        # Transform "price" column
        # Remove the '$' character and generate a new column named 'price_currency'"
        scraped_data['price'] = scraped_data['price'].str.replace('$', '')

        # Cast the data type to a numeric
        scraped_data['price'] = scraped_data['price'].astype(float)

        # Generate new column to store a price currency 
        scraped_data['price_currency'] = 'USD'

        # Rename the columns
        # Specify the column to be renamed from the product data
        rename_cols = {
            'title' : 'listing_title',
            'url' : 'source_url'
        }

        # Update the data
        scraped_data = scraped_data.rename(columns=rename_cols)
        
        # Mapping the columns
        # Define the order of columns to be mapped
        mapping_cols = [
            'listing_title',
            'price',
            'price_currency',
            'rating',
            'source_url'
        ]

        # Update the data
        scraped_data = scraped_data[mapping_cols]
        
        # Export the transformed scraped data to a CSV
        scraped_data.to_csv(self.output().path, index=False)
    



# Luigi task to load the transformed data into the database
class LoadData(luigi.Task):
    
    def requires(self):
        """
        This task depends on all the transformation tasks and requires each CSV file produced by those tasks.
        
        """
        return [TransformProductData(), 
                TransformSalesData(),
                TransformScrapedData()]
        
    def output(self):
        """
        Specify the path where all the loaded data files will be saved.
        
        """
        return [luigi.LocalTarget('/home/ricofebrian/projects/simple-etl/output_data/load/load_product_data.csv'),
                luigi.LocalTarget('/home/ricofebrian/projects/simple-etl/output_data/load/load_sales_data.csv'),
                luigi.LocalTarget('/home/ricofebrian/projects/simple-etl/output_data/load/load_scraped_data.csv')]

    def run(self):
        """
        Main function to load the selected updated data from sales database into the data warehouse.
        
        """
        
        try:
            # Init database engine connection
            engine = dwh_load_engine()
            
            # Read the output file from each tranformation task
            load_product_data = pd.read_csv(self.input()[0].path)
            load_sales_data = pd.read_csv(self.input()[1].path)
            load_scraped_data = pd.read_csv(self.input()[2].path)
            
            # Add a 'sales_id' column with sequential numbers starting from 1
            load_sales_data.insert(0, 'sales_id', range(1, 1 + len(load_sales_data)))
            
            # Set 'sales_id' as the index of the DataFrame
            load_sales_data.set_index('sales_id', inplace=True)

            # Init table name for each task
            product_data_table = 'product_data'
            sales_data_table = 'sales_data'
            scraped_data_table = 'scraped_data'
            
            # Upsert data into database using pangres upsert
            upsert(con=engine, df=load_sales_data, table_name=sales_data_table, if_row_exists='update')         
        
        except Exception as e:
            print(f'Error: {e}')
            
        # Save the process output
        load_product_data.to_csv(self.output()[0].path, index=False)
        load_sales_data.to_csv(self.output()[1].path, index=False)
        load_scraped_data.to_csv(self.output()[2].path, index=False)
        
 # Run the pipeline       
if __name__ == '__main__':
    luigi.build([ExtractProductData(),
                 ExtractSalesData(),
                 ExtractScrapedData(),
                 TransformProductData(),
                 TransformSalesData(),
                 TransformScrapedData(),
                 LoadData()])
    