import subprocess
import time
import os

# Define backup parameters
user = "root"
password = "your_password"
database = "your_database_name"
backup_dir = "backups"

# Ensure backup directory exists
os.makedirs(backup_dir, exist_ok=True)

# Create a unique filename with timestamp
timestamp = time.strftime("%Y%m%d-%H%M%S")
filename = f"{database}_backup_{timestamp}.sql"
filepath = os.path.join(backup_dir, filename)

# Run the backup using mysqldump
try:
    result = subprocess.run(
        ["mysqldump", "-u", user, f"-p{password}", database],
        stdout=open(filepath, "w"),
        stderr=subprocess.PIPE
    )
    if result.returncode == 0:
        print(f"Backup successful: {filepath}")
    else:
        print(f"Backup failed. Error: {result.stderr.decode()}")
except Exception as e:
    print(f"An exception occurred: {e}")
