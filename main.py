import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database="testdatabase"
)

myCursor = db.cursor()

def main():
    print("x = " + vertical_fraction("-b +/- sqrt(b^2 - 4ac)", "2a"))
    create_databases()

#Make fractions look like real math equations    
def vertical_fraction(numerator, denominator):
    width = max(len(str(numerator)), len(str(denominator)))
    top = str(numerator).center(width)
    line = "-" * width
    bottom = str(denominator).center(width)
    return f"{top}\n{line}\n{bottom}"

def create_databases():
    #myCursor.execute("CREATE TABLE Test (name varchar(50))")  Create a table
    #myCursor.execute("DROP TABLE Test")  Delete a table

    myCursor.execute("CREATE TABLE English (id int PRIMARY KEY AUTO_INCREMENT, )")
    db.commit()

main()