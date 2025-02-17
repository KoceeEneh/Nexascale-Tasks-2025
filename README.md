# NEXASCALE-ASSIGNMENT-LINUX


## Linux Administrator at HypotheticalCorp
This is a growing tech company that provides cloud-based services to clients. responsibilitoes includes
- User access
- ensuring sustem security
- Monitoring system performance
- Handling application deplyments
  

this project, records detailed step to step approach on how i was able to carry out my tasks as a linux adminstrator.


## Requirments
- linux OS


## Challanges


### TASK 1 - User and Role managements 
The company recently hired five new developers who need access to the development server. Your task is to:

1.  Creating user accounts for them and add them to the developers group
   
+ Step 1 - added five users

```bash

sudo adduser user_name
```

output

<img width="584" alt="Screenshot 2025-02-16 at 20 48 00" src="https://github.com/user-attachments/assets/f730553a-dd9c-43ab-8611-65f446c10d4f" />


<img width="579" alt="Screenshot 2025-02-16 at 20 48 23" src="https://github.com/user-attachments/assets/7d48c6c0-91ea-439b-973d-d03f7c950672" />


<img width="614" alt="Screenshot 2025-02-16 at 20 48 43" src="https://github.com/user-attachments/assets/fbadd58e-212d-4067-8365-45b16c2a9a94" />


<img width="618" alt="Screenshot 2025-02-16 at 20 49 09" src="https://github.com/user-attachments/assets/d15703b2-bd51-4851-9e60-dbf97e17acfe" />


<img width="628" alt="Screenshot 2025-02-16 at 20 49 35" src="https://github.com/user-attachments/assets/6c71aa66-1cfd-49bc-b7aa-09fe6a8fd49e" />

+ Step 2 - adding them to a group

first create a group

```bash
sudo addgroup group_name
```

output

<img width="621" alt="Screenshot 2025-02-16 at 23 39 18" src="https://github.com/user-attachments/assets/232cdeef-d925-4ac8-8ca2-f21db68f7b84" />

after creating the group,you add them to it.

```bash
sudo usermod -aG group_name user_name
```

output

<img width="622" alt="Screenshot 2025-02-16 at 23 39 32" src="https://github.com/user-attachments/assets/d18dd340-d44c-4cb5-b6ad-e9b5cdfaee68" />

lastly,verify that they are already in the group

```bash
groups user_name
```

output

<img width="620" alt="Screenshot 2025-02-16 at 23 40 13" src="https://github.com/user-attachments/assets/f14e2553-bbdb-4cc8-8443-d38a076ca7d0" />

2.  Ensureing they have read and execute permission for _/var/www/project_ but cannot modify files

+ Step 1 - change the ownership of the directory so that i would belong to the group.

```bash
sudo chown :group_name folder_path
```

output
<img width="597" alt="Screenshot 2025-02-17 at 00 51 14" src="https://github.com/user-attachments/assets/ac457407-9a00-41b8-bfc6-382c39be895e" />

+ Step 2 - Then set the 'read' and 'execute' permission to the group

```bash
sudo chmod 750 folder_path
```

output

<img width="601" alt="Screenshot 2025-02-17 at 00 51 46" src="https://github.com/user-attachments/assets/56dc2120-3de6-4d73-b4f7-130be0a202a3" />

to verify if it works enterr this command

```bash
sudo ls -ld
```

output
<img width="591" alt="Screenshot 2025-02-17 at 00 52 14" src="https://github.com/user-attachments/assets/555adf71-b82d-4679-a2d1-e1b346be53b8" />

this lists the permissions assigned to owner.

drwxr-x--- : owner has full permission, group has 'read' and 'execute' perission.

3.  Restricting SSH access for two of them, who should only log in locally.
   
+ Step 1 - edit the ssh config file
  
```bash
sudo nano /etc/ssh/sshd_config
```

output

<img width="618" alt="Screenshot 2025-02-17 at 01 16 12" src="https://github.com/user-attachments/assets/d5865fb5-7a44-4bf5-a1df-d38e834da85d" />

