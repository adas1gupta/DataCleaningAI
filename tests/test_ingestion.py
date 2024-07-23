import unittest
import pandas as pd
import os
from src.ingestion import DataIngestion

class TestDataIngestion(unittest.TestCase):
    def setUp(self):
        self.ingestion = DataIngestion()
        self.test_data_dir = 'tests/test_data'
        
        # Load the expected data from a reference CSV file
        self.expected_data = pd.read_csv(f'{self.test_data_dir}/reference_data.csv')

    def test_csv_ingestion(self):
        df = self.ingestion.ingest_file(f'{self.test_data_dir}/sample.csv')
        pd.testing.assert_frame_equal(df, self.expected_data)

    def test_json_ingestion(self):
        df = self.ingestion.ingest_file(f'{self.test_data_dir}/sample.json')
        pd.testing.assert_frame_equal(df, self.expected_data)

    def test_excel_ingestion(self):
        df = self.ingestion.ingest_file(f'{self.test_data_dir}/sample.xlsx')
        pd.testing.assert_frame_equal(df, self.expected_data)

    def test_xml_ingestion(self):
        df = self.ingestion.ingest_file(f'{self.test_data_dir}/sample.xml')
        pd.testing.assert_frame_equal(df, self.expected_data)

    def assert_dataframes_equal(self, df1, df2, msg=None):
        try:
            pd.testing.assert_frame_equal(df1, df2)
        except AssertionError as e:
            print("\nDataFrames are not equal. Differences:")
            print(e)
            print("\ndf1:")
            print(df1.dtypes)
            print(df1)
            print("\ndf2:")
            print(df2.dtypes)
            print(df2)
            self.fail(msg or "DataFrames are not equal")

if __name__ == '__main__':
    unittest.main()