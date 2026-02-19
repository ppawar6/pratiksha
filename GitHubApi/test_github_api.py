import pytest
from unittest.mock import patch, MagicMock
from GitHubApi.github_api import get_repo_info


class TestGetRepoInfo:
    """Test suite for get_repo_info function"""
    
    @patch("GitHubApi.github_api.requests.get")
    def test_valid_user(self, mock_get):
        """Test retrieving repos and commits for a valid user"""
        # Mock repos response
        repos_response = MagicMock()
        repos_response.status_code = 200
        repos_response.json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        
        # Mock commits responses
        commits_response_1 = MagicMock()
        commits_response_1.status_code = 200
        commits_response_1.json.return_value = [{"id": "1"}, {"id": "2"}, {"id": "3"}]
        
        commits_response_2 = MagicMock()
        commits_response_2.status_code = 200
        commits_response_2.json.return_value = [{"id": "1"}]
        
        mock_get.side_effect = [repos_response, commits_response_1, commits_response_2]
        
        result = get_repo_info("testuser")
        
        assert result == [("repo1", 3), ("repo2", 1)]
        assert mock_get.call_count == 3
    
    @patch("GitHubApi.github_api.requests.get")
    def test_invalid_user(self, mock_get):
        """Test handling of non-existent user (404 response)"""
        repos_response = MagicMock()
        repos_response.status_code = 404
        mock_get.return_value = repos_response
        
        result = get_repo_info("nonexistentuser")
        
        assert result == []
    
    @patch("GitHubApi.github_api.requests.get")
    def test_empty_repo_list(self, mock_get):
        """Test user with no repositories"""
        repos_response = MagicMock()
        repos_response.status_code = 200
        repos_response.json.return_value = []
        mock_get.return_value = repos_response
        
        result = get_repo_info("userwithnorepos")
        
        assert result == []
    
    @patch("GitHubApi.github_api.requests.get")
    def test_api_error(self, mock_get):
        """Test handling of API errors (500 response)"""
        repos_response = MagicMock()
        repos_response.status_code = 500
        mock_get.return_value = repos_response
        
        result = get_repo_info("testuser")
        
        assert result == []
    
    @patch("GitHubApi.github_api.requests.get")
    def test_request_exception(self, mock_get):
        """Test handling of network/request exceptions"""
        import requests
        mock_get.side_effect = requests.RequestException("Connection error")
        
        result = get_repo_info("testuser")
        
        assert result == []
    
    @patch("GitHubApi.github_api.requests.get")
    def test_commit_api_error(self, mock_get):
        """Test handling when commits API returns error"""
        repos_response = MagicMock()
        repos_response.status_code = 200
        repos_response.json.return_value = [{"name": "repo1"}]
        
        commits_response = MagicMock()
        commits_response.status_code = 403
        
        mock_get.side_effect = [repos_response, commits_response]
        
        result = get_repo_info("testuser")
        
        assert result == [("repo1", 0)]
