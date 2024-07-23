from src.ingestion import DataIngestion
from src.utils import list_files, get_file_extension
import os

def main():
    ingestion = DataIngestion()
    input_dir = 'data/input'
    output_dir = 'data/output'

    for file in list_files(input_dir):
        file_path = os.path.join(input_dir, file)
        print(f"Ingesting file: {file}")

        try:
            df = ingestion.ingest_file(file_path)
            print(f"Ingested data shape: {df.shape}")

            output_file = f"{os.path.splitext(file)[0]}_processed.csv"
            output_path = os.path.join(output_dir, output_file)
            ingestion.save_data(output_path)
            print(f"Saved processed data to: {output_path}")

        except Exception as e:
            print(f"Error processing {file}: {str(e)}")

if __name__ == "__main__":
    main()