import luigi
import os
import sentry_sdk

from pipeline.extract import ExtractProductData, ExtractSalesData, ExtractScrapedData
from pipeline.transform import TransformProductData, TransformSalesData, TransformScrapedData
from pipeline.load import LoadData

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Define and read env variables
SENTRY_DSN = os.getenv(f"SENTRY_DSN")

# Configure Sentry for alerting and track the error
sentry_sdk.init(
    dsn = f"{SENTRY_DSN}"
)

 # Run the ETL pipeline       
if __name__ == '__main__':
    luigi.build([ExtractProductData(),
                 ExtractSalesData(),
                 ExtractScrapedData(),
                 TransformProductData(),
                 TransformSalesData(),
                 TransformScrapedData(),
                 LoadData()])
    