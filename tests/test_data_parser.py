import unittest
from unittest.mock import patch, MagicMock
import src.data_parser as data_parser

class TestDataParser(unittest.TestCase):

    @patch('langchain.embeddings.OpenAIEmbeddings')
    @patch('langchain.vectorstores.redis.Redis')
    def test_embeddings_and_redis(self, mock_redis, mock_embeddings):
        # Test embeddings and Redis interactions
        mock_embeddings.return_value = MagicMock()
        mock_redis.from_documents.return_value = MagicMock()
        rds = data_parser.rds
        self.assertIsNotNone(rds)

if __name__ == '__main__':
    unittest.main()
