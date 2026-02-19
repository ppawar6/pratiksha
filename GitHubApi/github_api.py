import requests


def get_repo_info(user_id):
    """
    Retrieve repository information and commit counts for a GitHub user.
    
    Args:
        user_id: GitHub username
        
    Returns:
        List of tuples: [("repo_name", commit_count), ...]
        Empty list if user not found or API error occurs
    """
    repos_url = f"https://api.github.com/users/{user_id}/repos"
    
    try:
        repos_response = requests.get(repos_url)
        
        if repos_response.status_code == 404:
            return []
        
        if repos_response.status_code != 200:
            return []
        
        repos = repos_response.json()
        
        if not isinstance(repos, list):
            return []
        
        result = []
        
        for repo in repos:
            repo_name = repo.get("name")
            commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
            
            try:
                commits_response = requests.get(commits_url)
                
                if commits_response.status_code == 200:
                    commits = commits_response.json()
                    commit_count = len(commits) if isinstance(commits, list) else 0
                else:
                    commit_count = 0
                
                result.append((repo_name, commit_count))
            except requests.RequestException:
                result.append((repo_name, 0))
        
        return result
    
    except requests.RequestException:
        return []


if __name__ == "__main__":
    user_input = input("Enter GitHub user ID: ")
    repos_info = get_repo_info(user_input)
    
    if repos_info:
        for repo_name, commit_count in repos_info:
            print(f"Repo: {repo_name} Number of commits: {commit_count}")
    else:
        print("No repositories found or user not found.")
