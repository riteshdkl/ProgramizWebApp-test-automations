Feature: Python Files Examples

    As a user
    I want to view python Files examples
    so that i can see all the File examples details that are available

    Scenario: A user clicks on the "Files" text on the screen
        Given The user is on the programiz.com/python-programming/examples page
        And the user is visible to the "Files" text
        When the user clicks on the "Files" text
        Then the user can see all the list of files related examples with the texts

    Scenario: A user clicks on the "Python Program to Check the File Size" text inside Files example

        Given The user is on the programiz.com/python-programming/examples page
        And the user is visible to the "Python Program to Check the File Size" text
        When the user clicks on the "Python Program to Check the File Size" text
        Then the user is redirected to the page with the heading text
            """Python Program to Check the File Size"""

