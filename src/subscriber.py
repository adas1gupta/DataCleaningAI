from google.cloud import pubsub_v1

class PubSubSubscriber:
    def __init__(self, project_id, subscription_name):
        self.subscriber = pubsub_v1.SubscriberClient()
        self.subscription_path = self.subscriber.subscription_path(project_id, subscription_name)

    def callback(self, message):
        print(f"Received message: {message.data}")
        message.ack()

    def listen(self):
        streaming_pull_future = self.subscriber.subscribe(
            self.subscription_path, callback=self.callback
        )
        print(f"Listening for messages on {self.subscription_path}")
        try:
            streaming_pull_future.result()
        except KeyboardInterrupt:
            streaming_pull_future.cancel()