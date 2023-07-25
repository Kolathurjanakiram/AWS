import boto3
import subprocess
import os

# Replace these variables with your AWS region and CodeCommit repository name
AWS_REGION = 'us-east-1'
REPO_NAME = 'your-codecommit-repo-name'

def create_codecommit_repo():
    client = boto3.client('codecommit', region_name=AWS_REGION)

    try:
        # Create the CodeCommit repository
        response = client.create_repository(repositoryName=REPO_NAME)

        print(f"Repository '{REPO_NAME}' created successfully.")

        # Clone the local Git project
        git_clone_cmd = f"git clone https://github.com/your-github-username/your-github-repo.git"
        subprocess.run(git_clone_cmd, shell=True)

        # Change directory to the local Git project
        os.chdir(os.path.join(os.getcwd(), 'your-github-repo'))

        # Add the CodeCommit repository as a remote
        add_remote_cmd = f"git remote add codecommit https://git-codecommit.{AWS_REGION}.amazonaws.com/v1/repos/{REPO_NAME}"
        subprocess.run(add_remote_cmd, shell=True)

        # Push the local Git project to CodeCommit
        push_cmd = "git push codecommit master"
        subprocess.run(push_cmd, shell=True)

        print("Code pushed to CodeCommit successfully.")

    except client.exceptions.RepositoryNameExistsException:
        print(f"Repository '{REPO_NAME}' already exists.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    create_codecommit_repo()