+ Step 2 - add the following to the configuration file
  
```bash
Deny user_name1 user_name2
```

output

<img width="599" alt="Screenshot 2025-02-17 at 01 16 58" src="https://github.com/user-attachments/assets/1f907335-46ac-493d-adad-2363faf8b3db" />

+ Step 3 - restart ssh to save the changes and apply them.
  
```bash
sudo systemctl restart ssh
```

output

<img width="597" alt="Screenshot 2025-02-17 at 01 17 22" src="https://github.com/user-attachments/assets/eacb54ed-f6ff-40b8-84f7-433a440687f1" />


### TASK 2 - System Monitoring & Performance Analysis
The team has been receiving complaints about server slowness during peak hours. You suspect a process might be consuming too many resources. Your tasks are:

1.  To identify the top resource-consuming process and determine if it is necessary.
   
+ Step 1 - to check for resource-consuming process we use the Top comd

```bash
top
htop #use if installed, has a more freindly user-interface
```

+Step 2 - determine if its necessary by running there commands

```bash
ps -p <PID> -o comm,args
```


2.  To check the disk usage to ensure logs are not consuming too much space.
   
+ Step 1 - to check the disk usage run

```bash
df -h #-h to read in a human understandable format
```

output

<img width="1090" alt="Screenshot 2025-02-17 at 01 58 52" src="https://github.com/user-attachments/assets/9af35015-4453-457f-b852-860b7684565f" />

+ Step 2 - checking the size in system log

```bash
du -sh /var/log  #system log is stored in /var/log
```

output

<img width="598" alt="Screenshot 2025-02-17 at 01 59 24" src="https://github.com/user-attachments/assets/bfd969e0-ce02-4d6d-bfb8-e8d20bc27a91" />

this shows the total space used by the log


3.  Monitor real-time system logs to detect anomalies.

+ Step 1 - Using journalctl to monitor system logs in real time

```bash
sudo journalctl -f
```

output

<img width="618" alt="Screenshot 2025-02-17 at 02 05 59" src="https://github.com/user-attachments/assets/b34088fb-3297-49cc-830e-5e300e776f17" />

+ Step 2 - also checking for failed SSH login attempt

```bash
sudo journalctl -u ssh -f
```
looking for multiple login attempt might indicate a brute force attack

output

<img width="613" alt="Screenshot 2025-02-17 at 02 09 54" src="https://github.com/user-attachments/assets/4f01c51c-3116-4059-8ba1-706bc4f393f8" />

+ Step 3 - Useing top or htop to detect CPU-heavy anomalies
  
```bash
top
htop
```

Looks for unexpected high CPU or memory usage.

+ Step 4 - Checking for unusual network connections
  
```bash
sudo netstat -tulnp
sudo lsof -i  #looks for unkown program listening on port
```

for unusual network connection

<img width="620" alt="Screenshot 2025-02-17 at 02 17 36" src="https://github.com/user-attachments/assets/8dd4ef2d-0ff5-4ecd-b3c7-14cefb5817b7" />

for unknown program listening on port

<img width="620" alt="Screenshot 2025-02-17 at 02 19 04" src="https://github.com/user-attachments/assets/46b51c11-ec3a-465e-8e0a-3f52adc7b099" />


### TASK 3 - Application Management
The development team has requested the installation of Nginx for a new microservice. They also need:

1.  The Nginx service to start automatically on boot
   
+ Step 1 - installing Nginx
  
```bash
sudo apt update && sudo apt install nginx -y
```

output

<img width="621" alt="Screenshot 2025-02-17 at 13 36 50" src="https://github.com/user-attachments/assets/76453a1e-0ee2-4d3e-a3b8-87bdb3be4cac" />

+ Step 2 - start and enable Nginx
  
```bash
sudo systemctl enable nginx
```

output

