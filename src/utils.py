from src.ingestion import DataIngestion  # Importing the DataIngestion class from the src.ingestion module
from src.utils import list_files, get_file_extension  # Importing helper functions from the src.utils module
import os  # Importing the os module for interacting with the operating system

# Main function to ingest and process data files
def main():
    # Creating an instance of the DataIngestion class
    ingestion = DataIngestion()

    # Specifying the input directory where the data files are located
    input_dir = 'data/input'

    # Specifying the output directory where the processed files will be saved
    output_dir = 'data/output'

    # Looping through each file in the input directory
    for file in list_files(input_dir):
        # Constructing the full file path
        file_path = os.path.join(input_dir, file)

        # Printing a message indicating the file being ingested
        print(f"Ingesting file: {file}")

        try:
            # Ingesting the file and storing the data in a DataFrame
            df = ingestion.ingest_file(file_path)

            # Printing the shape of the ingested data
            print(f"Ingested data shape: {df.shape}")

            # Constructing the output file name by appending '_processed' to the original file name
            output_file = f"{os.path.splitext(file)[0]}_processed.csv"

            # Constructing the full output file path
            output_path = os.path.join(output_dir, output_file)

            # Saving the processed data to the output file
            ingestion.save_data(output_path)

            # Printing a message indicating where the processed data has been saved
            print(f"Saved processed data to: {output_path}")

        # Handling any exceptions that occur during the ingestion and saving process
        except Exception as e:
            # Printing an error message with the file name and the exception message
            print(f"Error processing {file}: {str(e)}")

# Ensuring that the main function is called only when the script is executed directly
if __name__ == "__main__":
    main()
