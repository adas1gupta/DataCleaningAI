# AI Data Cleaning System

This project implements an AI-powered data cleaning system that can handle various file formats

## Features

- Flexible data ingestion (CSV, JSON, XML, Excel)
- Data profiling and analysis
- Machine learning-based cleaning
- Data transformation
- Data validation

## Installation

1. **Clone the repository:** 
    ```
    git clone https://github.com/adas1gupta/ai-data-cleaning-system.git
    cd ai-data-cleaning-system
    ```
2. **Install the required dependencies:**
    ```
    pip install -r requirements.txt
    ```
3. **Set up Google Cloud credentials:**
    ```
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
    ```
## Usage

### Data Ingestion

To ingest data, replace `path/to/your/file.csv` with the path to your data file in `src/ingestion.py`:

```python
from src.ingestion import DataIngestion

ingestion = DataIngestion()
df = ingestion.ingest_file('path/to/your/file.csv')
```
## Running the Data Cleaning System

To run the entire data cleaning system, you need to use your specific Google Cloud project details:

```python
from src.data_ingestion_system import DataIngestionSystem

# Replace these with your actual Google Cloud project details
project_id = 'your-project-id'  # e.g., 'my-data-project-12345'
topic_name = 'your-topic-name'  # e.g., 'raw-data-ingestion-topic'
subscription_name = 'your-subscription-name'  # e.g., 'raw-data-ingestion-subscription'

ingestion_system = DataIngestionSystem(project_id, topic_name, subscription_name)
ingestion_system.run()
```
## Publishing Messages

To publish messages to the Pub/Sub topic:

```python
from src.publish_messages import PubSubPublisher

# Replace these with your actual Google Cloud project details
project_id = 'your-project-id'  # e.g., 'my-data-project-12345'
topic_name = 'your-topic-name'  # e.g., 'raw-data-ingestion-topic'
subscription_name = 'your-subscription-name'  # e.g., 'raw-data-ingestion-subscription'

publisher.publish_message(message)
subscriber.listen()
```