# Clean_Desktop



# Python Script for Organizing Files on Your Desktop

This Python script helps you declutter your desktop by creating three folders: "Images," "Documents," and "Videos." It then intelligently moves files with corresponding extensions into these folders. To avoid any potential file name conflicts, the script adds the current date to the beginning of each file name.

## Usage

1. Download the `organize_desktop.py` script to your preferred directory.

2. Open your terminal and navigate to the directory where the script is located.

3. Run the script using the following command:

   ```bash
   python3 organize_desktop.py
   ```

Your desktop files will now be organized into the appropriate folders, and the script will prevent any file name clashes.

## Automation (Linux Example)

To make this process automatic, you can schedule the script to run daily using tools like `cron` on Linux. Here's how:

1. Open your terminal and type `crontab -e` to edit your user's crontab.

2. Add the following line to schedule the script to run every day at 8 AM:

   ```bash
   0 8 * * * /usr/bin/python3 /path/to/your/organize_desktop.py
   ```

   The five asterisks represent the minute, hour, day of the month, month, and day of the week.

3. Save and exit the crontab file.

By following these steps, the script will automatically organize your desktop files at your specified time every day.

## Contribution

Feel free to contribute by opening issues or submitting pull requests. Your contributions can help improve the script and make it even more efficient!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


Remember to replace 
```bash
 /path/to/your/organize_desktop.py
```
with the actual path to your script. This markdown content can be directly copied and pasted into your GitHub README.md file to provide a clear guide for users interested in using and automating the script.
