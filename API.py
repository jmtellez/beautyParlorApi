__author__ = 'Juan Tellez'

import mysql.connector

cnx = mysql.connector.connect(user='root', password='jmt3559', host='localhost', database='BeautyParlor')
cursor = cnx.cursor()

def getStaffByPosition(position):
    query=("SELECT fName,lName FROM Staff WHERE position='"+ position+"'")
    cursor.execute(query)
    print ('First Name'+'\t'+'Last Name').expandtabs(15)
    for i in cursor:
        print (str(i[0])+'\t'+str(i[1])).expandtabs(15)

def getStaffByOwner(owner_id):
    query=('SELECT S.fName, S.lName FROM Staff S, Owner O WHERE O.owner_id=S.owner_id AND S.owner_id='+ owner_id)
    cursor.execute(query)
    print ('First Name'+'\t'+'Last Name').expandtabs(15)
    for i in cursor:
       print (str(i[0])+'\t'+str(i[1])).expandtabs(15)

def getClientInfo(aptTime, staff_id):
    query=("SELECT C.fName, C.lName, C.phoneNo, A.aptTime, A.aptDate FROM Staff S, Client C, Appointments A WHERE A.client_id = C.client_id AND A.staff_id = S.staff_id AND A.aptTime > '"+aptTime+"' AND S.staff_id ="+staff_id)
    cursor.execute(query)
    print ('First Name'+'\t'+'Last Name'+'\t'+ 'Phone Number'+'\t'+'AptTime'+'\t'+'AptDate').expandtabs(15)
    for i in cursor:
        print (str(i[0])+'\t'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3])+'\t'+str(i[4])).expandtabs(15)



def getProductCount(brand):
    query=("SELECT COUNT(I.brand) From Inventory I WHERE I.brand='"+ brand +"'")
    cursor.execute(query)
    print "Count"
    for i in cursor:
        print i[0]

def getStaffByAppointments(aptTime, count):
    query=("SELECT staff.staff_id, staff.fName, staff.lName FROM Staff staff, Appointments appointments WHERE staff.staff_id=appointments.staff_id 	AND appointments.aptTime='"+aptTime+"' GROUP BY staff.staff_id HAVING COUNT(*)>="+str(count))
    cursor.execute(query)
    print ('Staff ID'+'\t'+'First Name'+'\t'+ 'Last Name').expandtabs(15)
    for i in cursor:
        print (str(i[0])+'\t'+str(i[1])+'\t'+str(i[2])).expandtabs(15)

def getStaffForEval(freeTime,aptTime):
    query=("SELECT DISTINCT S.fName, S.lName, S.position FROM Staff S, Appointments A WHERE S.staff_id=A.staff_id AND A.aptTime='"+aptTime+"' AND NOT EXISTS (SELECT * FROM Staff St, Appointments Ap WHERE St.staff_id=Ap.staff_id AND Ap.aptTime='"+freeTime+"' AND S.staff_id=St.staff_id)")
    cursor.execute(query)
    print ('First Name'+'\t'+'Last Name'+'\t'+ 'Position').expandtabs(15)
    for i in cursor:
        print (str(i[0])+'\t'+str(i[1])+'\t'+str(i[2])).expandtabs(15)

def showMenu():
        print "\nBeautyParlor API Test Menu\n 1: Get Staff by Position\n 2: Get Staff by Owner ID\n 3: Get Staff's Appointments Info\n 4: Get Number of Products by Brand\n 5: Get Staff by Number of Appointments\n 6: Get Staff for Evaluation\n -1: Quit\n"

