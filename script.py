import csv
import sys

file_location = r"C:\Users\User\Downloads\bamboohr-netsuite-export.csv.back (1).csv"
#initilizing python2 to a variable
python2 = sys.version_info[0] == 2
#opening file to read and write
def open_file(mode):
    if python2:
        return open(file_location, mode)
    else:
        return open(file_location, mode, newline='', encoding='utf-8') #python3 gives options for those last 2 arguments

filtered_rows = []
#reading file
with open_file('rb' if python2 else 'r') as file:
    reader = csv.DictReader(file)

    firstName = 'firstName'
    if python2:
        firstName = firstName.encode('utf-8') #unnecessary?
#appending all the rows without the specified values into file
    for row in reader:
        if row[firstName] not in ["Behnam", "Arash"]:
            filtered_rows.append(row)

fieldnames = ["employeeNumber", "status", "displayName", "firstName", "lastName", 
              "jobTitle", "workEmail", "division", "department", "location", "currency", 
              "subsidiary", "employmentHistoryStatus", "supervisorId", "customBusinessUnit",
              "hireDate", "lastChanged"]
#writing file
with open_file('wb' if python2 else 'w') as file:

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for row in filtered_rows:
        writer.writerow(row)
