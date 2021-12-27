def donar(name,age,contact_number,bloodgroup,address):
	import mysql.connector
	mydb=mysql.connector.connect(host="localhost",user="root",passwd="chiranthen54321",database="bloodbank")
	cursor=mydb.cursor()
	cursor.execute("INSERT INTO donar(name,age,contact_number,bloodgroup,address) VALUES(%s,%s,%s,%s,%s)",(name,age,contact_number,bloodgroup,address))
	mydb.commit()
	print(" Donar Records Added Successfully")


def request_blood(name,age,hospital_name,contact_number,bloodgroup,address):
	import mysql.connector
	mydb=mysql.connector.connect(host="localhost",user="root",passwd="chiranthen54321",database="bloodbank")
	cursor=mydb.cursor()
	cursor.execute("INSERT INTO patient(name,age,hospital_name,contact_number,blood_group,address) VALUES(%s,%s,%s,%s,%s,%s)",(name,age,hospital_name,contact_number,bloodgroup,address))
	mydb.commit()
	print(" Patient Records Added Successfully")

def donar_info():
	import mysql.connector
	mydb=mysql.connector.connect(host="localhost",passwd="chiranthen54321",username="root",database="bloodbank")
	cursor=mydb.cursor()
	cursor.execute("SELECT * from donar")
	myresult=cursor.fetchall()
	for row in myresult:
		print(row)
def patient_info():
	import mysql.connector
	mydb=mysql.connector.connect(host="localhost",user="root",password="chiranthen54321",database="bloodbank")
	cursor=mydb.cursor()
	cursor.execute("SELECT * from Patient")



print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++++++++++BLOOD-BANK MANAGAMENT+++++++++++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

username=(input("Enter username:"))
password=(input("Enter Password:"))
if(username=="admin" and password=="root"):
	print("                                                                                       ")
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print("TO DONATE BLOOD ENTER 1:")
	print("TO REQUEST BLOOD ENTER 2:")
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


	opt=int(input("Enter Your Option:"))
	if(opt==1):
		name=(input("Enter Donar name:"))
		age=int(input("Enter Donar Age:"))
		contact_number=int(input("Enter Donar Contact number:"))
		bloodgroup=(input("Enter Donar Bloodgroup:"))
		address=(input("Enter Donar Address:"))
		donar(name,age,contact_number,bloodgroup,address)

	if(opt==2):
		name=(input("Enter Patient name:"))
		age=int(input("Enter Patient Age:"))
		contact_number=int(input("Enter Patient Contact number:"))
		bloodgroup=(input("Enter Patient Bloodgroup:"))
		address=(input("Enter Patient Address:"))
		hospital_name=(input("Enter Patient hospital_name:"))

		request_blood(name,age,hospital_name,contact_number,bloodgroup,address)
if(username=="mainadmin" and password=="mainroot"):
	print("+++++++++++++++++++++++++++++++++++WELCOME-ADMIN+++++++++++++++++++++++++++++++++++")
	print("TO SHOW ALL DATA ENTER 1:")
	opt2=int(input("Enter Your Option:"))
	if(opt2==1):
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		donar_info()
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	elif(opt2==2):
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		patient_info()
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	else:
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("ENTER A VALID OPTION")
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")