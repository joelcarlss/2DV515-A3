import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="wikipedia"
)
# mydb.commit()

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE text (id INT PRIMARY KEY, name VARCHAR(255), category VARCHAR(255), text VARCHAR(1800))")


# Returns arrays with objects
def query_db(query, args=(), one=False):
    mycursor.execute(query, args)
    r = [dict((mycursor.description[i][0], value)
              for i, value in enumerate(row)) for row in mycursor.fetchall()]
    return (r[0] if r else None) if one else r

