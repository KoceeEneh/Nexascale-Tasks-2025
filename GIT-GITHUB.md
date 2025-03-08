# Nexascale Task  on GIT/GITHUB

# Overview

This assignment focuses on Git and GitHub basics, including version control, collaboration, and conflict resolution. 

# Features
- version control and branching
- Team collabration
- resolving merge conflict
- working with a remote repository

# Installation
---   

# **TASK 1 - version control and branching**

1. create a git repository on github ( i created a repo called `nexascale_devsecops` )

<img width="1437" alt="Screenshot 2025-03-08 at 16 30 58" src="https://github.com/user-attachments/assets/ea80732d-c533-4744-ba2b-81279396d4fc" />

2. Clone the repository locally ( replace with the repo you created )

``` bash
   git clone https://github.com/KoceeEneh/nexascale_decsecops.git
```
   
3. Create a new branch called `feature-update`

```bash
git branch feature-update
```

 4. Add a new file named README.md and write a short introduction

``` bash
nano README.md
```
*CTRL+X - Y - ENTER**

5. Commit the changes and push the `feature-update` branch to the remote repository.

```bash
git add .
git commit -m " added readme.md "
git push origin feature-update
```

6. Open a pull request (PR) to merge feature-update into main

   - open pull request
  
<img width="1024" alt="Screenshot 2025-03-08 at 16 46 17" src="https://github.com/user-attachments/assets/d19f9956-b5c0-4ef7-a5b3-be5ec8cb6391" />

   - merged pull request

<img width="1015" alt="Screenshot 2025-03-08 at 16 46 41" src="https://github.com/user-attachments/assets/a1c03afb-0444-451d-8ee1-36f3e34c1f4f" />

---

# **TASK 2 - Team collabration**

1. for this task i collaborated with @cliuzy
2. created a repository and added me as a collaborator
   
4. The collaborator should clone the repo, create a new branch `update-styles`, and modify index.html by adding a <style> section.

```bash
git clone https://github.com/cliuzy/Team-collaboration.git
git branch update-styles
nano index.html
```

   - modifying the index.html file
     
```bash 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Webpage</title>

        <link rel="stylesheet" href='style.css">
</head>
<body>
    <h1>Welcome to Nexascale Git task</h1>
    <p>This is a simple HTML page.</p>
</body>
</html>
```

   - commit and push changes

```bash
git commit -m "created style section"
git push origin updates-styles
```

   - open pull request

<img width="1020" alt="Screenshot 2025-03-08 at 17 19 45" src="https://github.com/user-attachments/assets/3cbb2b5b-4ba6-4c38-bf23-361b76495ef6" />

5. The repository owner should review, approve, and merge the PR.
   
   - the owner reviewed and merged the PR

6. Both students should pull the latest changes to their local machines
   - pulled changes to repo

```bash
git pull origin update-styles
```
---
 
# **TASK 3 - resolving merge conflict**

1. Each student should create a repository and clone it ( for this assignment i created `Merge-conflict-Task3` )

```bash
git clone https://github.com/KoceeEneh/Merge-Conflict-Task3.git
```

2. Create a new branch `edit-text` and modify an existing file (or create one)

```bash
git branch edit-text
nano index.html
```

   - `edit-text` index.html

<img width="1154" alt="Screenshot 2025-03-08 at 17 47 09" src="https://github.com/user-attachments/assets/38a97774-90ba-4f0a-9e3a-f517aa1fe06e" />

3.Switch back to main and modify the same file in a different way.

   - `main` index.html

<img width="1178" alt="Screenshot 2025-03-08 at 17 50 21" src="https://github.com/user-attachments/assets/5545d7bc-222f-4a88-afca-2dac50dbb60d" />

4. Merge edit-text into main to intentionally create a merge conflict

<img width="1017" alt="Screenshot 2025-03-08 at 17 54 43" src="https://github.com/user-attachments/assets/4be11c04-59cf-48b0-bda7-5889878f6584" />

5. Resolve the conflict, commit the changes, and push the final version

   - Resolved conflict
<img width="1440" alt="Screenshot 2025-03-08 at 17 58 17" src="https://github.com/user-attachments/assets/625bb730-4c49-44d7-a184-ebd4a4313a4b" />

   - Merged changes

<img width="1020" alt="Screenshot 2025-03-08 at 18 01 23" src="https://github.com/user-attachments/assets/c6298522-90f5-4ec7-bc46-b8c5e6ba48b9" />

---

#  **TASK 4 - working with a remote repository**

1. go to the repository you are working with (for this assignment, i used https://github.com/NexaScaleHQ/cloud-titans-project-1)
2. Click the "Fork" button at the top right.
3. Choose your GitHub account to fork the repository.
4. Clone your forked repository locally
   

``` bash


git clone https://github.com/NexaScaleHQ/cloud-titans-project-1.git


```


5. Create a new branch (for this assignment i used `documentation-update` )
   

``` bash


git branch documentaton-update


```


6. Make meaningful changes to the documentation files (for this assignment i created a file called TASK4.md)
   

<img width="1440" alt="Screenshot 2025-03-08 at 00 19 12" src="https://github.com/user-attachments/assets/f7f915f8-d893-4e1a-b946-0af95146bd2a" />


7. Commit the changes with appropriate commit messages.
   

``` bash


git commit -m "commit message"


```


8. Push the branch to your fork


``` bash


git push origin documentation-updatd


```


9. Create a pull request to the original repository (do this on your github interface if you are not familiar with github cli) <br/>
    

 <img width="1025" alt="Screenshot 2025-03-08 at 00 25 35" src="https://github.com/user-attachments/assets/a91695f9-a995-4af7-b185-ff451880d242" />
 
--- 

# Resources

- TASK 1 - https://github.com/KoceeEneh/nexascale_decsecops
- TASK 2 - https://github.com/cliuzy/Team-collaboration
- TASK 3 - https://github.com/KoceeEneh/Merge-Conflict-Task3
- TASK 4 - https://github.com/KoceeEneh/cloud-titans-project-1








