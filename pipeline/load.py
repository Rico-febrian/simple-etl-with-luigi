import luigi
import pandas as pd
from utils_function.db_connector import dwh_load_engine
from extract import ExtractProductData, ExtractSalesData, ExtractScrapedData
from transform import TransformProductData, TransformSalesData, TransformScrapedData


# Luigi task to load the transformed data into the database
class LoadData(luigi.Task):
    
    # To keep track of new data without replacing existing data in the ETL process, you can use timestamps
    # current_timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
    # get_current_timestamp = luigi.Parameter(default=current_timestamp)
    
    # You can add a timestamp in the output file like this:
    # luigi.LocalTarget(f'/home/data_path/load_product_data_{self.get_current_timestamp}.csv')
    
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
        return [luigi.LocalTarget(f'/home/ricofebrian/projects/simple-etl/output_data/load/load_product_data.csv'),
                luigi.LocalTarget(f'/home/ricofebrian/projects/simple-etl/output_data/load/load_sales_data.csv'),
                luigi.LocalTarget(f'/home/ricofebrian/projects/simple-etl/output_data/load/load_scraped_data.csv')]

    def run(self):
        """
        Main function to load all transformed data into a each table in the data warehouse.
       
        """
        
        try:
            # Init database engine connection
            engine = dwh_load_engine()
            
            # Read the output file from each tranformation task
            load_product_data = pd.read_csv(self.input()[0].path)
            load_sales_data = pd.read_csv(self.input()[1].path)
            load_scraped_data = pd.read_csv(self.input()[2].path)
            
            # Init table name for each task
            product_data_table = 'product_data'
            sales_data_table = 'sales_data'
            scraped_data_table = 'scraped_data' 
        
            # Insert each transformed data into the database
            load_product_data.to_sql(name=product_data_table,
                                     con=engine,
                                     if_exists='append',
                                     index=False)
            
            load_sales_data.to_sql(name=sales_data_table,
                                   con=engine,
                                   if_exists='append',
                                   index=False)
            
            load_scraped_data.to_sql(name=scraped_data_table,
                                     con=engine,
                                     if_exists='append',
                                     index=False)
        
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
    