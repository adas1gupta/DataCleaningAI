from src.ingestion import DataIngestion
from src.utils import list_files, get_file_extension
import os
import pandas as pd
import json
import xml.etree.ElementTree as ET
import unittest

class TestDataIngestion(unittest.TestCase):
    def setUp(self):
        self.ingestion = DataIngestion()
        self.test_data_dir = 'tests/test_data'

    def test_csv_ingestion(self):
        csv_file = os.path.join(self.test_data_dir, 'sample.csv')
        df = self.ingestion.ingest_file(csv_file)
        self.assertIsInstance(df, pd.DataFrame)
        # Add more specific tests based on your CSV content

    def test_json_ingestion(self):
        json_file = os.path.join(self.test_data_dir, 'sample.json')
        df = self.ingestion.ingest_file(json_file)
        self.assertIsInstance(df, pd.DataFrame)
        # Add more specific tests based on your JSON content

    def test_excel_ingestion(self):
        excel_file = os.path.join(self.test_data_dir, 'sample.xlsx')
        df = self.ingestion.ingest_file(excel_file)
        self.assertIsInstance(df, pd.DataFrame)
        # Add more specific tests based on your Excel content

    def test_xml_ingestion(self):
        xml_file = os.path.join(self.test_data_dir, 'sample.xml')
        df = self.ingestion.ingest_file(xml_file)
        self.assertIsInstance(df, pd.DataFrame)
        # Add more specific tests based on your XML content

if __name__ == '__main__':
    unittest.main()