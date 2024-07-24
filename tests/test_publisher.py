import unittest
from unittest.mock import patch, MagicMock
from src.publish_messages import PubSubPublisher

class TestPublisher(unittest.TestCase):

    @patch('google.cloud.pubsub_v1.PublisherClient')
    def setUp(self, mock_publisher):
        self.mock_publisher = mock_publisher
        self.project_id = 'test-project'
        self.topic_name = 'test-topic'
        self.publisher = PubSubPublisher(self.project_id, self.topic_name)

    def test_init(self):
        self.mock_publisher.assert_called_once()
        self.mock_publisher().topic_path.assert_called_once_with(self.project_id, self.topic_name)

    def test_publish_message(self):
        test_message = {'key': 'value'}
        mock_future = MagicMock()
        mock_future.result.return_value = 'message_id'
        self.mock_publisher().publish.return_value = mock_future

        self.publisher.publish_message(test_message)

        self.mock_publisher().publish.assert_called_once()
        call_args = self.mock_publisher().publish.call_args[0]
        self.assertEqual(call_args[0], self.publisher.topic_path)
        self.assertEqual(call_args[1], b'{"key": "value"}')

    @patch('builtins.print')
    def test_publish_message_print(self, mock_print):
        test_message = {'key': 'value'}
        mock_future = MagicMock()
        mock_future.result.return_value = 'message_id'
        self.mock_publisher().publish.return_value = mock_future

        self.publisher.publish_message(test_message)

        mock_print.assert_called_once_with("Published message ID: message_id")

if __name__ == '__main__':
    unittest.main()