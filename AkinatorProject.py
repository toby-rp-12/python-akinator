
#Function to check if an answer is correct.
def comf(right):
    if right == "yes":
        return("Yay, I got it!")
    elif right == "no":
        return ("What? I give up. Keep in mind that I'm only coded to guess names in ONE class group.")
    else:
        return("Sorry, I don't understand what you typed. Whatever, I don't have the time for this. Bye!")

#Sets the amount of times user has played to 0.
play = 0

#Greets user.
print("Hello there! Welcome to Guess Who: Classroom Edition!")
name = input("Before we begin the game, a quick question. What is your name?")

#Checks if input is a number.
while True:
    try:
        Age = int(input("How old are you, " + name + "?"))
        if Age <= 0 or Age > 125:
            print("You shouldn't be alive. Please enter another age:")
        else:
            break
    except ValueError:
        print("WRITE A NUMBER, IT'S NOT THAT HARD:")
        continue

#Intro
print("Ah, got it. Totally not stealing your information now...")
placeholder = input("(Press enter to begin)")
print("")
print("Guess Who: Classroom Edition")
print("Write T for tutorial.")
print("Press ENTER to play.")
tutor = input()

#Tutorial
if tutor == "T" or tutor == "t":
    print("TUTORIAL:")
    print("I will try to guess the classmate in CS that you are thinking of in under 12 questions!")
    placeholder = input("(Press enter to continue)")
    print("Respond 'yes' or 'no' to answer the questions.")
    placeholder = input("(Press enter to continue)")
    print("I'm case sensitive, so don't use any spaces or uppercase letters.")
    placeholder = input("(Press enter to continue)")
    print("I'll take anything you write besides 'yes' as a no.")
    got = input("Write yes if you understand.")
    while got != "yes":
        print("Well, I guess you don't understand.")
        print("You have to answer the questions with either 'yes' or 'no'.")
        got = input("Got it now...? (write yes)")

#Sets go to 1 so user can play.
go = 1
while go == 1:
    #Asks questions to guess the classmate.
    print("")
    print("Let's get started then.")
    if input("My first question: Is your student a boy?") == "yes":
                am = input("Does your student’s name begin with letters A-M?")
                if am == "yes":
                    if input("Does your student have glases?") == "yes":
                        print("I know it! Your student is Daniel Olowina.")
                        print(comf(input("Right?")))
                    else:
                        if input("Is your student's first name Adam?") == "yes":
                            if input("Is your student in the Wellness Minyan?"):
                                print("I know it! Your student is Adam Reisfeld!")
                                print(comf(input("Right?")))
                            else:
                                print("I know it! Your student is Adam Nirenberg!")
                                print(comf(input("Right?")))
                        else:
                            if input("Does your student's last name INCLUDE an R?") == "yes":
                                if input("Does your student's last name START WITH an R?") == "yes":
                                    if input("Is your student in Helios (the student newspaper)?") == "yes":
                                        print("I know it! Your student is Li'el Ravin!")
                                        print(comf(input("Right?")))
                                    else:
                                        print("I know it! Your student is Max Rev!")
                                        print(comf(input("Right?")))
                                else:
                                    if input("Is your student In Steven's Social Studies Class (SS9-C)?") == "yes":
                                        print("I know it! Your student is Isaac Posner!")
                                        print(comf(input("Right?")))
                                    else:
                                        print("I know it! Your student is Miles Lalezarian.")
                                        print(comf(input("Right?")))
                            else:
                                if input("Did your student work on this project?") == "yes":
                                    print("I know it! Your student is Elijah Cassidy!")
                                    print(comf(input("Right?")))
                                else:
                                    print("I know it! Your student is Asher Bunkin!")
                                    print(comf(input("Right?")))
                else:
                    if input("Is your student in the Learning Lab?") == "yes":
                        if input("Is your student in Helios (the student newspaper)?") == "yes":
                            print("I know it! Your student is Toby Rapoport!")
                            print(comf(input("Right?")))
                        else:
                            print("I know it! Your student is Ronnie Borden!")
                            print(comf(input("Right?")))
                    else:
                        if input("Is your student's first name Simon?") == "yes":
                            print("I know it! Your student is Simon Cohen!")
                            print(comf(input("Right?")))
                        else:
                            print("I know it! Your student is Nathan German!")
                            print(comf(input("Right?")))
    else:
        hyphen = input("Is your student's last name hyphenated (includes a hyphen)?")
        if hyphen == "yes":
            if input("Is your student in Zev's math class (MATH9B-B)?") == "yes":
                print("I know it! Your student is Lily Cohen-Iwanowski!")
                print(comf(input("Right?")))
            else:
                print("I know it! Your student is Leora Bowers-Poulad!")
                print(comf(input("Right?")))
        else:
            if input("Does your student have glasses?") == "yes":
                print("I know it! Your student is Tova Samansky!")
                print(comf(input("Right?")))
            else:
                print("I know it! Your student is Tali Siegel!")
                print(comf(input("Right?")))
    #Ends game and increases amount of times user has played.
    play = play + 1
    print("")

    #Checks if user wants to play again.
    print("Press ENTER to play again.")
    plays = input("Write S to exit.")
    if plays == "":
        continue
    else:
        go = go + 1
        print("Thank you for playing, " + name + "!")
        print("You have played " + str(play) + " times!")
        break
