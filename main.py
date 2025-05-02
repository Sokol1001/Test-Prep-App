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
    create_tables()

#Make fractions look like real math equations    
def vertical_fraction(numerator, denominator):
    width = max(len(str(numerator)), len(str(denominator)))
    top = str(numerator).center(width)
    line = "-" * width
    bottom = str(denominator).center(width)
    return f"{top}\n{line}\n{bottom}"

def create_tables():
    #myCursor.execute("CREATE TABLE Test (name varchar(50))")  Create a table
    #myCursor.execute("DROP TABLE Test")  Delete a table

    # myCursor.execute("CREATE TABLE English (" \
    # " question_id tinyint UNSIGNED," \
    # " question VARCHAR(500)," \
    # " option_1 VARCHAR(500)," \
    # " option_2 VARCHAR(500)," \
    # " option_3 VARCHAR(500)," \
    # " option_4 VARCHAR(500)," \
    # " answer tinyint," \
    # " id int PRIMARY KEY AUTO_INCREMENT)"
    # )
    
    # --! question_id - 1: Sentence completion 2: Restatements 3: Reading comprehension !--

    #myCursor.execute("INSERT INTO English (question_id, question, option_1, option_2, option_3, option_4, answer) VALUES (%s, %s, %s, %s, %s, %s, %s)", (1, "After being ______ by France for decades, Cambodia became independent in 1953", "bought", "ruled", "translated", "filmed", 2))

    myCursor.execute("SELECT * FROM English")

    for x in myCursor:
        print(x)

main()