<img width="624" alt="Screenshot 2025-02-17 at 13 45 45" src="https://github.com/user-attachments/assets/e37e3f9f-1002-4691-8ee5-de1a0e0d61b6" />


2.  A check to ensure it is running properly after installation.

 checking if the service is running
 
```bash
sudo systemctl status nginx
```

output

<img width="624" alt="Screenshot 2025-02-17 at 13 37 28" src="https://github.com/user-attachments/assets/aaac53a9-c599-480d-ba40-0581632ed5f4" />


3.  The ability to restart it if it crashes.
   
Systemd manages services in Kali Linux.i will be configuring it to automtically restart Nginx.

+ Step 1 - creating and editing the systemd overide file
  
```bash
sudo mkdir -p /etc/systemd/system/nginx.service.d
sudo nano /etc/systemd/system/nginx.service.d/restart.conf
```

add these lines

```bash
[Service]
Restart=always
RestartSec=5s
```

- Restart=always → Ensures Nginx restarts after a failure.
- RestartSec=5s → Waits 5 seconds before restarting.

output

<img width="601" alt="Screenshot 2025-02-17 at 14 08 57" src="https://github.com/user-attachments/assets/d43fb8be-6dfc-47cb-94c0-232decb91980" />

+ Step 2 - reload and restart nginx

```bash
sudo systemctl daemon-reload
sudo systemctl restart nginx
```


### TASK 4 - Networking and Security

Security is a top priority at HypotheticalCorp.
Your tasks are to configure these security measures on your Linux server:

1.Blocking all incoming traffic except SSH and HTTP.

+ Step 1 - install ufw (unconplicated firewall) if not installed
  
```bash
sudo apt update && sudo apt install ufw -y
```

+ Step 2 - set default rules

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

output

<img width="626" alt="Screenshot 2025-02-17 at 17 54 57" src="https://github.com/user-attachments/assets/e8923e01-ec4e-41b4-bf7c-0f5a33797df4" />

+ Step 3 - allow only SSH and HTTP

```bash
sudo ufw allow 22
sudo ufw allow 80
```

+ Step 4 - enable ufw
  
```bash
sudo ufw enable
 ```

+ Step 5 - check the status to ensure its working

 ```bash
sudo ufw status
```


2.Checking which ports are currently open on the system.

there are so many methods we can use to check for open ports. but i will be using two.

+ method 1 - using netstat
  
```bash
sudo netstat -tulnp
```
if you dont have netstat installed try installing it first: __sudo apt install net-tools -y_

output

<img width="623" alt="Screenshot 2025-02-17 at 17 52 28" src="https://github.com/user-attachments/assets/8365c6db-2e16-4669-99d1-f39f6ee353f1" />

+ method 2 - using ss
```bash
sudo ss -tulnp
```

 output

 <img width="626" alt="Screenshot 2025-02-17 at 17 52 56" src="https://github.com/user-attachments/assets/15a056ca-06c1-490a-9038-f783c4b265eb" />

3.Setting up an SSH key-based authentication to eliminate password logins.

+ Step 1 - Generate SSH Key Pair (On Your Local Machine)

```bash
ssh-keygen -t rsa -b 4096
```

+ Step 2 -  Copy the Public Key to the Server

Use ssh-copy-id to copy the key to your Kali Linux server:

```bash
ssh-copy-id user@your_server_ip
```

enter your ssh password if prompted

+ Step 3 -  Test SSH Key Login

try logging in to the server without a password:

```bash
ssh user@your_server_ip
```

If the key is set up correctly, you should get access without a password.

+ Step 4 - Disable Password Logins

To completely disable password-based logins, edit the SSH configuration:

```bash
sudo nano /etc/ssh/sshd_config
```

Find and modify these lines:
```bash
PasswordAuthentication no
PubkeyAuthentication yes
```

+ Step 5 - Restart SSH Service

```bash
sudo systemctl restart ssh
```


## Contributing

drop your thoughts on simpler and faster methods that has worked for you


## License


## contact

**x** - https://x.com/ko_ceeherself




