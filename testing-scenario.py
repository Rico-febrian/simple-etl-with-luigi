import luigi
import pandas as pd

from pipeline.utils_function.db_connector import dwh_load_engine
from pipeline.extract import ExtractProductData, ExtractSalesData, ExtractScrapedData
from pipeline.transform import TransformProductData, TransformSalesData, TransformScrapedData
from pangres import upsert


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
       
        
 # Run the ETL pipeline       
if __name__ == '__main__':
    luigi.build([ExtractProductData(),
                 ExtractSalesData(),
                 ExtractScrapedData(),
                 TransformProductData(),
                 TransformSalesData(),
                 TransformScrapedData(),
                 LoadData()])
    