"""
import csv
# Function to add new rows
def add_row(file_name, data):
    with open(file_name, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

# Function that gets headers
def get_headers(file_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
    return headers

file_name = "C:\\Users\\User\\Downloads\\bamboohr-netsuite-export.csv.back (15).csv"

# Get the headers of the CSV file
headers = get_headers(file_name)

# Create data for new rows
names = ["Behnam", "Arash", "Fin"]
rows = []

# Add the names and add API Integration
for name in names:
    row_data = {header: "" for header in headers}
    row_data['displayName'] = name
    row_data['jobTitle'] = "Api integration" 
    rows.append(row_data)

# Add the hireDate values
rows.append({header: "" if header != "hireDate" else "00-00-0000" for header in headers})
rows.append({header: "" if header != "hireDate" else "14/2/2022" for header in headers})

# Append rows 
for row in rows:
    add_row(file_name, [row[header] for header in headers])

print("works")




"""
import csv
import sys
import datetime

file_location = r"C:\\Users\\User\\Downloads\\bamboohr-netsuite-export.csv.back (15).csv"

python2 = sys.version_info[0] == 2
#opens file 
def open_file(mode):
    if python2:
        return open(file_location, mode)
    else:
        return open(file_location, mode, newline='', encoding='utf-8')

filtered_rows = []
#reading file
with open_file('rb' if python2 else 'r') as file:
    reader = csv.DictReader(file)

    displayName = 'displayName'
    jobTitle = 'jobTitle'
    hireDate = 'hireDate'
    
    if python2:
        displayName = displayName.encode('utf-8')
        jobTitle = jobTitle.encode('utf-8')
        hireDate = hireDate.encode('utf-8')

    for row in reader:
        # Checks for names 
        if row[displayName] not in ["Behnam", "Arash", "Fin"]:
            # filters out rows
            if 'Api integration' not in row[jobTitle]:
                # Check for invalid start date
                if row[hireDate] != "00-00-0000":
                    # Updates date format to mm/dd/yy
                    try:
                        date_obj = datetime.datetime.strptime(row[hireDate], '%d-%m-%Y')
                        row[hireDate] = date_obj.strftime('%m/%d/%y')
                    except ValueError:
                        pass
                    filtered_rows.append(row)

fieldnames = ["employeeNumber", "status", "displayName", "firstName", "lastName", 
              "jobTitle", "workEmail", "division", "department", "location", "currency", 
              "subsidiary", "employmentHistoryStatus", "supervisorId", "customBusinessUnit",
              "hireDate", "lastChanged"]
#writes file
with open_file('wb' if python2 else 'w') as file:

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for row in filtered_rows:
        writer.writerow(row)
print("Successful")


