import requests
from bs4 import BeautifulSoup
from tabulate import tabulate



def grades():
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
                                if dataStage[0] == limitSY:
                                        data.append(dataStage)
                        except IndexError:
                                pass
                elif limitSY == '':
                        data.append(dataStage) 
                dataStage = []
        
        print (tabulate(data, headers=["SY", "Sem", "Subject", "Desc", "Units", "Midterms", "Finals"]))


def textscrapper():
        global username, password, limitSY, userInput
        with open('userinfo.txt', "r+") as text:
                textContent = text.read()
                if len(textContent) == 0:
                        print("userinfo.txt not found or is empty\n")
                        setup()
                else:
                        print("userinfo.txt found. Attempting to get grades.\n")
                        data = textContent.split('\n')
                        try:
                                username = data[0]
                                password = data[1]
                                limitSY = data[2]
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
        textscrapper()

print("Silliman Grades")
while True:
        try:  # Doing this apparently forces python to create a "userinfo.txt" file
                textscrapper()
        except:
                pass
        
        try:
                grades()
                break
        except:
                print("==ERROR==")
                print("Errors occured most likely due to a setup error")
                open('userinfo.txt', 'w').close()
                print("Erasing content of userinfo.txt\n")
