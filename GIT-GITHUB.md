# Nexascale Task  on GIT/GITHUB

# Overview

This assignment focuses on Git and GitHub basics, including version control, collaboration, and conflict resolution. 

# Features
- version control and branching
- Team collabration
- resolving merge conflict
- working with a remote repository

# Installation


# - version control and branching

1. create a git repository on github ( i created a repo called **nexascale_devsecops** )

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



# - working with a remote repository

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









