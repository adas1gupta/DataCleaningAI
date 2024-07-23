import pandas as pd
import json
import xml.etree.ElementTree as ET

class DataIngestion:
    def __init__(self):
        # Initialize the data attribute to None
        self.data = None

    def ingest_csv(self, file_path):
        # Read a CSV file and store it in the data attribute
        self.data = pd.read_csv(file_path)
        return self.data

    def ingest_json(self, file_path):
        # Open and read a JSON file
        with open(file_path, 'r') as file:
            # Convert JSON to a pandas DataFrame and store it
            self.data = pd.json_normalize(json.load(file))
        return self.data

    def ingest_xml(self, file_path):
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Extract data from XML elements
        data = []
        for child in root:
            row = {}
            for elem in child:
                # Try to convert to int or float, fall back to string
                try:
                    row[elem.tag] = int(elem.text)
                except ValueError:
                    try:
                        row[elem.tag] = float(elem.text)
                    except ValueError:
                        row[elem.tag] = elem.text
            data.append(row)
        # Convert extracted data to a pandas DataFrame
        self.data = pd.DataFrame(data)
        return self.data

    def ingest_excel(self, file_path):
        # Read an Excel file and store it in the data attribute
        self.data = pd.read_excel(file_path)
        return self.data

    def ingest_file(self, file_path):
        # Get the file extension
        file_extension = file_path.split('.')[-1].lower()
        # Call the appropriate ingestion method based on file extension
        if file_extension == 'csv':
            return self.ingest_csv(file_path)
        elif file_extension == 'json':
            return self.ingest_json(file_path)
        elif file_extension == 'xml':
            return self.ingest_xml(file_path)
        elif file_extension in ['xls', 'xlsx']:
            return self.ingest_excel(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")

    def save_data(self, output_path, format='csv'):
        # Save the data to a file in the specified format
        if format == 'csv':
            self.data.to_csv(output_path, index=False)
        elif format == 'json':
            self.data.to_json(output_path, orient='records')
        elif format in ['xls', 'xlsx']:
            self.data.to_excel(output_path, index=False)
        else:
            raise ValueError(f"Unsupported output format: {format}")