#Feature file for Online Programiz compiler
Feature: Programiz Online Compiler

    As a user
    I want to Run my codes in the compiler
    So that i can get accurate outputs for my inputted codes

    Background: Reaching the compiler
        Given The user has visited the programiz online compiler interface

    #1.  Normally yo scenario haru genenralised gareka hun (same scenario for all 6 compiler so yes ma hamile code ma
    # actual string value haleka xainam. So if we need to put actual value halne bela ma ki scenario output garne
    #or maile socheko test case ma kura milaune)

    #2. Similarly scenario generalised ho. so yesuta language ma kaam lagne scenario aarko language ma na milna ni sakxa
    # So please test that also

    #Scenario 1
    Scenario Outline: The user tries to access the main page
        Given the user has visited and/and not used the compiler interface
        When the user clicks the |Programiz| <compiler text> link
        Then the user is redirected to the programiz home page in a new tab
        Examples:
            #The first line is the header (variable) and lines after that denotes the values of the variable
            | compiler text              |
            | Python online compiler     |
            | C online compiler          |
            | C++ online compiler        |
            | Java online compiler       |
            | C# online compiler         |
            | JavaScript online compiler |

    #Scenario 2
    Scenario Outline: The user tries to learn the desired language through mobile application
        Given the user is currently accessing the compiler of the desired language
        When the user presses the button Learn <language> app
        Then the user is redirected to the mobile tutorial link of that specific language
        Examples:
            | language   |
            | Python     |
            | C          |
            | C++        |
            | Java       |
            | C#         |
            | JavaScript |

    #Scenario 3
    Scenario Outline: The user wants to access the desired compiler
        Given the user is in the online compiler interface
        When the user clicks the specific <compiler-button> button
        Then the user is redirected to that specific compiler in another tab
        Examples:
            | compiler-button |
            | ( python icon)  |
            | ( C icon)       |
            | ( C++ icon)     |
            | ( Java icon)    |
            | ( C# icon)      |
            | ( JS icon)      |
            | ( SQL icon)     |

    #Scenario 4
    Scenario: The user wants to enter the full screen mode
        Given the user is in the specific compiler interface
        But the compiler instance is not in full screen mode
        When the user clicks the button
            | (Enlarge icon) |
        Then the compiler instance is enlarged

    #Scenario 5
    Scenario: The user wants to exit the full screen mode
        Given the user is in the specific compiler interface
        But the compiler instance is in full screen mode
        When the user clicks the button
            | (Shrink icon) |
        Then the compiler instance is shrinked

    #Scenario 6
    Scenario: The user wants to change the theme of the compiler instance to dark mode
        Given the user is in ther specific compiler interface
        And the user is in light mode
        When the user presses the button
            | (Moon icon) |
        Then the theme of the compiler changes to dark mode
        And the user sees the compiler interface in dark mode

    #Scenario 7
    Scenario: The user wants to change the theme of the compiler instance to light mode
        Given the user is in ther specific compiler interface
        And the user is in dark mode
        When the user presses the button
            | (Sun icon) |
        Then the theme of the compiler changes to light mode
        And the user sees the compiler interface in light mode

    #yesma problem huna sakxa (language)
    #Scenario 8
    Scenario: The user wants to check whether the theme of that specific instance has changed or not during closing and repoening of that compiler instance
        Given the user has the compiler in the desired theme
        And the user has closed that compiler tab
        When the user selects that same compiler instance
        Then the user is redirected to that same compiler
        And the theme of the compiler is same as the one when the compiler was closed

    #Scenario 9
    Scenario: The user tries to run the inputted text
        #scenario for just running the text (not any code)
        #run button chalxa ki nai vanna ko lagi matrai ho
        Given the user has inputted the text in the compiler text area
            """
            hello
            """
        When the user clicks the primary "Run" button
        Then some text is printed in the shell/output section of the interface

    #Scenario 10
    Scenario: The user tries to clear the present text in the output/shell field
        Given the user has run the inputted text/code
        And appropriate text has been printed in the output/shell field
        When the user clicks the "Clear" button
        Then the text printed in the output/shell field is cleared

    #Scenario 11
    Scenario: The user tries to run a correct code
        #Normal accurate program
        Given the user has inputted a syntatically correct code
        When the user clicks the |Run| button
        Then appropriate result is displayed in the output/shell section

    #Scenario 11
    Scenario: The user tries to run a syantatically incorrect code
        #typo vako code
        Given the user has inputted a syntatically incorrect code
        When the user clicks the "Run" button
        Then the user should see this message
            """
            SyntaxError: invalid syntax
            """
        And the location and point of the invalid syntax is printed

    #Scenario 12
    Scenario: The user tries to check a semantically correct code
        Given the user has inputted a syntatically correct code
        And the code in semantically correct
        And the user clicks "Run" button
        When the output is displayed in the output/shell field
        Then the output of the field should match the users expection

    #Scenario 13
    Scenario: The user tries to check a semantically incorrect code
        #program milxa run pani hunxa but unexpected answer aauxa
        Given the user has inputted a syntatically correct code
        But the code in semantically incorrect
        And the user clicks "Run" button
        When the output is displayed in the output/shell field
        Then the output of the field should not match the users expection

    #Scenario 14
    Scenario: The user tries to check a runtime error
        #Exception
        Given the user has inputted a syntatically and semantically correct code
        But the code has a runtime error
        When the user clicks "Run" button
        Then an error message is displayed

    #Scenario 15
    Scenario Outline: The user tries to run a program that tries to import user-defined packages
        Given the user is in <compiler>
        And the user has inputted an accurate code
        But the program has user defined packages
        When the user clicks the "Run" button
        Then the user sees the <error> message
        Examples:
            | compiler   | error                                                                                |
            | Python     | A module you have imported isn't available at the moment. It will be available soon. |
            | C          | No such file or directory                                                            |
            | C++        | No such file or directory                                                            |
            | Java       | package doesnot exist                                                                |
            | C#         | The type or namespace could not be found                                             |
            | JavaScript | SyntaxError                                                                          |

    #Scenario 16
    Scenario Outline: The user tries to run empty instance of the compiler
        Given the user is in <compiler>
        But the user has cleared the compiler instance
        When the user clicks the "Run" button
        Then the user sees the <clear_condition> message
        Examples:
            #Empty string ( || ) vaneko k lekhnu parxa thaha navako
            | compiler   | clear_condition                                                                                          |
            | Python     |                                                                                                          |
            | C          | /usr/bin/ld:cannotopenoutputfilea.out:Permission denied collect2: error: ld returned 1 exit status       |
            | C++        | /usr/bin/ld: cannot open output file a.out: Permission denied collect2: error: ld returned 1 exit status |
            | Java       | Program does not contain a static 'Main' method suitable for an entry point                              |
            | C#         | Program does not contain a static 'Main' method suitable for an entry point                              |
            | JavaScript |                                                                                                          |

    #Scenario 17
    Scenario: The user tries to run program that creates unwanted results for the system
        #Results include shutting down of the system, opening of cmd and so on
        Given ther user has inputted program that is accurate
        But the program results in conditions that is unwanted by the system
        When the user clicks "Run" button
        Then the program is not run


#The following are the scenarios specificially for SQL editor so we start the counting from 1