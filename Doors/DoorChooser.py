"""
This is a file that aims to choose what door is needed given a certain set of data.
"""


def ask(question, answers="integer"):
    """
    Ask user question given the question and possible answers.


    Answers defaults to asking for an integer, which can be specificied by setting it to "integer".

    If given the term "float", it will assume that the answer must be float.

    #TODO: Allow for floats without range restriction to have a decimal place restriction

    If given a tuple of 2 numbers it will take those to be the range of allowed numbers.
    If given a tuple of 3 numbers, it will take the third to be amount of decimal places allowed.
    (A negative number will infer numbers only divisible by 10^(-number), e.g. -2 allows 100, 200, 300, ...)

    If given a list, it will assume that the answers in that list are the allowed answers.
    (Case will be ignored)

    If given the term "boolean", only True, False, Yes, No, and similar will be accepted.
    (These will be returned as a boolean)

    If given the term "string", anything will be accepted as an answer.

    #TODO: Restructure function so that testing of call validity occurs before asking for a response.
    """

    # Asking question
    response = raw_input(str(question))

    if isinstance(answers, str):
        if answers == "integer":
            # Testing for response integer type
            try:
                response = int(response)
                return response
            except ValueError:
                # Recursive re-asking of question
                print("Sorry, only integers are allowed! Please try again.")
                return ask(question, answers)
        
        elif answers == "float":
            # Testing for response float type
            try:
                response = float(response)
                return response
            except ValueError:
                # Recursive re-asking of question
                print("Please enter a number.")
                return ask(question, answers)

        elif answers == "boolean":
            # Removes ambiguities due to case
            response = str(response).upper()

            # Removes any inadvertant whitespace at the beginning or end
            response = response.strip()

            # List of "True" and "False" terms:
            trueTerms = ['TRUE', 'YES', 'CORRECT', 'YUP', 'YEP', 'YE', 'YEA', 'YEAH', "YEH", 'OKAY', 'TRUE', 'POSITIVE']
            falseTerms = ['FALSE', 'NO', 'INCORRECT', 'NOPE', 'NAH', 'NUH', 'UNTRUE', 'NEGATIVE', 'NEVER']

            if response in trueTerms:
                return True
            elif response in falseTerms:
                return False
            else:
                # Recursive re-asking of question
                print "Sorry, I didn't understand you there. Could you please respond with either yes or no?"
                return ask(question, answers)


        elif answers == "string":
            # Returns anything (as a string)
            return str(response)


    elif isinstance(answers, tuple):
        # Testing for tuple's correct structure
        if (len(answers) == 2 or len(answers) == 3) and answers[0] < answers[1]:
            try:
                response = float(response)
                # Tuple in correct range?
                if response >= answers[0] and response <= answers[1]:
                    if len(answers) == 3:
                        # Tuple of allowed decimal places?
                        if round(response, answers[2]) == response:
                            return response
                        else:
                            # Wrong number of decimal places
                            if answers[2] > 0:
                                # Recursive re-asking of question
                                print("Please enter a value with a maximum of " + str(answers[2]) + " decimal places.")
                                return ask(question, answers)
                            elif answers[2] < 0:
                                # Recursive re-asking of question
                                print("Please enter a value divisible by " + str(10**(-answers[2])) + ".")
                                return ask(question, answers)
                            else:
                                # Edgecase of '0' being specified as the number of decimal places required.
                                print("Please enter an integer.")
                                # Recursive re-asking of question
                                return ask(question, answers)
                    else:
                        return response
                else:
                    print("Please enter a value between " + str(answers[0]) + " and " + str(answers[1]) + ".")
                    return ask(question, answers)
            except ValueError:
                # This should only run if there is an issue on the line where conversion to a float is attempted.
                print("Please enter a number.")
                return ask(question, answers)
            except TypeError:
                # This should only run if there is an issue on the line that rounds the response.
                print "There's an error with the way the question was constructed."
                print str(answers) + " has its third item as likely not being an integer"
                raise TypeError("Question construction error. Last value not an integer.")
        else:
            # Incorrect calling of the ask() function.
            print("There's an error with the way the question was constructed.")
            print str(answers) + " is either of inappropriate length or the min and max are swapped."
            raise ValueError("Question construction error. Min/Max swapped or bad length.")

    elif isinstance(answers, list):
        # The default is to not care about case.
        # However, if two answers are present that are identical if case isn't considered, case is considered.
        # This method assumes that no identical items are present even when case is considered.
        
        # Initialising no-case list and case registering boolean
        noCaseAnswers = []

        # Filling no-case list
        for item in answers:
            noCaseAnswers.append(str(item).upper())

        # Counting duplicate answers
        duplicates = 0
        for item_a in noCaseAnswers:
            for item_b in noCaseAnswers:
                if item_a == item_b:
                    duplicates += 1

        # Testing if duplicates is equal to the number of answers.
        # (As each answer should have registered a duplicate when comparing to itself)
        if duplicates == len(noCaseAnswers):
            answers = noCaseAnswers
            response = response.upper()

        # Testing for presence of response in answers list:
        if response in answers:
            return response
        else:
            print("Please enter one of the following items:")
            print str(answers)
            return ask(question, answers)

    else:
        print("There's an error with the way the question was constructed.")
        print str(answers) + " doesn't seem like an appropriate answer type"
        raise ValueError("Question construction error. Bad answer type.")


