import csv
from operator import itemgetter
fields = ['EMPID','Name','DOB','Department','Designation','Experience',  'No of leaves','Salary']
rows = [['1',   'Mounika',  '02-05-2001',   'E-104',    'HR',       '1',    '20',   '30000'],
        ['2',   'Vishal',   '11-06-1984',  'E-105',    'Admin',    '5',    '15',   '25000']]
choice=int(input('Enter Your choice : '))
if choice==1:
    filename = "Employees.csv"
    with open(filename, 'w') as csvfile:
        try:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
            print('Inserted into the CSV file')
        except Exception as e:
            print(e)
elif choice==2:
    with open("Employees.csv", mode='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)
elif choice==3:
    with open("Employees.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        # csv_reader = csv.reader(csv_file)
        for lines in csv_reader:
            if(int(lines['No of leaves'])>int(2)):
                print(lines)
elif choice==4:
    with open("Employees.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for lines in csv_reader:
            if(int(lines['Experience'])>int(10)):
                print(lines)
elif choice==5:
    with open("Employees.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for lines in csv_reader:
            print(lines["Name"])
            print(lines["EMPID"])
else:
    exit()