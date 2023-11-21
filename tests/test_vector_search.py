import unittest
from unittest.mock import patch, MagicMock
from src import vector_search

class TestVectorSearch(unittest.TestCase):

    @patch('src.vector_search.rds.similarity_search')
    def test_similarity_search(self, mock_search):
        # Mocking Redis similarity_search response
        mock_response = MagicMock()
        mock_response.page_content = "Test content"
        mock_search.return_value = [mock_response]

        # Test similarity_search function
        results = vector_search.rds.similarity_search("query")
        self.assertEqual(results[0].page_content, "Test content")

if __name__ == '__main__':
    unittest.main()
