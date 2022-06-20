Feature: Java Introduction Tutorial Page

    As a user
    I want to view java Introduction tutorial page
    so that i can view all the introduction details about the java programming language that are available on the website

    Scenario: A user clicks on "Java Hello World" text on the Java Introduction card

        Given the user is on the programiz.com/java-programming page
        And also the user is visible to the Java Introduction card
        When the user clicks on the "Java Hello World" text
        Then the user should be redirected to java introduction page with the heading text
            """Java Hello World Program"""


    Background: The user is on the programiz.com/python-programming/hello-world page

    Scenario: A user clicks on "Java comments" text on the "How Java "Hello, World!" Program Works?" section

        Given the user is visible to the "Java comments" text
        When the user clicks on "Java comments" text
        Then the user is redirected to the java comments page
        And the user should see the heading with the text
            """Java Comments"""

    Scenario: A user clicks on the "Run Code" button on the Single-line Comment section

        Given the user is visible to the "Run Code" button on the Single-line Comment sectionon
        When the user clicks on the "Run Code" button
        Then the user should be redirected to the "online python compiler" page on the next tab
        And also the user should see the title of the page with the text
            """Online Java Compiler"""


    Scenario: A user clicks on Next Tutorial button on pagination section

        Given the user is visible to the next tutorial button
        When the user clicks on the next tutorial button
        Then the user should be redirected to the next following tutorial with the heading text
            """Java JDK, JRE and JVM"""