import os


# function that counts "error" in a log file
def count_errors(log_file):

    if not os.path.exists(log_file):
        print("Error: File not found.")
        return

    with open(log_file, "r") as file:
        logs = file.readlines()

    error_count = sum(1 for line in logs if "ERROR" in line)

    print(f"Found {error_count} error logs in {log_file}")


# function to filter logs by severity level
def filter_logs(log_file, level="ERROR"):
    if not os.path.exists(log_file):
        print("Error: File not found.")
        return

    with open(log_file, "r") as file:
        logs = [line.strip for line in file if level.upper() in line.upper()]

    print(f"\n logs with '{level}' : ")
    if logs:
        for log in logs:
            print(log)
        print(f"\nFound {len(logs)} occurrences of '{level}' in logs.")
    else:
        print(f"No logs with '{level}' found.")


# create a log file
log_file = "demo.log"
if not os.path.exists(log_file):
    with open(log_file, "w") as file:
        file.write("INFO: Application started\n")
        file.write("ERROR: Something went wrong\n")
        file.write("INFO: Application stopped\n")
        file.write("ERROR: Another error occurred\n")
        file.write("DEBUG: Debugging information\n")
        file.write("ERROR: Yet another error\n")

# function calls
filter_logs(log_file, "ERROR")
filter_logs(log_file, "INFO")
filter_logs(log_file, "ERROR")
count_errors(log_file)
