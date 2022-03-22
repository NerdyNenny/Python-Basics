#UPDATED ALU HANGMAN
# Creating two lists for the questions and answers respectively.
questions = ["When was ALU founded?", "Who is the CEO of ALU?", "Where are ALU campuses?", "How many campuses does ALU have?",
             "What is the name of ALU Rwanda’s Dean?", "Who is in charge of Student Life?", "What is the name of our Lab?",
             "How many students do we have in Year 2 CS?", "How many degrees does ALU offer?", "Where is the headquarters of ALU?"]
answers = ["2015", "Fred Swaniker", "Rwanda and Mauritius", "2", "Veda Sunasse", "Sila Ogidi", "Fab Lab", "92", "8", "Mauritius"]
print("Welcome to the ALU hangman game\n Let's see how much you know about your school\n")
#setting the initial value to count the number of score and mistakes

def replay():
    response = ["Yes", "yes", "yeah", "Yeah", "y", "Y"]
    reply = input("Do you want to play again?\n")
    if reply in response:
        game()
    else:
        exit()
def game():
    score = 0
    mistakes = 0
    while True:       # Using a while loop to iterate through the list with a set of conditions
        for x in questions:         #prints each question in the list of questions
            print(x)
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

        if score == 10:
            print("Congratulations, you saved the man!\n Your final score is ", score)
            replay()                     #calls the replay function
        elif score > 6:
            print("Thank you for saving the man!")
            print("You made ", mistakes, "mistakes.")
            replay()
        else:
            print("Sorry, you were not able to save the man")
            replay()
game()     #calls the function to start the game