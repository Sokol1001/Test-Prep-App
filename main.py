import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database="testdatabase"
)

def print_question_set(subject, subject_subtype):
    correct_answers = 0
    questions_count = 0

    match subject:
        case 1:
            match subject_subtype:
                case 1:
                    myCursor.execute("SELECT * FROM English WHERE question_id = 1")
                case 2: 
                    myCursor.execute("SELECT * FROM English WHERE question_id = 2")
   
    for question in myCursor:
            questions_count += 1
            print(question[1])
            print("A:", question[2])
            print("B:", question[3])
            print("C:", question[4])
            print("D:", question[5])
            #print("Answer Index:", question[6])
            print("-" * 30)
            answer = input("Answer: ")
            if(answer == question[6]):
                print("Correct!")
                correct_answers += 1
            else:
                print("Wrong! answer: " + question[6])
    print("You answered " + correct_answers + "/" + questions_count + "correct")



myCursor = db.cursor()

def get_questions():
    subject_answer = int(input("What you would like to practice? \n(1) English (2) Math \n"))
    if(subject_answer == 1):
        subtype_answer = int(input("What subtype you would like to practice? \n(1) Sentence completion (2) Restatements"))
        print_question_set(subject_answer, subject_answer)

#Make fractions look like real math equations    
def vertical_fraction(numerator, denominator):
    width = max(len(str(numerator)), len(str(denominator)))
    top = str(numerator).center(width)
    line = "-" * width
    bottom = str(denominator).center(width)
    return f"{top}\n{line}\n{bottom}"

def main():
    #print("x = " + vertical_fraction("-b +/- sqrt(b^2 - 4ac)", "2a"))
    get_questions()

main()

#def create_tables():
    #myCursor.execute("CREATE TABLE Test (name varchar(50))")  Create a table
    #myCursor.execute("DROP TABLE Test")  Delete a table
    #create_english_table()


#def create_english_table():
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

    #myCursor.execute("INSERT INTO English (question_id, question, option_1, option_2, option_3, option_4, answer) VALUES (%s, %s, %s, %s, %s, %s, %s)", (2, "The United States is the largest producer of oranges in the world.", "The United States is the largest country in the world that grows oranges.", "More oranges are sold in the United States than in any other country.", "The oranges produced in the United States are the largest in the world.", "No other country grows as many oranges as the United States.", 4))

    #myCursor.execute("UPDATE English SET answer = '3' WHERE id = '11'")  --! Update the table !--
    #db.commit()
    #myCursor.execute("SELECT * FROM English")

    #for x in myCursor:
        #print(x)