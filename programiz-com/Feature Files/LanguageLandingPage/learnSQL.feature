Feature: Language landing page

    As a user
    I want to view language landing page
    so that i can view all the details about the language that are available on the web page

    Background: The user is on the Learn SQL page

    Scenario: A user sees "Learn SQL: SQL Tutorial for Beginners" heading
        Given the user is on the heading section
        When the user is visible to the text
        Then the user should see the heading with the text
            """
            Learn SQL: SQL Tutorial for Beginners
            """

    Scenario: A user clicks on "TUTORIALS" button
        Given the user is visible to the "TUTORIALS" button on the heading section
        When the user clicks on the "TUTORIALS" button
        Then the user should see the page being refreshed

    Scenario: A user clicks on "SQL EDITOR" button
        Given the user is visible to the SQL EDITOR button on the heading section
        When the user clicks on the "SQL EDITOR" button
        Then the user should be redirected to the sql editor page
        And also the user should see the url of the site being changed to
            """https://dev.programiz.com/sql/online-compiler"""

    Scenario: A user sees list of contents inside "Page Index" card
        Given the user is on the contents section
        When
        Then the user should see the list of contents with the text
            | Introduction          |
            | SQL SELECT (I)        |
            | SQL SELECT (II)       |
            | SQL JOIN              |
            | SQL Database          |
            | SQL Insert and Delete |
            | SQL Constraints       |
            | SQL Additional Topics |
            | About SQL             |
            | Why learn SQL?        |
            | How to Learn SQL?     |


    Scenario: A user clicks on "Online SQL Compiler" link
        Given the user is visible to the "Online SQL Compiler" link
        When the user clicks on the link
        Then the user shuld be redirected to the SQL Compiler page
        And also the user should see the url of the site being changed to
            """https://www.programiz.com/sql/online-compiler/"""

