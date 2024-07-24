import json
import time
import threading
from src.publish_messages import PubSubPublisher
from src.subscriber import PubSubSubscriber

class DataIngestionSystem:
    def __init__(self, project_id, topic_name, subscription_name):
        self.publisher = PubSubPublisher(project_id, topic_name)
        self.subscriber = PubSubSubscriber(project_id, subscription_name)

    def ingest_data(self, data):
        self.publisher.publish_message(data)

    def process_data(self, message):
        print(f"Received message: {message.data}")
        data = json.loads(message.data.decode('utf-8'))
        cleaned_data = self.clean_data(data)
        print(f"Cleaned data: {cleaned_data}")
        message.ack()

    def clean_data(self, data):
        cleaned_data = {k: v.strip() if isinstance(v, str) else v for k, v in data.items()}
        return cleaned_data

    def run(self):
        subscriber_thread = threading.Thread(target=self.subscriber.listen)
        subscriber_thread.start()

        for i in range(10):
            data = {
                'id': i,
                'timestamp': time.time(),
                'data': f'  Sample data {i}  '
            }
            self.ingest_data(data)
            time.sleep(1)

        subscriber_thread.join()

if __name__ == "__main__":
    project_id = 'ai-data-cleaning-system'
    topic_name = 'raw-data-ingestion-topic'
    subscription_name = 'raw-data-ingestion-subscription'
    ingestion_system = DataIngestionSystem(project_id, topic_name, subscription_name)
    ingestion_system.run()