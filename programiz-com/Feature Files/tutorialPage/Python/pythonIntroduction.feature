Feature: Python Introduction Tutorial Page

    As a user
    I want to view python Introduction tutorial page
    so that i can view all the introduction details about the python language that are available on the website

    Scenario: A user clicks on "Getting Started" text on the Introduction card

        Given the user is on the programiz.com/python-programming page
        And also the user is visible to the Introduction card
        When the user clicks on the "Getting Started" text
        Then the user should be redirected to introduction page with the heading text
            """
            How to Get Started With Python?
            """


    Background: The user is on the programiz.com/python-programming/first-program page

    Scenario: A user clicks on Red YouTube clickable button on the video introduction section

        Given the user is visible to the YouTube button
        When the user clicks on the button
        Then the user should see the video being played on the screen

    Scenario: A user clicks on "Thonny IDE" text on the Easiest Way to Run Python section

        Given the user is visible to the "Thonny IDE" text on the Easiest Way to Run Python section
        When the user clicks on the "Thonny IDE" text
        Then the user is should be redirected to the page with the url "https://thonny.org"
        And also the user should see the heading of the page with the text
            """
            Thonny
            """


    Scenario: A user clicks on the "latest version of Python" text on the install python separately section

        Given the user is visible to the "latest version of Python" text on the install python separately section
        When the user clicks on the "latest version of Python" text
        Then the user should be redirected to the page with the url "https://www.python.org/downloads/"

    Scenario: A user clicks on the "Run Code" button on the your first python program section

        Given the user is visible to the "Run Code" button on the your first python program section
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


    Scenario: A user clicks on "sad face emoji" on "Did you find this article helpful?" section

        Given the user is visible to the "sad face emoji" on the "Did you find this article helpful?" section
        When the user clicks on "sad face emoji"
        Then the user should see the message with the text "Sorry about that."
        And the user should see the text input message field
        And also the user should see a submit button with the text
            """
            Submit Feedback
            """


    Scenario: A user sees "Feedback field is required" error message when the message text area is empty and submit feedback button is clicked
        Given the user has already clicked sad face emoji
        When the user clicks on the sibmit feedback button
        Then the user should see error message with the text
            """
            Feedback field is required.
            """


    Scenario: A user clicks on next tutorial button on pagination section

        Given the user is visible to the next tutorial button
        When the user clicks on the next tutorial button
        Then the user should be redirected to the next following tutorial with the heading text
            """
            Python Keywords and Identifiers
            """


    Scenario: A user clicks on the "facebook icon"

        Given the user is on the "Did you find this article helpful?" section
        When the user clicks on the facebook icon
        Then the user should be redirected to share on facebook page
        And also the user should be visible to the programiz.com link that is to be shared

    Scenario: A user clicks on "Python IDEs and Code Editors" card on "Relted Tutorials" section

        Given the user is on the "Relted Tutorials" section
        When the user clicks on the "Python IDEs and Code Editors" card
        Then the user is redirected to the page with the heading text
            """
            Python IDEs and Code Editors
            """







