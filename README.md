# Silliman-Grades-Web_Scraper

A lighter and faster alternative to loading one's Silliman grades. Helpful for those sem-ender grade anxiety.

## Installation
- Download the Project Files
- Have Python Installed
- Install Modules with `pip install -r requirements.txt`
- Run `python3 grades.py` inside the folder

*(Needs a tutorial but I got lazy)*

---
## A suggestion for macOS Monterey users
- After the initial setup, a shortcut could be made to automate the process. This shortcut for example is accessible for me in the menu bar. See image attached.
- Shortcuts could also be configured to run other shortcuts. Thus when properly configured, allows for the script to run every hour, and notifies you only for when there's an update to your grades.
![image](https://user-images.githubusercontent.com/62688314/150344161-46816971-d2fc-4d24-b74f-d908bc338495.png)

---
# Explainations
Attempts to get your grades from https://my.su.edu.ph/mysilliman/ displays it and calculates for your CQPA/QPA.

This is done by:
1. Sending your login requests to the website.
2. Receive the html of what would be shown in https://my.su.edu.ph/mysilliman/student/grades.php.
3. Locates the table that contains your grades.
4. Filters out html tags and prints either: a) everything or b) limits to the school year/semester specified in the setup process.
5. Calculates CQPA/QPA based on the data gathered

## userinfo.txt format

To avoid having to type the same information after every launch, the program starts with a one-time setup process that then stores that information in a file named "userinfo.txt" (saved in the folder where the python file is located). Every launch after that setup, the program reads that text file instead. 

In the event of an error, the program will attempt to fix itself by deleting the contents of the userinfo.txt and go through the setup process again.

Below this text contains the format in which the program reads from (minus the python comments "#"). Any slight changes in the order or spelling might cause an error so please be cautious.
```
21-0-00000  # SU-ID
p@ssw0rd  # SU Password
2021-2022  # (1) Limit results to a specific school year
1st Sem  # (2) Limit results to a specific semester
```

### Sidenotes
- (1) S.Y. limits only work when inputed that exact format, no extra spaces or characters
- (2) Sem limits work on the following 3 options: (1) "1st Sem", (2) "2nd Sem", (3) "Both" 

---
## ⚠️ Some concerns
- This program stores your password locally, but in plain text. Not recommended for shared computers.
  - (Clarification) This is not to be confused with the requests sent to mysilliman. That seemed to be fine.
    - see for more info:https://www.geeksforgeeks.org/ssl-certificate-verification-python-requests/
