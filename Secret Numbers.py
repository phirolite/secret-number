#Devils Plan Secret Numbers Game: Concept1: find x and y by using three conditional rules to see if you can narrow down x and y values. 
import random # [random] to allow randomising x and y #[math] to allow use of math.floor to remove decimal 
import math 

class Rules_hints: #sets up Rules by name, text, example and type
    def __init__(self, name, text, example , type):
        self.name = name
        self.text  = text 
        self.example = example
        self.type = type
    def __repr__(self) -> str:
        return self.name

class Input_Vars(): #sets up Inputs by title,  display_text, User_Options and Answers
    def __init__(self, title = "", display_text = "", User_Options = "", Answers = "") -> None:
        self.title = title
        self.display_text = display_text
        self.User_Options = User_Options
        self.Answers = Answers
    # To include NAME - LIST of USER_OPTIONS list of ANSWERS
    #     # CALL FUNCTION for each QUESTION 

def rules(): #Function: Prints out rules 
    Rule1= Rules_hints("Addition","Addtion rule will show X + Y as whole number","6 and 40 = 46 shows 46","rule")
    Rule2= Rules_hints("Multiple","Multiple X * Y and only shows last digit.","6*40 = 240 shows as 0","rule")
    Rule3= Rules_hints("Devision","Division X > Y where larger number is divided by the smaller and shown as a whole number, no decilmals.","40 / 6 = 6.67 will show as a 6","rule")
    Hint1= Rules_hints("Zero's","Zero's show the number of Zeros in a number between X and Y.","6 to 40 has 10 20 30 so shows as 3","hint")
    print("")
    print("Rule one {}: {} Example: {}".format(Rule1.name,Rule1.text,Rule1.example))
    print("Rule two {}: {} Example: {}".format(Rule2.name,Rule2.text,Rule2.example))
    print("Rule three {}: {} Example: {}".format(Rule3.name,Rule3.text,Rule3.example))
    print("Rule four {}: {} Example: {}".format(Hint1.name,Hint1.text,Hint1.example))
    print("")

class GameCommands():
    def __init__(self, Command ="" , Discription = "") -> None:
        self.Command = Command
        self.Discription = Discription

    def Help(): #Shows Game Menu and Commands
        GameCommands.Game_Menu()
    def Rules(): #Shows rules
        rules()#Runs Rules 
    def Game_Menu(): #Prints Game Menu
        print("")
        print("GAME MENU")
        print("")
        print("START : Allows user to start the game.")
        print("RULES : Shows the rules of the Game")
        print("CLUE  : Buy a clue from one of the four options.")
        print("GUESS : Make a guess of the values of X and Y.") 
        print("HINT  : Buy a hints view of all possible options [Only works after clues given]") 
        print("EXIT  : Quit the Secret Numbers") 
        print("")

#create named lists <<< here >>>
def numbers_1_to_100(): #Creates list from 1 to 100
    items = list(range(1,101))
    return items
def numbers_paired(): #Creates all possible pairs EG: [1,2],[1,3]......[98,99],[98,100],[99,100]
    paired = []
    valx = 0 
    valy = 0 
    for valx in range(1,101):
        for valy in range(1,101):
            if valx != valy and valx < valy:
                paired.append([valx,valy])
    return paired
num_1_to_100_list = numbers_1_to_100()
numbers_paired_list = numbers_paired()
numbers_in_tens = [10,20,30,40,50,60,70,80,90]
def sortAndUniq(input): #function to sort numbers in order and only return unique numbers 
  output = []
  for AB in input:
    if AB not in output:
      output.append(AB)
  output.sort()
  return output

def values_of_x_and_y(): #randomises X and Y making sure X is less and not equal to Y 
    x = random.randint(1,100)#random Numbers for when code is live)
    y = random.randint(1,100)#random Numbers for when code is live
    while x >= y: 
        x = random.randint(1,100)#random Numbers for when code is live
        y = random.randint(1,100)#random Numbers for when code is live
    return x , y 
x_and_y = values_of_x_and_y()# list of X and Y generated at random. 
x_target = x_and_y[0]# Assigns X to Target variables
y_target = x_and_y[1]# Assigns Y to Target variables

def Possible_value_addition(x_target,y_target): #creates list of all possible for this clue. used for logic
    Possible_values = []
    for items in numbers_paired_list:
        x = items[0]
        y = items[1]
        if (x + y) == (x_target + y_target): 
            Possible_values.append(x)
            Possible_values.append(y)
    return Possible_values
