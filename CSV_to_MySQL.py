import pymysql
import csv

host = "localhost"
user = "root"
password = ""
db = "assessment"

database = pymysql.connect(host=host, user=user, passwd=password, db=db)
cursor = database.cursor()
csv_data = csv.reader(open("countries_visa_free_access.csv"))
header = next(csv_data)
print("File is being imported")
for row in csv_data:
    print(row)
    cursor.execute("INSERT INTO visafreeaccess (Country, Rank, VisaFreeAccess) VALUES (%s, %s, %s)",row)

database.commit()
cursor.close()
print("CSV File Loaded in Database Successfully")
