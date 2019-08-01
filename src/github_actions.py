from github import Github

class GithubTools:
    """
    Tools for interacting with github
    """

    def __init__(self):
        """
        Initializes the github tools by authenticating user
        """
        with open("github_PAT.txt") as github_token_file:
            personal_access_token = github_token_file.read()
        self.g = Github(personal_access_token)

    
    def get_user_repos(self):
        """
        List of all the repositories for the user
        :return: list of repository names
        """
        self.repo_names = []
        for repo in self.g.get_user("Matt-Gleich").get_repos():
            self.repo_names.append(repo.name)

jgf = GithubTools()
print(jgf.get_user_repos())

