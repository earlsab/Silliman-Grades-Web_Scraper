import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def grades():
        global data
        payload = {
                'username': username,
                'password': password
                }

        URL = "https://my.su.edu.ph/mysilliman/login.php"
        page = requests.get(URL)

        with requests.Session() as s:
                p = s.post('https://my.su.edu.ph/mysilliman/login.php', data=payload)
                r = s.get('https://my.su.edu.ph/mysilliman/student/grades.php')


        soup = BeautifulSoup(r.content,'html.parser')
        table = soup.find('table', class_="table")

        data = []
        dataStage = []

        tr = table.find_all("tr")
        for td in tr:
                row = td.find_all("td")
                for x in row:  # Prints out Individual Data
                        dataStage.append(x.get_text())

                if limitSY != '':
                        try:
                                if dataStage[0] == limitSY and (dataStage[1] == limitSem1 or dataStage[1] == limitSem2):  #TODO Allow for more options in "limitSY"
                                        data.append(dataStage)
                        except IndexError:
                                pass
                elif limitSY == '':
                        data.append(dataStage) 
                dataStage = []
        
        print(tabulate(data, headers=["SY", "Sem", "Subject", "Desc", "Units", "Midterms", "Finals"]))

def textscrapper():
        global username, password, limitSY, userInput, limitSem1, limitSem2 
        with open('userinfo.txt', "r+") as text:
                textContent = text.read()
                if len(textContent) == 0:
                        print("userinfo.txt not found or is empty\n")
                        setup()
                else:
                        print("userinfo.txt found. Attempting to get grades.\n")
                        userData = textContent.split('\n')
                        try:
                                username = userData[0]
                                password = userData[1]
                                limitSY = userData[2]
                        except:
                                print("userinfo.txt in wrong format")
                        try:
                                if userData[3] == "1st Sem":  # I acknowledge how lame this is written
                                        limitSem1 = "1st Sem"
                                        limitSem2 = "1st Sem"
                                elif userData[3] == "2nd Sem":
                                        limitSem1 = "2nd Sem"
                                        limitSem2 = "2nd Sem"
                                elif userData[3] == "Both":
                                        limitSem1 = "1st Sem"
                                        limitSem2 = "2nd Sem"
                        except:
                                print("userinfo.txt in wrong format")

def setup():
        print("==SETUP==")
        print("Any errors can be corrected by editing the \"userinfo.txt\" file.")
        with open('userinfo.txt', "w") as text:
                text.write(input("Silliman ID: "))
                text.write("\n")
                text.write(input("Password: "))
                text.write("\n")
                text.write(input("Limit to SY: "))
                text.write("\n")
                text.write(input("Limit Sem to (1st Sem/2nd Sem/Both): "))
        textscrapper()

def calculateQpa():
        qualityPoint = []
        units = []
        incompleteMatchedUnits = []
        completeGrades = False

        for index1 in data:
                try:
                        units.append(float(index1[4])) 
                        qualityPoint.append(float(index1[4]) * float(index1[6]))
                        incompleteMatchedUnits.append(float(index1[4]))  # Should only run if the code above works well. 
                except:
                        pass

        if len(units) == len(qualityPoint):
                cqpa = sum(qualityPoint) / sum(units)
                completeGrades = True
        else:
                cqpa = sum(qualityPoint) / sum(incompleteMatchedUnits)
                print("\n== ERROR ==")
                print("Found only grades for", len(qualityPoint), "subject(s)")
                print("Lacking grades for", (len(units) - len(qualityPoint)), "subject(s)")

        print("\nTotal Units: ", sum(units))
        print("Total Quality Points (Unit * Grade): ", sum(qualityPoint))
        
        print("\nCQPA = Total Quality Point / Number of Units")
        if completeGrades:
                print("Calculated CQPA:", cqpa)
        elif not completeGrades:
                print("Supposed CQPA Ouput (INCOMPLETE GRADES):", cqpa)

def showConfig():
        print(username)
        print(limitSY)
        print(limitSem1, "to", limitSem2, "\n")


print("Silliman Grades Python Script")
print('NOTE: This program does not contain a selectable menu of some kind, but rather is controlled through the "userinfo.txt" file.\n')
print('Check "README.md" for more info')

try:  # Doing this apparently forces python to create a "userinfo.txt" file
        textscrapper()
except:
        pass
try:
        print("showing config for:")
        showConfig()
        grades()
except:
        print("== ERROR ==")
        print("Errors occured most likely due to a setup error")
        open('userinfo.txt', 'w').close()
        print("Erasing content of userinfo.txt\n")

try:
        calculateQpa()
except:
        print("\n == ERROR ==")
        print("Failed to calculate QPA") 