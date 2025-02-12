import unittest
from unittest.mock import patch, MagicMock
import api_functions

class TestAPIFunctions(unittest.TestCase):

    @patch('api_functions.requests.get')
    def test_get_anime_schedule_success(self, mock_get):
        # Test successful schedule retrieval
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test_schedule"}
        mock_get.return_value = mock_response

        result = api_functions.get_anime_schedule(mal_id=9919, day="monday")
        self.assertEqual(result, {"data": "test_schedule"})

    @patch('api_functions.requests.get')
    def test_get_anime_schedule_failure(self, mock_get):
        # Test schedule retrieval failure (non-200 response)
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = api_functions.get_anime_schedule(mal_id=9919, day="monday")
        self.assertIsNone(result)

    @patch('api_functions.requests.get')
    def test_get_anime_info_success(self, mock_get):
        # Test successful anime info retrieval with anime id 9919
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test_anime_info"}
        mock_get.return_value = mock_response

        result = api_functions.get_anime_info(9919)
        self.assertEqual(result, {"data": "test_anime_info"})

    @patch('api_functions.requests.get')
    def test_get_anime_info_not_found(self, mock_get):
        # Test anime info retrieval when anime is not found
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = api_functions.get_anime_info(999)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
