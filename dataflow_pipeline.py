import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
from apache_beam.io import ReadFromText, WriteToText

# Define the pipeline options
options = PipelineOptions()
options.view_as(StandardOptions).runner = 'DataflowRunner'
options.view_as(StandardOptions).project = 'ai-data-cleaning-system'
options.view_as(StandardOptions).region = 'us-central1'
options.view_as(StandardOptions).temp_location = 'gs://dcai-cluster-1/temp-cluster'

# Define a simple transformation function
def transform_data(element):
    return element.upper()

# Create the pipeline
with beam.Pipeline(options=options) as p:
    (p
     | 'ReadData' >> ReadFromText('gs://dcai-cluster-1/input/input-file.txt')  # Replace with your actual input file location
     | 'TransformData' >> beam.Map(transform_data)
     | 'WriteData' >> WriteToText('gs://dcai-cluster-1/output/output-file.txt')  # Replace with your desired output location
    )

print("Pipeline submitted.")