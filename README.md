# Clean_Desktop
Python script that organizes files on your desktop. 

This script creates folders with names "Images", "Documents", and "Videos" on your desktop, and moves files with the corresponding extensions into those folders. The script also adds today's date to the beginning of each file name, to prevent overwriting of files with the same name.

To automate the script to run every day, you can use a task scheduler such as cron on Linux or Task Scheduler on Windows. Here is an example of how to schedule the script to run every day at 8am on Linux:

1. Open the terminal and enter crontab -e to edit your user's crontab file.
2. Add the following line to the bottom of the file: 0 8 * * * /usr/bin/python3 /path/to/your/script.py
3. Save and exit the crontab file.

This will schedule the script to run at 8am every day. You can modify the timing by changing the first two numbers (in the example, "0" and "8") to represent the minute and hour that you want the script to run
