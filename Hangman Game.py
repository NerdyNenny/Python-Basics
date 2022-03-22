#ALU HANGMAN
# Creating two lists for the questions and answers respectively.
questions = ["When was ALU founded?", "Who is the CEO of ALU?", "Where are ALU campuses?", "How many campuses does ALU have?",
             "What is the name of ALU Rwanda’s Dean?", "Who is in charge of Student Life?", "What is the name of our Lab?",
             "How many students do we have in Year 2 CS?", "How many degrees does ALU offer?", "Where is the headquarters of ALU?"]
answers = ["2015", "Fred Swaniker", "Rwanda and Mauritius", "2", "Veda Sunasse", "Sila Ogidi", "Fab Lab", "92", "8", "Mauritius"]

print("Welcome to the ALU hangman game\n")
#setting the initial value to count the number of score and mistakes
score = 0
mistakes = 0

while True:       # Using a while loop to iterate through the list with a set of conditions
    for question in questions:         #prints each question in the list of questions
        print(question)
        answer = input("Please enter the answer to this question\n")
        if answer in answers:      #checks if the player's input is included in the list of answers
            print("That is correct!")
            score += 1              #increases the score by 1 count
            print(score)
        else:
            print("You are hanging the man!")
            mistakes += 1           #increases the mistakes by 1
        if mistakes <= 6:
            print("You made ", mistakes, "mistakes. Your man is still safe")
        else:
            print("You made ", mistakes, "mistakes. Your man is hanged")
            exit()                          #exits the code when the player makes more than 6 total mistakes

    print("Your final score is ", score)
    if score == 10:
        print("Congratulations, you saved the man!\n Your final score is ", score)
        exit()                            #exits the code when the condition is met
    elif score <= 6:
        print("Thank you for saving the man!")
        print("You made ", mistakes, "mistakes.")
        exit()
    elif score > 6:
        print("You made", mistakes, " number of mistakes. But your man still lives!")
        exit()

    else:
        print("Sorry, you were not able to save the man")
        exit()