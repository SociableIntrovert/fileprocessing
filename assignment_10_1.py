import os
import csv
import traceback
from prettytable import PrettyTable

name = input("Enter your name: ")
address = input("Enter your address: ")
phone = input("Enter your phone number: ")
table = PrettyTable()

validDir = False
while not validDir:
    targetDir = input("Enter the directory to save to: ")
    if os.path.isdir(targetDir):
        file = os.path.join(targetDir, "contact.csv")
        try:
            with open(file, mode='w', newline='') as csvfile:
                fileWriter = csv.writer(csvfile, delimiter=',', quotechar='"')
                fileWriter.writerow(['Name', 'Address', 'Phone'])
                fileWriter.writerow([name, address, phone])
                csvfile.close()

            with open(file) as csvfile:
                fileReader = csv.reader(csvfile, delimiter=',')
                lineNo = 0
                for row in fileReader:
                    if lineNo == 0:
                        table.field_names = [row[0], row[1], row[2]]
                        lineNo += 1
                    else:
                        table.add_row([row[0], row[1], row[2]])
                csvfile.close()

            print(table)
        except:
            traceback.print_exc()
        validDir = True
    else:
        print("Path is bad. Try again.")

