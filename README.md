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
+ Step 1
3.  Restricting SSH access for two of them, who should only log in locally.
+ Step 1

### TASK 2 - System Monitoring & Performance Analysis
The team has been receiving complaints about server slowness during peak hours. You suspect a process might be consuming too many resources. Your tasks are:

1.  To identify the top resource-consuming process and determine if it is necessary.
+ Step 1
2.  To check the disk usage to ensure logs are not consuming too much space.
+ Step 1
3.  Monitor real-time system logs to detect anomalies.
+ Step 1

### TASK 3 - Application Management
The development team has requested the installation of Nginx for a new microservice. They also need:

1.  The Nginx service to start automatically on boot
+ Step 1
2.  A check to ensure it is running properly after installation.
+ Step 1
3.  The ability to restart it if it crashes.
+ Step 1

### TASK 4 - Networking and Security
Security is a top priority at HypotheticalCorp.
Your tasks are to configure these security measures on your Linux server:

1.Blocking all incoming traffic except SSH and HTTP.
+ Step 1
2.Checking which ports are currently open on the system.
+ Step 1
3.Setting up an SSH key-based authentication to eliminate password logins.
+ Step 1


## Contributing

## License

## contact




