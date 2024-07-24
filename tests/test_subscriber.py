import unittest
from unittest.mock import patch, MagicMock
from src.subscriber import PubSubSubscriber

class TestSubscriber(unittest.TestCase):

    @patch('google.cloud.pubsub_v1.SubscriberClient')
    def setUp(self, mock_subscriber):
        self.mock_subscriber = mock_subscriber
        self.project_id = 'test-project'
        self.subscription_name = 'test-subscription'
        self.subscriber = PubSubSubscriber(self.project_id, self.subscription_name)

    def test_init(self):
        self.mock_subscriber.assert_called_once()
        self.mock_subscriber().subscription_path.assert_called_once_with(self.project_id, self.subscription_name)

    @patch('builtins.print')
    def test_callback(self, mock_print):
        mock_message = MagicMock()
        mock_message.data = b'test message'

        self.subscriber.callback(mock_message)

        mock_print.assert_called_once_with("Received message: b'test message'")
        mock_message.ack.assert_called_once()

    @patch('builtins.print')
    def test_listen(self, mock_print):
        mock_future = MagicMock()
        self.mock_subscriber().subscribe.return_value = mock_future

        # Simulate KeyboardInterrupt to exit the listening loop
        mock_future.result.side_effect = KeyboardInterrupt()

        self.subscriber.listen()

        self.mock_subscriber().subscribe.assert_called_once_with(
            self.subscriber.subscription_path, callback=self.subscriber.callback
        )
        mock_print.assert_called_with(f"Listening for messages on {self.subscriber.subscription_path}")
        mock_future.cancel.assert_called_once()

if __name__ == '__main__':
    unittest.main()