Feature: JavaScript References Page

    As a user
    I want to view All JavaScript references
    so that i can see all the references details that are available



    Scenario: A user clicks on the "JavaScript Math sin()" text on the "JavaScript Math Object" section
        Given the user is visible to the "JavaScript Math sin()" text
        When the user clicks on the "JavaScript Math sin()" text
        Then the user should be redirected to the page with the heading text
            """JavaScript Math sin()"""


    Background: The user is on the "https://dev.programiz.com/javascript/library/math/sin" page

    Scenario: A user clicks on the "JavaScript Math atan()" text on the "Related Topics" section

        Given the user is visible to the "JavaScript Math atan()" text
        When the user clicks on the "JavaScript Math atan()" text
        Then the user is redirected to the page with the heading text
            """JavaScript Math atan()"""