def exportToCSV():
    for line in 



def questionnaire():
    """
    Run the questionnaire and determine the appropriate door.

    This is the 'runner' function of this file. It should include all the logic that goes into deciding
    what door should be used, and outsource any other functionalities (such as asking questions) into
    other functions.

    Details to be exported:             Notes                                               Dependencies
     - Room Number                      .                                                   Floorplan
     - Door Number                      .                                                   Floorplan
     - Type                             ????                                                .
     - Leaf Width                       .                                                   , design choice
     - Leaf Height                      .                                                   Level height, design choice
     - Leaf Thickness                   .                                                   Sound proofing, fire resistance, temp difference, security
     - Finish                           ????                                                .
     - Frame Type                       (Material I think)                                  , design choice
     - Pivot Spring Head / Floor Box    .                                                   .
     - Hinges                           .                                                   .
     - Locks                            Entered information confusing (L1, L2, ??)          .
     - Cylinder                         ???? (Similar entry to locks)                       .
     - Keying Charges                   ^^                                                  .
     - Furniture                        ^^                                                  .
     - Door Closer                      .                                                   .
     - Door Seals                       Entered information confusing ((S1, S2), ??)        .
     - Electric Strike                  .                                                   .
     - Door Stops                       ^^                                                  .
     - Handles                          ^^                                                  .
     - Signage                          ????                                                .
     - Card Reader, Rex, Break Glass    ???? Entered information confusing (CR, REX, BG)    .
     - Handle Height                    (Not on door schedule)                              .
    """

    # Questions & preliminary processing
    if ask("With the room number, is there a letter/phrase before the number? ", "boolean"):
        roomNumberPhrase = ask("What's the letter/phrase? ", "string")
        roomNumber = ask("What's the number after this letter/phrase? ", "float")
    else:
        roomNumberPhrase = "Not Applicable"
        roomNumber = ask("What's the room number? ", "float")
    
    doorNumber = ask("What's the door Number? (These are usually per-room)", "integer")

    floorHeight = ask("How high is the floor the door is on? Please enter your answer in millimetres. ", "integer")
    heightFlush = ask("Should the door height be flush with the ceiling? ") # TAKE MORE INTO CONSIDERATION
    if heightFlush:
        doorHeight = floorHeight:
    else:
        # TAKE MORE INTO CONSIDERATION
        print("No? Some common door heights include 2040mm and 2340mm")
        ask("How high should the door be then? Please enter your answer in millimetres. ", (0, floorHeight))