Possible_value_additions_sorted = sortAndUniq(Possible_value_addition(x_target,y_target)) #sorts list into order 
def Possible_value_Multiply(x_target,y_target): #creates list of all possible for this clue. used for logic
    Possible_values = []
    for items in numbers_paired_list:
        x = items[0]
        y = items[1]
        target_result = str(x_target * y_target)
        test_result =  str(x * y)
        if test_result[-1] == target_result[-1]: 
            Possible_values.append(x)
            Possible_values.append(y)
    return Possible_values
Possible_value_Multiply_sorted = sortAndUniq(Possible_value_Multiply(x_target,y_target)) #sorts list into order 
def Possible_value_Division(x_target,y_target): #creates list of all possible for this clue. used for logic
    Possible_values = []
    for items in numbers_paired_list:
        x = items[0]
        y = items[1]
        target_result = math.floor(y_target / x_target)
        test_result =  math.floor(y /x)
        if test_result == target_result: 
            Possible_values.append(x)
            Possible_values.append(y)
    return Possible_values
Possible_value_Division_sorted = sortAndUniq(Possible_value_Division(x_target,y_target)) #sorts list into order 

def set_single_values(): #create list of just possible numbers that apear in all three of the above lists.
    Result = []
    for each in Possible_value_additions_sorted:
        if each in Possible_value_Multiply_sorted and each in Possible_value_Division_sorted:
            Result.append(each)
    return Result
single_values = set_single_values()
def set_pairs(): #now created new pairs lists that are the only possible combinations of untested numbers 
    Result = []
    for each_x in single_values: 
        for each_y in single_values: 
            if each_x != each_y: 
                Result.append([each_x,each_y])
    return Result
possible_pairs_untested = set_pairs()
def tested_pairs(x_target,y_target): # tests the new pair list to see if meets all three conditions. And adds to new list. 
    Result = []
    for each in possible_pairs_untested: 
        test_1A = (each[0] + each[1])
        test_1B = (x_target + y_target)
        test_2A = str(each[0] * each[1])
        test_2B = str(x_target * y_target)
        test_3A = math.floor(each[1] / each[0])
        test_3B = math.floor(y_target / x_target)
        #print(each)
        #print("Test ADD: {}/{}".format(test_1A , test_1B))
        #print("Test MUL: {}/{}".format(test_2A[-1] , test_2B[-1]))
        #print("Test DIV: {}/{}".format(test_3A , test_3B))
        #print("---")
        if test_1A == test_1B and  test_2A[-1] == test_2B[-1] and test_3A == test_3B: 
            Result.append(each)
    return Result
possible_pairs_tested = tested_pairs(x_target,y_target)# This will be used to give user a hint if they are struggling to guess by giving them all the optional pairs. 
def Task1(x_target,y_target): #Completes X + Y 
    return x_target + y_target
def Task2(x_target,y_target): #Completes X * Y and returning only last digit
    result = str(x_target * y_target)
    return result[-1]
def Task3(x_target,y_target): #Completes Y / X and returning only whole number as result. 
    result = math.floor(y_target / x_target)
    return result
def Task4(x_target,y_target): #Completes X to Y and how numbers ending in Zero that it passes
    count = 0 
    for val in range(x_target,y_target):
        if val in numbers_in_tens:
            count += 1
    return count
Count_of_Tens = Task4(x_target,y_target)

def Get_Clues():#function to allow user to select clues
    Get_clues = True
    while Get_clues is True: 
        user_input = input("Do you want a clue? Y/N ")
        user_input = user_input.upper()
        selecting = True
        while selecting == True: 
            if user_input == "YES" or user_input == "Y":
                print("")
                print("Which clue would you like? ")
                print("")
                print("1: Clue on Addition's")
                print("")
                print("2: Clue on Multiplication's")
                print("")
                print("3: Clue on Division's")
                print("")
                print("4: Clue on Zero's")
                print("")
                print("5: No further clues needed")
                print("")
                Get_clues = False
                selection = True
                while selection == True: 
                    try: 
                        user_input = int(input("Which one do you select?  1 to 5 allowed: "))
                        if user_input == 1:
                            print("---")
                            print("The sum of the numbers equals {}.".format(Task1(x_target,y_target)))
                            print("---")
                        elif user_input == 2:
                            print("---")
                            print("The last digit of the numbers multiplied together is {}.".format(Task2(x_target,y_target)))
                            print("---")
                        elif user_input == 3:
                            print("---")
                            print("The larger number divided by the smaller number as a whole is {}.".format(Task3(x_target,y_target)))
                            print("---")
                        elif user_input == 4:
                            print("---")
                            print("There are {} numbers ending in Zero between the lower and higher number.".format(Task4(x_target,y_target)))
                            print("---")
                        elif user_input == 5:
                            selecting = False
                            selection = False
                            print("")
                        elif user_input < 1 and user_input > 5: 
                            print("Must be a number between 1 and 5")
                    except ValueError:
                        print("Must be a number between 1 and 5")
            else: 
                selection = False
                selecting = False
                Get_clues = False
                print("")
