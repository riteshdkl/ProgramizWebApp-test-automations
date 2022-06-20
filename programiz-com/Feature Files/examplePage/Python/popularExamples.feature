Feature: Python Popular Examples

    As a user
    I want to view python popular examples
    so that i can see the example details that are available



    Scenario: A user clicks on the "Python Program to Check Prime Number" card

        Given the user is on the programiz.com/python-programming/examples page
        And also the user is visible to the "Python Program to Check Prime Number" card
        When the user clicks on the "Python Program to Check Prime Number" card
        Then the user is redirected to the example page with the heading text
            """
            Python Program to Check Prime Number
            """


    Background: The user is on the programiz.com/python-programming/examples/prime-number page

    Scenario: A user clicks on "Python for loop" text on the heading section

        Given the user is visible to the "Python for loop" text
        When the user clicks on "Python for loop" text
        Then the user should be redirected to the for loop page with the heading text
            """
            Python for Loop
            """

    Scenario: A user clicks on the "Run Code" button on Example 1: Using a flag variable section

        Given the user is visible to the "Run Code" button on Example 1: Using a flag variable section
        When the user clicks on the "Run Code" button
        Then the user should be redirected to the "online python compiler" page on the next tab
        And also the user should see the heading of the page with the text
            """
            Python Online Compiler
            """

    Scenario: A user clicks on "happy face emoji" on "Did you find this article helpful?" section

        Given the user is visible to the "happy face emoji" on the "Did you find this article helpful?" section
        When the user clicks on "happy face emoji"
        Then the user should see the message on the screen with the text
            """
            We are glad you liked the article. Share with your friends.
            """

    Scenario: A user clicks on the "Check Armstrong Number" card on the Related Examples section

        Given the user is visible to the "Check Armstrong Number" card
        When the user on the "Check Armstrong Number" card
        Then the user is redirected to the page having heading text
            """
            Python Program to Check Armstrong Number
            """