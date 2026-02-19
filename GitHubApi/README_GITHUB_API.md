# GitHub API Assignment
[![Python CI](https://github.com/ppawar6/pratiksha/actions/workflows/ci.yml/badge.svg)](https://github.com/ppawar6/pratiksha/actions/workflows/ci.yml)

## Overview
This program retrieves repository information and commit counts for a GitHub user using the public GitHub REST API.

## Files
- `github_api.py` - Main program with `get_repo_info()` function
- `test_github_api.py` - Test suite using pytest and unittest.mock

## Requirements
- Python 3
- requests module
- pytest (for running tests)

## Installation
```bash
pip install requests pytest
```

## Usage

### Running the program
```bash
python github_api.py
```
Enter a GitHub username when prompted. The program will display all repositories and their commit counts.

Example:
```
Enter GitHub user ID: torvalds
Repo: linux Number of commits: 61605
Repo: subsurface-for-dirk Number of commits: 2102
...
```

### Running tests
```bash
pytest test_github_api.py -v
```

To run with coverage:
```bash
pip install pytest-cov
pytest test_github_api.py --cov=github_api -v
```

## Implementation Details
- Uses public GitHub REST API (no authentication required)
- Handles invalid users gracefully (returns empty list)
- Handles API errors and network exceptions safely
- Mocked API calls in tests (no real API calls during testing)
- Returns data as list of tuples: `[("repo_name", commit_count), ...]`
