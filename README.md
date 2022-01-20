# Silliman-Grades-Web_Scraper

A lighter and faster alternative to loading one's Silliman grades. Helpful for when your teachers haven't submitted your grades yet and you want to check it frequently.

---
Attempts to get your grades from https://my.su.edu.ph/mysilliman/

This is done by:
1. Sending your login requests to the website.
2. Receive the html of what would be shown in https://my.su.edu.ph/mysilliman/student/grades.php.
3. Locates the table that contains your grades.
4. Filters out html tags and prints either: a) everything or b) limits to the school year specified in the setup process.

---
Things that might be installed other than python.
```
pip install beautifulsoup4
pip install tabulate
pip install requests
```

---
## ⚠️ Some concerns
- This program stores your password locally, but in plain text. Not recommended for shared computers.
  - (Clarification) This is not to be confused with the requests sent to mysilliman. That seemed to be fine.
    - see for more info:https://www.geeksforgeeks.org/ssl-certificate-verification-python-requests/
