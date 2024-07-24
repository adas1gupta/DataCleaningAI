from google.cloud import pubsub_v1
import json

class PubSubPublisher:
    def __init__(self, project_id, topic_name):
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(project_id, topic_name)

    def publish_message(self, message):
        data = json.dumps(message).encode('utf-8')
        future = self.publisher.publish(self.topic_path, data)
        print(f"Published message ID: {future.result()}")

# Move this part inside the if block
if __name__ == '__main__':
    project_id = 'ai-data-cleaning-system'
    topic_name = 'raw-data-ingestion-topic'
    publisher = PubSubPublisher(project_id, topic_name)
    message = {"data": "Hello, Pub/Sub!"}
    publisher.publish_message(message)