def Guesses(): #function to allow user to make guesses
        Valid_Guesses_Loop = True
        while Valid_Guesses_Loop == True: 
            try_x_loop = True
            while try_x_loop == True:
                try: 
                    try_x = int(input("What do you think is value of the lower number is? "))
                    print("")
                    if try_x > 99 or try_x < 1:
                        print("Value must be between 1-99.")#Message to user
                        print("")
                        try_x_loop = True
                    else: 
                        try_x_loop = False
                except ValueError:
                    print("Lower must be a number.")
                    print("")
                    try_x_loop = True
            try_y_loop = True
            while try_y_loop == True:
                try:
                    try_y = int(input("What do you think is value of the higher number is? "))
                    print("")
                    if try_y <= try_x: 
                        print("Second value must be between 2-100 and higher than {}.".format(try_x))#Message to user
                        print("")
                        try_y_loop = True
                    else: 
                        try_y_loop = False
                except ValueError:
                    print("Higher must be a number.")
                    print("")
                    try_y_loop = True
                Valid_Guesses_Loop = False
        return try_x , try_y                 
def check_results(try_X_as,try_y_as):
    check_results = True 
    while check_results == True:
        print("Your guess is {} and {}.".format(try_X_as,try_y_as))
        print("")
        if x_target == try_X_as and y_target == try_y_as:
            print("Correct {} is {} and {} is {}, you have won! ".format("X",x_target,"Y",y_target))
            print("")
            check_results = False
        else: 
            print("Incorrect answer.")
            print("")
            Re_Guess_Loop = True
            while Re_Guess_Loop == True:
                try:
                    re_try = input("Do you want to try again? YES or NO. ")
                    print("")
                    re_try = re_try.upper()
                    if re_try == "YES" or re_try == "Y":
                        ask_for_hint = input("Do you wish to have a hint? Y/N ")
                        print("")
                        ask_for_hint = ask_for_hint.upper()
                        if ask_for_hint == "YES" or ask_for_hint == "Y":
                            print("The possible pairs are as follows {}.".format(possible_pairs_tested))
                            print("")
                        Get_guesses = Guesses()
                        try_X_as = Get_guesses[0]
                        try_y_as = Get_guesses[1]
                        Re_Guess_Loop = False
                    elif re_try == "NO" or re_try == "N":
                        print("{} was {} and {} was {}, better luck next time. ".format("x",x_target,"Y",y_target))
                        print("")
                        Re_Guess_Loop = False
                        check_results = False
                    else:
                        pass
                except ValueError:
                    print("must be Yes or No value")
                    Re_Guess_Loop = True
                else:
                    pass
                pass #end of Guesses Loop
def GAME(): #Runs GAME askes if they want certain clues. Then Allows user to guess. [Given hint if needed]
    Get_Clues()
    Get_guesses = Guesses()
    try_X_as = Get_guesses[0]
    try_y_as = Get_guesses[1]
    check_results(try_X_as,try_y_as)

#Start Game
Exit_Game = False
Loop_Input = True
while Exit_Game == False: #runs until told to exit game
    while Loop_Input == True:
        #welcome message HERE? 
        print("1:Play Game")
        print("2:Rules")
        print("3:Help")
        print("4:Exit")
        print("")
        try:
            User_input_Commands = int(input("Please select between 1 - 4. " ))
            print("")
            if User_input_Commands < 1 or User_input_Commands > 4:
                print(" Incorrect, Please select between 1 - 4. ")
                print("")
            else:
                if User_input_Commands == 1:
                    GAME()#play GAME 
                    Exit_Game = True
                    Loop_Input = False
                elif User_input_Commands == 2:
                    GameCommands.Rules()
                    Loop_Input = True
                elif User_input_Commands == 3: 
                    show_help = GameCommands.Help()
                    Loop_Input = True
                elif User_input_Commands == 4:
                    Exit_Game = True
                    Loop_Input = False
                else:
                    Loop_Input = True
        except ValueError:
            print("Must be a number.")
exit_game = input("Exiting Game. ")
