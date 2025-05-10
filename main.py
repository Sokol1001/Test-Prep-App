import mysql.connector
from colorama import Fore, Back, Style

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
        case 2:
            match subject_subtype:
                case 1:
                    myCursor.execute("SELECT * FROM Math WHERE question_id = 1")
                case 2: 
                    myCursor.execute("SELECT * FROM Math WHERE question_id = 2")
   
    for question in myCursor:
            questions_count += 1
            print(Fore.RED + question[1])
            print(Fore.GREEN + "1:", question[2])
            print(Fore.GREEN + "2:", question[3])
            print(Fore.GREEN + "3:", question[4])
            print(Fore.GREEN + "4:", question[5])
            #print("Answer Index:", question[6])
            answer = int(input("Answer: "))
            if(answer == question[6]):
                print("Correct!")
                correct_answers += 1
            else:
                print("Wrong! answer: " + str(question[6]))
            print("-" * 30)
    print("You answered " + str(correct_answers) + "/" + str(questions_count) + "correct")



myCursor = db.cursor()

def get_questions():
    subject_answer = int(input(Fore.YELLOW + "What you would like to practice? \n(1) English (2) Math \n"))
    if(subject_answer == 1):
        subtype_answer = int(input("What subtype you would like to practice? \n(1) Sentence completion (2) Restatements"))
    else:
        subtype_answer = int(input("What subtype you would like to practice? \n(1) Equations (2) "))
    print_question_set(subject_answer, subtype_answer)

def main():
    create_math_table()
    get_questions()

def create_math_table():
    # myCursor.execute("CREATE TABLE Math (" \
    # " question_id tinyint UNSIGNED," \
    # " question VARCHAR(500)," \
    # " option_1 VARCHAR(500)," \
    # " option_2 VARCHAR(500)," \
    # " option_3 VARCHAR(500)," \
    # " option_4 VARCHAR(500)," \
    # " answer tinyint," \
    # " id int PRIMARY KEY AUTO_INCREMENT)"
    # )
    
    #--! question_id - 1: Equations 2: Square roots and exponentiation !--

    myCursor.execute("INSERT INTO Math (question_id, question, option_1, option_2, option_3, option_4, answer) VALUES (%s, %s, %s, %s, %s, %s, %s)", (2,"a and c are whole numbers, 0<a<c \n a**c = c**a \n c=? " ,"5" ,"6","3", "4" , 4))

    #myCursor.execute("DELETE FROM Math WHERE id = '1'")  #--! Update the table !--
    db.commit()
    #myCursor.execute("SELECT * FROM Math")

    #for x in myCursor:
        #print(x)

main()