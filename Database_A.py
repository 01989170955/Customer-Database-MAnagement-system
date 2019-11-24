import sqlite3
#backend
def studentData():
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, Firstname text,\
         Surname text, DoR text, DoD text, Age text, Gender text, Address text, Mobile text)")
    con.commit()
    con.close()
def addStdRec(StdID, Firstname, Surname, DoR, DoD, Age, Gender, Address, Mobile):
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    query = "insert into 'student' (StdID, Firstname, Surname, DoR, DoD, Age, Gender, Address, Mobile) values(?,?,?,?,?,?,?,?,?) "
    cur.execute(query, (StdID, Firstname, Surname, DoR, DoD, Age, Gender, Address, Mobile))
    con.commit()
    con.close()
def viewData():
    con =sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("SELECT * FROM student")
    rows =cur.fetchall()
    con.close()
    return rows
def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    rows = cur.fetchall()
    con.commit()
    con.close()
def searchData(StdID="", Firstname="", Surname="", DoR="", DoD="", Age="", Gender="", Address="", Mobile=""):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Firstname=? OR Surname=? OR DoR=? OR DoD=? OR Age=? OR Gender=? OR Address=? OR Mobile=? ", (StdID, Firstname, Surname, DoR, DoD, Age, Gender, Address, Mobile))
    rows=cur.fetchall()
    con.close()
    return rows
def dataUpdate(id,StdID="", Firstname="", Surname="", DoR="", DoD="", Age="", Gender="", Address="", Mobile=""):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID=?, Firstname=?, Surname=?, DoR=?, DoD=?, Age=?, Gender=?, Address=?, Mobile=?, WHERE id=?", (StdID, Firstname, Surname, DoR, DoD, Age, Gender, Address, Mobile, id))
    con.commit()
    con.close()
studentData()