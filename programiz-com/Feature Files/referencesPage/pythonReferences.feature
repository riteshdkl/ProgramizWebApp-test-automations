Feature: Python References Page

    As a user
    I want to view All python references
    so that i can see all the references details that are available

    Background: the user is on the "https://dev.programiz.com/python-programming/methods" page

    Scenario: A user is searches a python function on the search bar

        Given the user is visible to the search bar with the placeholder "Search ..."
        When the user enters a key on the search bar
        Then the user should see the list of related search items with the heading text
            | Python Built-in Functions |
            | Python Set Methods        |
            | Python String Methods     |


    Scenario: A user clicks on "Python any()" text inside "Python Built-in Functions" section

        Given the use is visible to the "Python any()" text
        When the user clicks on "Python any()" text
        Then the user is redirected to the page wit the heading text
            """
            Python any()
            """


