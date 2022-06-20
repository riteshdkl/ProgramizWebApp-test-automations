Feature: Python All Examples

    As a user
    I want to view python All examples
    so that i can see all the example details that are available

    # Background: The user is on the programiz.com/python-programming/examples page

    Scenario: A user clicks on "Python Program to Print Hello world!" text on the examples list

        Given The user is on the programiz.com/python-programming/examples page
        And the user is visible to the "Python Program to Print Hello world!" text
        When the user clicks  on "Python Program to Print Hello world!" text
        Then the user should be redirected to the hello-world example page with the heading text
            """
            Python Program to Print Hello world!
            """

    Scenario: A user clicks on "How to Get Started With Python?" text on print hello world example page

        Given the user is on the https://dev.programiz.com/python-programming/examples/hello-world page
        And the user is visible to the "How to Get Started With Python?" text
        When the user clicks on the "How to Get Started With Python?" text
        Then the user should be redirected to the page with the heading text
            """
            How to Get Started With Python?
            """

    Scenario: A user clicks on "Convert Kilometers to Miles" text on the Python Examples Card

        Given the user is on the https://dev.programiz.com/python-programming/examples/hello-world page
        And the user is visible to the "Convert Kilometers to Miles" text
        When the user clicks on "Convert Kilometers to Miles" text
        Then the user should be redirected to the Python Program to Convert Kilometers to Miles page
        And the user should see the url being changed to
            """https://dev.programiz.com/python-programming/examples/km-mile"""

    Scenario: A user clicks on "Python Strings" text on the Related Topics Card

        Given the user is on the https://dev.programiz.com/python-programming/examples/hello-world page
        And the user is visible to the "Python Strings" text
        When the user clicks on "Python Strings" text
        Then user should be redirected to the Python Strings Tutorial Page
        And the user should see the url being changed to
            """https://dev.programiz.com/python-programming/examples/string"""