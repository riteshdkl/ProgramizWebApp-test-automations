Feature: Python Functions Tutorial Page

    As a user
    I want to view python functions tutorial page
    so that i can view all the python functions details that are available on the website

    Scenario: A user clicks on "Function" text on the "Page Index" card

        Given the user is on the programiz.com/python-programming page
        And also the user is visible to the Page Index card
        When the user clicks on the "Function" text
        Then the user should see the page being scrolled down to the "Python Functions" card
        And also the user should see the list of python functions with the text
            | Python Functions           |
            | Function Argument          |
            | Python Recursion           |
            | Anonymous Function         |
            | Global, Local and Nonlocal |
            | Python Global Keyword      |
            | Python Modules             |
            | Python Package             |

    Scenario: A user clicks on "Python Functions" text on the Python Functions card

        Given the user is on the programiz.com/python-programming page
        And the user is visible to the Python Functions card
        When the user clicks on "Python Functions" text
        Then the user should should be redirected to Python Functions page with the heading text
            """Python Functions"""


    Background: The user is on the "programiz.com/python-programming/function" tutorial page

    Scenario: A user clicks on the "rules of writing identifiers in Python" text on "What is a function in Python?" section

        Given the user is visible to the "rules of writing identifiers in Python" text  on "What is a function in Python?" section
        When the user clicks on the "rules of writing identifiers in Python" text
        Then the user should to redirected to the "Rules for writing identifiers"
        And also the user should see the url being changed to
            """https://dev.programiz.com/python-programming/keywords-identifier#rules"""


    Scenario: A user clicks on the "Python Global Keyword" text on "Related Topics" card

        Given the user is visible to the "Python Global Keyword" text on the "Related Topics" card
        When the user clickson the "Python Global Keyword" text
        Then the user is redirected to the "Python Global Keyword" page
        And also the user should see the heading of the page with the text
            """Python Global Keyword"""


    Scenario: A user clicks on the "Run Code" button on the your Scope and Lifetime of variables section

        Given the user is visible to the "Run Code" button on the Scope and Lifetime of variables section
        When the user clicks on the "Run Code" button
        Then the user should be redirected to the "online python compiler" page on the next tab
        And also the user should see the heading of the page with the text
            """Python Online Compiler"""


    Scenario: A user clicks on "Previous Tutorial" button on pagination section

        Given the user is visible to the "Previous Tutorial" button
        When the user clicks on "Previous Tutorial" button
        Then the user is redirected to the previous tutorial page
